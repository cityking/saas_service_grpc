import grpc
import json
from . import pay_pb2, pay_pb2_grpc

_HOST = 'localhost'
_PORT = '8800'

conn = grpc.insecure_channel(_HOST + ':' + _PORT)

def weixin_order_query(app_id, out_trade_no):
    client = pay_pb2_grpc.WeixinPayStub(channel=conn)
    data = dict(app_id=app_id,
            out_trade_no=out_trade_no)
    text = json.dumps(data)

    response = client.OrderQuery.future(pay_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text) 
    return data 

def ali_order_query(app_id, out_trade_no):
    client = pay_pb2_grpc.AliPayStub(channel=conn)
    data = dict(app_id=app_id,
            out_trade_no=out_trade_no)
    text = json.dumps(data)

    response = client.OrderQuery.future(pay_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text) 
    return data 



def unified_order(app_id, out_trade_no, body, total_fee, product_id, trade_type):
    client = pay_pb2_grpc.WeixinPayStub(channel=conn)
    data = dict(app_id=app_id,
            out_trade_no=out_trade_no,
            body=body,
            total_fee=int(total_fee*100),
            product_id=product_id,
            trade_type=trade_type)
#    data.pop('app_id')
    text = json.dumps(data)
    response = client.UnifiedOrder.future(pay_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def precreate(app_id, out_trade_no, total_amount, subject):
    client = pay_pb2_grpc.AliPayStub(channel=conn)
    data = dict(app_id=app_id,
            out_trade_no=out_trade_no,
            total_amount=total_amount,
            subject=subject,
            )
#    data.pop('app_id')
    text = json.dumps(data)
    response = client.Precreate.future(pay_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data

def ali_app_pay(app_id, out_trade_no, total_amount):
    client = pay_pb2_grpc.AliPayStub(channel=conn)
    data = dict(app_id=app_id,
            out_trade_no=out_trade_no,
            total_amount=total_amount,
            )
    text = json.dumps(data)
    response = client.AppPay.future(pay_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text)
    return data


def tibetancalendar(year, month):
    client = pay_pb2_grpc.TibetanCalendarStub(channel=conn)
    data = dict(year=year,
            month=month)
    text = json.dumps(data)

    response = client.QueryCalendar.future(pay_pb2.json(text=text))
    response = response.result()
    data = json.loads(response.text) 

    return data 




#if __name__ == '__main__':
    #data = weixinpay('wx551718a402287291', '1234567890123')
    #print(data)
