import os
import sys
import grpc
import time
import json
import django
import datetime
import requests
from concurrent import futures


from live_app.grpc_tool import live_pb2, live_pb2_grpc
from live_app.models import LiveStream, LiveRecord, LivePlayBack, PlayStream
from live_app.qiniu_tool import query_stream, create_stream, pull_stream_url,\
    get_play_urls, disable_stream, query_historyactivity, play_back as get_play_back
from redis_tool import RedisConnector

import hashlib

cache_conn = RedisConnector().CacheRedis


def json_response(func):
    def wrapper(view, request, context):
        res_data = func(view, request, context)
        json_data = json.dumps(res_data)
        return live_pb2.json(text=json_data)
    return wrapper


class LiveManagement(live_pb2_grpc.LiveManagementServicer):
    @json_response
    def AddLive(self, request, context):
        data = json.loads(request.text)
        play_streams = data.pop('play_streams')
        live_record = LiveRecord.objects.create(**data)
        for play_stream in play_streams:
            play_stream['user_id'] = data['user_id']
            play_stream['live_record_id'] = live_record.id
            PlayStream.objects.create(**play_stream)
        data = dict(status='success')
        return data

    @json_response
    def GetLiveList(self, request, context):
        data = json.loads(request.text)
        user_id = data['user_id']
        live_records = LiveRecord.objects.filter(user_id=user_id)

        count = live_records.count()

        page = int(data.pop('page', 0))
        page_size = int(data.pop('page_size', 0))
        if page:
            live_records = live_records[(page-1)*page_size:page*page_size]

        live_record_list = [live_record.get_info() for live_record in live_records]
        data = dict(status='success', live_record_list=live_record_list,
                count=count)
        return data

    @json_response
    def UpdateLive(self, request, context):
        data = json.loads(request.text)
        record_id = data.pop('live_record_id')
        user_id = data.pop('user_id')
        LiveRecord.objects.filter(id=record_id, user_id=user_id).update(**data)
        data = dict(status='success')
        return data

    @json_response
    def DeleteLive(self, request, context):
        data = json.loads(request.text)
        record_id = data.pop('live_record_id')
        user_id = data.pop('user_id')
        PlayStream.objects.filter(live_record_id=record_id,
                user_id=user_id).delete()
        LiveRecord.objects.filter(id=record_id, user_id=user_id).delete()
        data = dict(status='success')
        return data


class LiveStreamManagement(live_pb2_grpc.LiveStreamManagementServicer):
    @json_response
    def GetLiveStreams(self, request, context):
        data = json.loads(request.text)
        user_id = data.pop('user_id') 
        live_record_id = data.pop('live_record_id', None) 
        if live_record_id:
            play_streams = PlayStream.objects.filter(user_id=user_id,
                    live_record_id=live_record_id)
            play_stream_list = [play_stream.get_info() for play_stream in play_streams]
            data = dict(status='success', play_stream_list=play_stream_list)
            return data
        stream = LiveStream.objects.filter(user_id=user_id).first()
        if stream:
            stream_info = stream.get_info()
            data = dict(status='success', stream_info=stream_info)
        else:
            data = dict(status='fail', msg='未找到流信息')
        return data

    @json_response
    def AddLiveStream(self, request, context):
        data = json.loads(request.text)
        stream = PlayStream.objects.create(**data)
        if stream:
            data = dict(status='success')
        else:
            data = dict(status='fail')
        return data

    @json_response
    def UpdateLiveStream(self, request, context):
        data = json.loads(request.text)
        user_id = data.pop('user_id')
        stream_id = data.pop('play_stream_id')
        stream = PlayStream.objects.filter(id=stream_id, user_id=user_id,
                state=0).update(**data)
        data = dict(status='success')
        return data

    @json_response
    def DeleteLiveStream(self, request, context):
        data = json.loads(request.text)
        stream_id = data.pop('play_stream_id')
        user_id = data.pop('user_id')
        PlayStream.objects.filter(id=stream_id, user_id=user_id, state=0).delete()
        data = dict(status='success')
        return data


class PlayBackManagement(live_pb2_grpc.PlayBackManagementServicer):
    @json_response
    def AddPlayBack(self, request, context):
        data = json.loads(request.text)
        play_back_title = data.pop('play_back_title', None)
        if play_back_title:
            data['live_info'] = play_back_title
        live_record = LivePlayBack.objects.create(**data)
        data = dict(status='success')
        return data

    @json_response
    def GetPlayBackList(self, request, context):
        data = json.loads(request.text)
        user_id = data['user_id']
        live_playbacks = LivePlayBack.objects.filter(user_id=user_id)

        page = int(data.pop('page', 0))
        page_size = int(data.pop('page_size', 0))
        count = live_playbacks.count()

        if page:
            live_playbacks = live_playbacks[(page-1)*page_size:page*page_size]


        live_playback_list = [live_playback.get_info() for live_playback in live_playbacks]
        data = dict(status='success', live_playback_list=live_playback_list,
                count=count)
        return data

    @json_response
    def UpdatePlayBack(self, request, context):
        data = json.loads(request.text)
        play_back_id = data.pop('play_back_id')
        user_id = data.pop('user_id')
        play_back_title = data.pop('play_back_title', None)
        if play_back_title:
            data['live_info'] = play_back_title

        LivePlayBack.objects.filter(id=play_back_id, user_id=user_id).update(**data)
        data = dict(status='success')
        return data

    @json_response
    def DeletePlayBack(self, request, context):
        data = json.loads(request.text)
        play_back_id = data.pop('play_back_id')
        user_id = data.pop('user_id')
        LivePlayBack.objects.filter(id=play_back_id, user_id=user_id).delete()
        data = dict(status='success')
        return data

    @json_response
    def GetNoAddPlayBack(self, request, context):
        data = json.loads(request.text)
        print(data)
        user_id = data['user_id']
        stream = LiveStream.objects.filter(user_id=user_id).first()
        now_play_backs = LivePlayBack.objects.filter(user_id=user_id, media_type=0)
        live_infos = [now_play_back.live_info for now_play_back in now_play_backs]

        play_backs = []

        content = query_historyactivity(stream.name, 0, 0)
        items = content['items']
        for item in items:
            fname = str(item['start'] + item['end']) + '.m3u8'
            play_back_url = get_play_back(stream.name, item['start_time'],
                    item['end_time'], fname=fname)['fname']
            if item['play_back_title'] not in live_infos:
                play_backs.append(dict(play_back_title=item['play_back_title'],
                    media_url=play_back_url))

        data = dict(status='success', play_backs=play_backs)
        return data


