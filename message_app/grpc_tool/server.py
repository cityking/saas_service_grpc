import os
import sys
import grpc
import time
import json
import django
import datetime
import requests
from concurrent import futures
from message_app.grpc_tool import charge_pb2 as data_pb2,charge_pb2_grpc as data_pb2_grpc
from message_app.models import Business, MsgRecord, ChargePackage, Order, PayInfo
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

