import grpc
import json
from . import server_pb2, server_pb2_grpc
from . import article_pb2, article_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp

_HOST = '120.77.237.231'
_PORT = '7703'
conn = grpc.insecure_channel(_HOST + ':' + _PORT)

def savemetadata(play_back):
    timestamp = Timestamp()
    timestamp.FromDatetime(play_back.create_time)
    metadata = article_pb2.MetaData(obj_type=3,
            obj_id=play_back.id,
            desc=play_back.details,
            is_vipuser=True if play_back.is_vip else False,
            title=play_back.title,
            detail=play_back.title,
            create_time=timestamp)
    client = server_pb2_grpc.TempleServerStub(channel=conn)

    response = client.MetaDataSave.future(metadata)
    response = response.result()
    return response

def deletemetadata(play_back):
    timestamp = Timestamp()
    timestamp.FromDatetime(play_back.create_time)
    metadata = article_pb2.MetaData(obj_type=3,
            obj_id=play_back.id,
            desc=play_back.details,
            is_vipuser=True if play_back.is_vip else False,
            title=play_back.title,
            detail=play_back.title,
            create_time=timestamp)
    client = server_pb2_grpc.TempleServerStub(channel=conn)

    response = client.MetaDataDelete.future(metadata)
    response = response.result()
    return response


