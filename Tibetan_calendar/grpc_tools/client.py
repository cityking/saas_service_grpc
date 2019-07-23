import grpc
import json
#from . import calendar_pb2, calendar_pb2_grpc
import calendar_pb2, calendar_pb2_grpc

_HOST = '123.206.17.178'
_PORT = '50055'

conn = grpc.insecure_channel(_HOST + ':' + _PORT)

def list(year, month):
    client = calendar_pb2_grpc.CalendarServiceStub(channel=conn)
    calendar_req = calendar_pb2.ProtoCalendarReq(year=year,month=month)
    response = client.list.future(calendar_pb2.ProtoCalendarReq(year=year,
        month=month))
    response = response.result()
    return data 


if __name__ == '__main__':
    list(2019, 7)

