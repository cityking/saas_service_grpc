import os
import sys
import grpc
import time
import json
import django
import datetime
import requests
from concurrent import futures
from Tibetan_calendar.grpc_tools import tibetan_calendar_pb2, tibetan_calendar_pb2_grpc
from Tibetan_calendar.grpc_tools import calendar_pb2, calendar_pb2_grpc, common_info_pb2
from Tibetan_calendar.models import TibetanCalendar as TibetanCalendarModel
from Tibetan_calendar.grpc_tools.client import get_gregorian_range
from redis_tool import RedisConnector

import hashlib
cache_conn = RedisConnector().CacheRedis
def str_md5(string):
    md = hashlib.md5()
    md.update(string.encode())
    res = md.hexdigest()
    return res

def json_response(func):
    def wrapper(view, request, context):
        res_data = func(view, request, context)
        json_data = json.dumps(res_data)
        return tibetan_calendar_pb2.json(text=json_data)
    return wrapper

class TibetanCalendar(tibetan_calendar_pb2_grpc.TibetanCalendarServicer):
    @json_response
    def QueryCalendar(self, request, context):
        print('start QueryCalendar')
        data = json.loads(request.text)
        gregorian = data['gregorian']
        calendar = TibetanCalendarModel.get_date(gregorian)
        if not calendar:
            data = dict(status='fail')
        else:
            data = dict(status='success', calendar=calendar)
        return data

    @json_response
    def UpdateDay(self, request, context):
        print('start UpdateDay')
        data = json.loads(request.text)
        gregorian = data.pop('gregorian')
        TibetanCalendarModel.objects.filter(gregorian=gregorian).update(**data)
        return dict(status='success')

class Calendar(calendar_pb2_grpc.CalendarServiceServicer):
    def list(self, request, context):
        print('Calendar/list')
        year = request.year
        month = request.month
        calendars = TibetanCalendarModel.objects.filter(year=year, month=month)
        if not calendars:
            TibetanCalendarModel.add_calendar(year, month)
            calendars = TibetanCalendarModel.objects.filter(year=year, month=month)

        resp = calendar_pb2.ProtoCalendarListResp(result=1)
        for calendar in calendars:
            proto_calendar = resp.list.add()
            proto_calendar.gregorian = int(calendar.gregorian)
            proto_calendar.chinese = int(calendar.chinese)
            proto_calendar.tibetan = int(calendar.tibetan)
            proto_calendar.holiday = calendar.holiday
            proto_calendar.img = calendar.img
        return resp
    def getGregorianRange(self, request, context):
        resp = get_gregorian_range()
        return resp




