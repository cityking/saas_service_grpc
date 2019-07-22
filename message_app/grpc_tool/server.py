import os
import sys
import grpc
import time
import json
import django
import datetime
import requests
from concurrent import futures
sys.path.append('/new_dev/test_workspace/saas_service')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_servcie.settings')
django.setup()

from message_app.grpc_tool import charge_pb2 as data_pb2,charge_pb2_grpc as data_pb2_grpc
from message_app.models import Business, MsgRecord, ChargePackage, Order, PayInfo
from redis_tool import RedisConnector

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '0.0.0.0'
_PORT = '8801'

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
        return data_pb2.json(text=json_data)
    return wrapper


class MessageCharge(data_pb2_grpc.MessageChargeServicer):
    @json_response
    def GetChargeInfo(self, request, context):
        data = json.loads(request.text)
        business_id = data['business_id']
        pakages = ChargePackage.objects.all()
        pakages = [pakage.get_info() for pakage in pakages]
        pay_infos = PayInfo.objects.filter(business_id=business_id)
        pay_types = [{pay_info.pay_type:pay_info.get_pay_type()} for pay_info in pay_infos]
        data = dict(status='success', pakages=pakages, pay_types=pay_types)
        return data

    @json_response
    def UnifiedOrder(self, request, context):
        print('start UnifiedOrder')
        print(request.text)
        data = json.loads(request.text)
        package = ChargePackage.objects.filter(charge_num=data['charge_num'],
                price=data['price']).first()
        if not package:
            return dict(status='fail', msg='未找到充值套餐')
        else:
            order_no = Order.get_order_no()
            data['order_no'] = order_no
            order = Order.objects.create(**data)
            pay_code = order.pay_order()
            if pay_code:
                return dict(status='success', pay_code=pay_code,
                        order_no=order.order_no)
            else:
                return dict(status='fail', msg='支付信息获取失败, 请重试')

    @json_response
    def CheckOrder(self, request, context):
        data = json.loads(request.text)
        order_no = data['order_no']
        business_id = data['business_id']
        order = Order.objects.filter(order_no=order_no, business_id=business_id).first()
        if not order:
            return dict(status='fail', msg='订单不存在')
        else:
            if order.state==1:
                return dict(status='success', state=1)
            else:
                pay_success = order.query_pay_state()
                if pay_success:
                    order.state = 1
                    order.save()
                    business = order.business
                    business.msg_num += order.charge_num
                    business.save()
                    return dict(status='success', state=1)
                else:
                    return dict(status='success', state=0)

    @json_response
    def QueryBusinessInfo(self, request, context):
        print('start QueryBusinessInfo')
        print(request.text)
        data = json.loads(request.text)
        if 'business_id' in data:
            business_id = data['business_id']
            business = Business.objects.filter(id=business_id).first()
        elif 'business_name' in data:
            business = Business.objects.filter(name=data['business_name']).first()
        else:
            return dict(status='fail', msg='商户不存在')
        if business:
            return dict(status='success', business_info=business.get_info())
        else:
            return dict(status='fail', msg='商户不存在')

    @json_response
    def QueryOrderList(self, request, context):
        print('start QueryOrderList')
        data = json.loads(request.text)
        orders = Order.objects.filter(business_id=data['business_id'],state=1).order_by('-create_time')
        count = orders.count()
        if 'page' in data:
            page = data['page']
            page_size = data['page_size']
            start = (page-1) * page_size
            end = page * page_size
            orders = orders[start:end]

        order_list = [order.get_info() for order in orders]
        return dict(status='success', order_list=order_list, count=count)

    @json_response
    def AddMsgSendRecord(self, request, context):
        print('start AddMsgSendRecord')
        data = json.loads(request.text)
        business_id = data['business_id']
        business = Business.objects.get(id=business_id)
        business.msg_num -= 1
        business.save()
        MsgRecord.objects.create(**data)
        return dict(status='success')

def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))   # 创建一个服务器
    # 在服务器中添加派生的接口服务（自己实现了处理函数）
    data_pb2_grpc.add_MessageChargeServicer_to_server(MessageCharge(), grpcServer)

    grpcServer.add_insecure_port(_HOST + ':' + _PORT)    # 添加监听端口
    grpcServer.start()    #  启动服务器
    print('服务启动')
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0) # 关闭服务器

if __name__ == '__main__':
    serve()
