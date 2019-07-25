import grpc
import json
import time
from . import calendar_pb2, calendar_pb2_grpc
from . import tibetan_calendar_pb2, tibetan_calendar_pb2_grpc
#import calendar_pb2, calendar_pb2_grpc
import hashlib

_HOST = '123.206.17.178'
_PORT = '50055'

_HOST2 = 'localhost'
_PORT2 = '8800'

conn = grpc.insecure_channel(_HOST + ':' + _PORT)
conn2 = grpc.insecure_channel(_HOST2 + ':' + _PORT2)

def str_md5(string):
    md = hashlib.md5()
    md.update(string.encode())
    res = md.hexdigest()
    return res


def get_calendar_list(year, month):
    client = calendar_pb2_grpc.CalendarServiceStub(channel=conn)
    calendar_req = calendar_pb2.ProtoCalendarReq(year=year,month=month)

    timestamp = str(int(time.time()))
    uid = '0'
    shadow = str_md5(uid+timestamp)
    metadata = [('x-zhibeifw-millis', timestamp),
            ('x-zhibeifw-shadow', shadow),
            ('x-zhibeifw-token', ''),
            ('x-zhibeifw-uid', uid)]

    response = client.list(calendar_req, metadata=metadata)
    result = response.result
    desc = response.desc
    ProtoCalendar_list = response.list

    return ProtoCalendar_list 

def query_calendar(gregorian):
    client = tibetan_calendar_pb2_grpc.TibetanCalendarStub(channel=conn2)
    data = dict(gregorian=gregorian)
    print(data)
    text = json.dumps(data)
    response = client.QueryCalendar(tibetan_calendar_pb2.json(text=text))
    data = json.loads(response.text)

    return data 

def update_day():
    client = tibetan_calendar_pb2_grpc.TibetanCalendarStub(channel=conn2)
    data = dict(gregorian='20190707',
            img='http://fojiao2-10042480.costj.myqcloud.com/data/loacl/zangli/zl149.jpg',
            holiday='药师佛加持日',
            mark = '添加节日'
            )
    print(data)
    text = json.dumps(data)
    response = client.UpdateDay(tibetan_calendar_pb2.json(text=text))
    data = json.loads(response.text)

    return data 


if __name__ == '__main__':
    list(2019, 7)

