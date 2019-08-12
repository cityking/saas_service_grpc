import os
import grpc
import time
import json
import django
import datetime
import requests
from concurrent import futures
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_servcie.settings')
django.setup()

from grpc_tool import pay_pb2, pay_pb2_grpc, paypal_pb2, paypal_pb2_grpc
from message_app.grpc_tool import charge_pb2, charge_pb2_grpc
from live_app.grpc_tool import live_pb2, live_pb2_grpc
from live_app.grpc_tool import live_longensi_pb2, live_longensi_pb2_grpc
from live_app.grpc_tool import live_collect_pb2, live_collect_pb2_grpc

from Tibetan_calendar.grpc_tools import tibetan_calendar_pb2, tibetan_calendar_pb2_grpc
from Tibetan_calendar.grpc_tools import calendar_pb2, calendar_pb2_grpc

#from tools import tools_pb2, tools_pb2_grpc
#from tools.handler import ToolsHandler
from redis_tool import RedisConnector
from pay_app.models import WeixinPay as WeixinPayM, AliPay as AliPayM, PayPalPay
from message_app.grpc_tool import server as message_server
from live_app.grpc_tool import server as live_server
from Tibetan_calendar.grpc_tools import server as tibetan_calendar_server


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

def pre_request_weixin_pay(func):
    """微信支付"""
    def wrapper(view, request, context):
        data = json.loads(request.text)
        app_id = data.pop('app_id', None)
        if not app_id:
            return_code = 'FAIL'
            return_msg = '缺少参数app_id'
            data = dict(return_code=return_code,
                    return_msg=return_msg)
            data = json.dumps(data)
            return pay_pb2.json(text=data)
        pay = WeixinPayM.objects.filter(app_id=app_id).first()


        if not pay:
            return err_rsp(msg='支付信息未登记')

        context.pay = pay
        context.data = data
        return func(view, request, context)
    return wrapper
def err_rsp(msg=None):
    return_code = 'FAIL'
    return_msg = msg
    data = dict(return_code=return_code,
            return_msg=return_msg)
    data = json.dumps(data)
    return pay_pb2.json(text=data)
def pre_request_ali_pay(func):
    """微信支付"""
    def wrapper(view, request, context):
        data = json.loads(request.text)
        app_id = data.pop('app_id', None)
        if not app_id:
            return_code = 'FAIL'
            return_msg = '缺少参数app_id'
            data = dict(return_code=return_code,
                    return_msg=return_msg)
            data = json.dumps(data)
            return pay_pb2.json(text=data)
        pay = AliPayM.objects.filter(app_id=app_id).first()


        if not pay:
            return err_rsp(msg='支付信息未登记')

        context.pay = pay
        context.data = data
        return func(view, request, context)
    return wrapper

def pre_request_paypal_pay(func):
    """paypal支付"""
    def wrapper(view, request, context):
        client_id = request.client_id
        if not client_id:
            rsp = paypal_pb2.PaymentCreateRsp()
            rsp.status = 400
            rsp.msg = '缺少参数client_id'
            return rsp
        pay = PayPalPay.objects.filter(client_id=client_id).first()


        if not pay:
            return paypal_pb2.PaymentCreateRsp(status = 400, msg='支付信息未登记')

        context.pay = pay
        return func(view, request, context)
    return wrapper



class WeixinPay(pay_pb2_grpc.WeixinPayServicer):
    @pre_request_weixin_pay
    def OrderQuery(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.order_query(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_weixin_pay
    def UnifiedOrder(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.unified_order(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_weixin_pay
    def CloseOrder(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.close_order(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_weixin_pay
    def Refund(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.refund(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_weixin_pay
    def RefundQuery(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.refund_query(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_weixin_pay
    def Micropay(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.micropay(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

class AliPay(pay_pb2_grpc.AliPayServicer):
    @pre_request_ali_pay
    def Precreate(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.precreate(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_ali_pay
    def OrderQuery(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.order_query(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

    @pre_request_ali_pay
    def AppPay(self, request, context):
        pay = context.pay
        data = context.data
        res = pay.app_pay(data)
        res_data = json.dumps(res)
        return pay_pb2.json(text=res_data)

class PaypalPay(paypal_pb2_grpc.PaypalPayServicer):
    @pre_request_paypal_pay
    def PaymentCreate(self, request, context):
        pay = context.pay
        items = request.items
        items = [dict(name=item.name,
            sku=item.sku,
            price=item.price,
            currency='USD',
            quantity=item.quantity) for item in items]
        print(items)
        payment, approval_url = pay.create_payment(items, request.total, request.description)
        if payment:
            return paypal_pb2.PaymentCreateRsp(status=200,
                    paymentId=payment.id,
                    approval_url=approval_url)
        else:
            return paypal_pb2.PaymentCreateRsp(status=400, msg='支付订单创建失败')

    @pre_request_paypal_pay
    def PaymentExecute(self, request, context):
        pay = context.pay

        res, payment, approval_url = pay.payment_excute(request.paymentId, request.PayerID)
        if res:
            return paypal_pb2.PaymentExecuteRsp(status=200,
                    paymentId=payment.id,
                    approval_url=approval_url,
                    result='success')
        else:
            return paypal_pb2.PaymentExecuteRsp(status=400, msg='支付失败')



def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))   # 创建一个服务器

    # 在服务器中添加派生的接口服务（自己实现了处理函数）
    pay_pb2_grpc.add_WeixinPayServicer_to_server(WeixinPay(), grpcServer)
    pay_pb2_grpc.add_AliPayServicer_to_server(AliPay(), grpcServer)

    paypal_pb2_grpc.add_PaypalPayServicer_to_server(PaypalPay(), grpcServer)
    #pay_pb2_grpc.add_TibetanCalendarServicer_to_server(TibetanCalendar(), grpcServer)

    charge_pb2_grpc.add_MessageChargeServicer_to_server(message_server.MessageCharge(),
            grpcServer)

    live_pb2_grpc.add_LiveManagementServicer_to_server(live_server.LiveManagement(), grpcServer)
    live_pb2_grpc.add_LiveStreamManagementServicer_to_server(live_server.LiveStreamManagement(), grpcServer)
    live_pb2_grpc.add_PlayBackManagementServicer_to_server(live_server.PlayBackManagement(), grpcServer)
    live_longensi_pb2_grpc.add_LiveFrontServicer_to_server(live_server.LiveFront(), grpcServer)
    live_collect_pb2_grpc.add_PlayBackCollectServicer_to_server(live_server.PlayBackCollect(), grpcServer)

    tibetan_calendar_pb2_grpc.add_TibetanCalendarServicer_to_server(tibetan_calendar_server.TibetanCalendar(), grpcServer)
    calendar_pb2_grpc.add_CalendarServiceServicer_to_server(tibetan_calendar_server.Calendar(), grpcServer)

    #短信服务等
    #tools_pb2_grpc.add_ToolsServerServicer_to_server(ToolsHandler(), grpcServer)

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
