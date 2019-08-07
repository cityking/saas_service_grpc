import grpc
import json
from . import live_pb2, live_pb2_grpc
from . import live_longensi_pb2, live_longensi_pb2_grpc
from . import live_collect_pb2, live_collect_pb2_grpc
from live_app.models import LiveStream

#_HOST = 'localhost'
#_PORT = '8800'

_HOST = '120.77.237.231'
_PORT = '9274'
conn = grpc.insecure_channel(_HOST + ':' + _PORT)

def add_live():
    stream = LiveStream.objects.filter(user_id=1).first()
    info = stream.get_info()

    data = dict(user_id=1,
            title='我的直播',
            speaker='cityking',
            image_url='http://jjjjj',
            details='hhjjjjdksjjss',
            start_time='2019-07-20 08:00:00',
            last_time=120,
            pull_stream_url=info['pull_stream_url'],
            play_streams=info['play_streams']
            )

    print(data)

    client = live_pb2_grpc.LiveManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.AddLive.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def add_play_back(data):
    print(data)
    client = live_pb2_grpc.PlayBackManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.AddPlayBack.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data


def get_live_list(user_id):
    data = dict(user_id=user_id)
    print(data)
    client = live_pb2_grpc.LiveManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.GetLiveList.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def get_no_add_play_back(user_id):
    data = dict(user_id=user_id)
    print(data)
    client = live_pb2_grpc.PlayBackManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.GetNoAddPlayBack.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def get_play_back_list(user_id):
    data = dict(user_id=user_id)
    print(data)
    client = live_pb2_grpc.PlayBackManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.GetPlayBackList.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def add_stream():
    data = dict(user_id=1,
            live_record_id=5,
            stream_name='youtube',
            live_type='video',
            stream_url='http://jjkkkll')
    print(data)
    client = live_pb2_grpc.LiveStreamManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.AddLiveStream.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def get_streams(user_id, live_record_id=None):
    if live_record_id:
        data = dict(user_id=user_id, live_record_id=live_record_id)
    else:
        data = dict(user_id=user_id)
    print(data)
    client = live_pb2_grpc.LiveStreamManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.GetLiveStreams.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def update_stream():
    data = dict(user_id=1,
            play_stream_id=4,
            live_record_id=5,
            stream_name='youtube',
            live_type='mp4',
            stream_url='http://jjkkkll')

    print(data)
    client = live_pb2_grpc.LiveStreamManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.UpdateLiveStream.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def delete_stream():
    data = dict(user_id=1,
            play_stream_id=4,
            )

    print(data)
    client = live_pb2_grpc.LiveStreamManagementStub(channel=conn)
    text = json.dumps(data)

    response = client.DeleteLiveStream.future(live_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def get_latest_live(user_id):
    client = live_longensi_pb2_grpc.LiveFrontStub(channel=conn)

    response = client.GetLatestLive.future(live_longensi_pb2.LiveReq(user_id=user_id))
    response = response.result()
    return response

def get_live_time(user_id):
    client = live_longensi_pb2_grpc.LiveFrontStub(channel=conn)

    response = client.GetLiveStartTime.future(live_longensi_pb2.LiveReq(user_id=user_id))
    response = response.result()
    return response

def get_play_back(user_id, page, page_size):
    client = live_longensi_pb2_grpc.LiveFrontStub(channel=conn)
    play_back_req = live_longensi_pb2.PlayBackReq(user_id=user_id,
            page=page,
            page_size=page_size)
    response = client.GetPlayBackList.future(play_back_req)
    response = response.result()
    return response

def get_play_back_collected(user_id, page, page_size):
    client = live_collect_pb2_grpc.PlayBackCollectStub(channel=conn)
    play_back_req = live_longensi_pb2.PlayBackReq(user_id=user_id,
            page=page,
            page_size=page_size)
    response = client.GetCollectedList.future(play_back_req)
    response = response.result()
    return response

def play_back_collect(user_id, play_back_id, method):
    client = live_collect_pb2_grpc.PlayBackCollectStub(channel=conn)
    play_back_req = live_collect_pb2.PlayBackColletReq(user_id=user_id,
            play_back_id=play_back_id,
            method=method)
    response = client.Collect.future(play_back_req)
    response = response.result()
    return response


def add_play_record(user_id, play_back_id):
    client = live_longensi_pb2_grpc.LiveFrontStub(channel=conn)
    play_back_req = live_longensi_pb2.PlayRecordReq(user_id=user_id,
            play_back_id=play_back_id)
    response = client.AddPlayRecord.future(play_back_req)
    response = response.result()
    return response

def get_single_play_back(user_id, play_back_id):
    client = live_longensi_pb2_grpc.LiveFrontStub(channel=conn)
    play_back_req = live_longensi_pb2.PlayRecordReq(user_id=user_id,
            play_back_id=play_back_id)
    response = client.GetSinglePlayBack.future(play_back_req)
    response = response.result()
    return response

if __name__ == '__main__':
    data = dict(user_id=1,
            title='我的直播',
            speaker='cityking',
            image_url='http://jjjjj',
            details='hhjjjjdksjjss',
            media_type=0,
            live_info='直播回放(201907180200)',
            media_url='http://pili-vod.realtime-live.iruyue.tv/3126834719.m3u8')

    #data = add_play_back(data)
    #data = add_live(data)
    #data = get_live_list(1)
    #data = get_no_add_play_back(1)
    #data = add_stream(1, 'livestream', '本地')
    #data = get_streams(1)
    #data = update_stream(1, 1, '本地', 0)
    #data = get_play_back_list(1)
    print(data)
