from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from django.utils.encoding import escape_uri_path
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from pay_app.models import WeixinPay
import datetime
import random
import os

def json_rsp(content=None,msg=None):
    data = dict(status=200, content=content, msg=msg)
    return JsonResponse(data)

def err_rsp(content=None,msg=None):
    data = dict(status=400, content=content, msg=msg)
    return JsonResponse(data)

def weixinpay(func):
    """微信支付"""
    def wrapper(view, *args, **kwargs):
        req = view.request
        data = req.data
        app_id = data.pop('app_id')
        if app_id:
            pay = WeixinPay.objects.filter(app_id=app_id).first()
            if not pay:
                return err_rsp(msg='支付信息未登记')
        else:
            return err_rsp(msg='缺少app_id')

        req.pay = pay
        return func(view, *args, **kwargs)
    return wrapper


class WeixinOrderView(View):
    @weixinpay
    def post(self, req):
        pay = req.pay
        data = req.data
        res = pay.unified_order(data)
        return json_rsp(content=res)
    @weixinpay
    def get(self, req):
        data = req.data
        pay = req.pay
        res = pay.order_query(data)
        return json_rsp(content=res)

    @weixinpay
    def delete(self, req):
        data = req.data
        pay = req.pay
        res = pay.close_order(data)
        return json_rsp(content=res)

class WeixinRefundView(View):
    @weixinpay
    def post(self, req):
        pay = req.pay
        data = req.data
        res = pay.refund(data)
        return json_rsp(content=res)

    @weixinpay
    def get(self, req):
        data = req.data
        pay = req.pay
        res = pay.refund_query(data)
        return json_rsp(content=res)

class WeixinMicropayView(View):
    @weixinpay
    def post(self, req):
        pay = req.pay
        data = req.data
        res = pay.micropay(data)
        return json_rsp(content=res)
    @weixinpay
    def get(self, req):
        data = req.data
        pay = req.pay
        res = pay.refund_query(data)
        return json_rsp(content=res)

class PayCallbackView(View):
    def post(self, req):
        import pdb;pdb.set_trace()
    def get(self, req):
        import pdb;pdb.set_trace()


