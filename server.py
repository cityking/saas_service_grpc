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

from grpc_tool import pay_pb2, pay_pb2_grpc
from message_app.grpc_tool import charge_pb2, charge_pb2_grpc
from live_app.grpc_tool import live_pb2, live_pb2_grpc

#from tools import tools_pb2, tools_pb2_grpc
#from tools.handler import ToolsHandler
from redis_tool import RedisConnector
from pay_app.models import WeixinPay as WeixinPayM, AliPay as AliPayM
from message_app.grpc_tool import server as message_server
from live_app.grpc_tool import server as live_server


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




class TibetanCalendar(pay_pb2_grpc.TibetanCalendarServicer):
    def QueryCalendar(self, request, context):
        start = datetime.datetime.now()
        data = json.loads(request.text)
        year = data['year']
        month = data['month']

        if month.startswith('0'):
            l_key = year + month[-1]
        else:
            l_key = year + month

        key = 'TibetanCalendar'

#        if cache_conn.hexists(key, l_key):
#            res = cache_conn.hget(key, l_key).decode()
#        else:
        if True:
            checkValue = str_md5(year+month).upper()
            url = 'http://site.zhibeili.com/index.php?g=app&m=Zangli&a=index'
            data = dict(checkValue=checkValue,
                data=request.text)
            res = requests.post(url, data=data).text
            cache_conn.hset(key, l_key, res)

        end = datetime.datetime.now()
        print(end-start)

        return pay_pb2.json(text=res)  # 返回一个类实例

def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))   # 创建一个服务器

    # 在服务器中添加派生的接口服务（自己实现了处理函数）
    pay_pb2_grpc.add_WeixinPayServicer_to_server(WeixinPay(), grpcServer)
    pay_pb2_grpc.add_AliPayServicer_to_server(AliPay(), grpcServer)
    pay_pb2_grpc.add_TibetanCalendarServicer_to_server(TibetanCalendar(), grpcServer)

    charge_pb2_grpc.add_MessageChargeServicer_to_server(message_server.MessageCharge(),
            grpcServer)

    live_pb2_grpc.add_LiveManagementServicer_to_server(live_server.LiveManagement(), grpcServer)
    live_pb2_grpc.add_LiveStreamManagementServicer_to_server(live_server.LiveStreamManagement(), grpcServer)
    live_pb2_grpc.add_PlayBackManagementServicer_to_server(live_server.PlayBackManagement(), grpcServer)

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
