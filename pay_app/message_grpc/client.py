import grpc
import json
from . import charge_pb2 as data_pb2, charge_pb2_grpc as data_pb2_grpc

_HOST = 'localhost'
_PORT = '8801'

conn = grpc.insecure_channel(_HOST + ':' + _PORT)

def get_chargeinfo(business_id):
    client = data_pb2_grpc.MessageChargeStub(channel=conn)
    data = dict(business_id=business_id)
    text = json.dumps(data)

    response = client.GetChargeInfo.future(data_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def unified_order(business_id, charge_num, price, pay_type):
    client = data_pb2_grpc.MessageChargeStub(channel=conn)
    data = dict(business_id=business_id,
            charge_num=charge_num,
            price=price,
            pay_type=pay_type)
    text = json.dumps(data)

    response = client.UnifiedOrder.future(data_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def check_order(business_id, order_no):
    client = data_pb2_grpc.MessageChargeStub(channel=conn)
    data = dict(business_id=business_id,
            order_no=order_no)
    print(data)
    text = json.dumps(data)

    response = client.CheckOrder.future(data_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def query_businessinfo(business_id):
    client = data_pb2_grpc.MessageChargeStub(channel=conn)
    data = dict(business_id=business_id)
    text = json.dumps(data)

    response = client.QueryBusinessInfo.future(data_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def query_orderlist(business_id):
    client = data_pb2_grpc.MessageChargeStub(channel=conn)
    data = dict(business_id=business_id)
    print(data)
    text = json.dumps(data)

    response = client.QueryOrderList.future(data_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def add_msg_send_record(biz_id, phone, content):
    client = data_pb2_grpc.MessageChargeStub(channel=conn)
    data = dict(business_id=biz_id, phone=phone, content=content)

    text = json.dumps(data)

    response = client.AddMsgSendRecord.future(data_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

if __name__ == '__main__':
#    data = get_chargeinfo(1)
#    data = check_order(1, '15633887877173738')
    data = unified_order(1, 100, 0.01, 1)
#    data = query_businessinfo(1)
#    data = query_orderlist(1)
    print(data)
