# 标准库
import time
import string
import random
import hashlib
from xml.etree import ElementTree as etree
import datetime
import json
import urllib.parse
import rsa
import base64
import requests

# 三方库
import requests

from django.db import models

FAIL = "FAIL"
SUCCESS = "SUCCESS"

class WeixinPayError(Exception):
    def __init__(self, msg):
        super(WeixinPayError, self).__init__(msg)

def xml_to_dict(content):
        raw = {}
        root = etree.fromstring(content)
        for child in root:
            raw[child.tag] = child.text
        return raw

class Map(dict):
    """
    提供字典的dot访问模式
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    m.first_name='Eduardo'
    """

    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    if isinstance(v, dict):
                        v = Map(v)
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, dict):
                    v = Map(v)
                self[k] = v

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __getitem__(self, key):
        if key not in self.__dict__:
            super(Map, self).__setitem__(key, {})
            self.__dict__.update({key: Map()})
        return self.__dict__[key]

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

def cert_path(instance, filename):
    return "uploads/cert/%s_cert.pem" % instance.app_id

def key_path(instance, filename):
    return "uploads/cert_key/%s_key.pem" % instance.app_id

# Create your models here.
class WeixinPay(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    app_id = models.CharField(max_length=20)
    mch_id = models.CharField(max_length=20)
    mch_key = models.CharField(max_length=50)
    notify_url = models.CharField(max_length=100, null=True,blank=True,
            verbose_name='回调链接')
    cert_key = models.FileField('证书key', null=True, blank=True,
            upload_to=key_path)
    cert = models.FileField('证书', null=True, blank=True, upload_to=cert_path)

    def __str__(self):
        return self.name

    @property
    def sess(self):
        return requests.Session()

    @property
    def nonce_str(self):
        char = string.ascii_letters + string.digits
        return "".join(random.choice(char) for _ in range(32))

    def sign(self, raw):
        raw = [(k, str(raw[k]) if isinstance(raw[k], int) else raw[k])
               for k in sorted(raw.keys())]
        s = "&".join("=".join(kv) for kv in raw if kv[1])
        s += "&key={0}".format(self.mch_key)
        return hashlib.md5(s.encode("utf-8")).hexdigest().upper()

    def check_sign(self, data):
        sign = data.pop("sign")
        return sign == self.sign(data)

    def to_xml(self, raw):
        s = ""
        for k, v in raw.items():
            s += "<{0}>{1}</{0}>".format(k, v)
        s = "<xml>{0}</xml>".format(s)
        return s.encode("utf-8")

    def to_dict(self, content):
        raw = {}
        root = etree.fromstring(content)
        for child in root:
            raw[child.tag] = child.text
        return raw

    def _fetch(self, url, data, use_cert=False):
        data.setdefault("appid", self.app_id)
        data.setdefault("mch_id", self.mch_id)
        data.setdefault("nonce_str", self.nonce_str)
        data.setdefault("sign", self.sign(data))

        if use_cert:
            resp = self.sess.post(url, data=self.to_xml(data),
                    cert=(self.cert.url, self.cert_key.url))
        else:
            resp = self.sess.post(url, data=self.to_xml(data))
        content = resp.content.decode("utf-8")
        if "return_code" in content:
            data = Map(self.to_dict(content))
            if data.return_code == FAIL:
                raise WeixinPayError(data.return_msg)
            if "result_code" in content and data.result_code == FAIL:
                raise WeixinPayError(data.err_code_des)
            return data
        return content

    def reply(self, msg, ok=True):
        code = SUCCESS if ok else FAIL
        return self.to_xml(dict(return_code=code, return_msg=msg))

    def unified_order(self, data):
        """
        统一下单
        out_trade_no、body、total_fee、trade_type必填
        app_id, mchid, nonce_str自动填写
        """
        url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
        # 关联参数
        if data["trade_type"] == "JSAPI" and "openid" not in data:
            raise WeixinPayError("trade_type为JSAPI时，openid为必填参数")
        if data["trade_type"] == "NATIVE" and "product_id" not in data:
            raise WeixinPayError("trade_type为NATIVE时，product_id为必填参数")
        data.setdefault("notify_url", self.notify_url)
        print(data)

        raw = self._fetch(url, data)
        return raw

    def app_pay(self, data):
        """
        统一下单
        out_trade_no、body、total_fee必填
        app_id, mchid, nonce_str自动填写
        """
        data['trade_type'] = 'APP'
        raw = self.unified_order(data)
        print(raw)
        
    def micropay(self, data):
        """
        提交付款码支付
        body 店名-销售商品类目
        out_trade_no
        total_fee
        spbill_create_ip
        auth_code
        app_id, mchid, nonce_str自动填写
        """

        url = "https://api.mch.weixin.qq.com/pay/micropay"
        raw = self._fetch(url, data)
        return raw


    def jsapi(self, **kwargs):
        """
        生成给JavaScript调用的数据
        详细规则参考 https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=7_7&index=6
        """
        kwargs.setdefault("trade_type", "JSAPI")
        raw = self.unified_order(**kwargs)
        package = "prepay_id={0}".format(raw["prepay_id"])
        timestamp = str(int(time.time()))
        nonce_str = self.nonce_str
        raw = dict(appId=self.app_id, timeStamp=timestamp,
                   nonceStr=nonce_str, package=package, signType="MD5")
        sign = self.sign(raw)
        return dict(package=package, appId=self.app_id,
                    timeStamp=timestamp, nonceStr=nonce_str, sign=sign)

    def order_query(self, data):
        """
        订单查询
        out_trade_no, transaction_id至少填一个
        appid, mchid, nonce_str不需要填入
        """
        url = "https://api.mch.weixin.qq.com/pay/orderquery"
        return self._fetch(url, data)


    def close_order(self, data):
        """
        撤销订单
        out_trade_no必填
        appid, mchid, nonce_str不需要填入
        """
        url = "https://api.mch.weixin.qq.com/pay/closeorder"
        return self._fetch(url, data)

    def refund(self, data):
        """
        申请退款
        out_trade_no、transaction_id至少填一个且
        out_refund_no、total_fee、refund_fee、op_user_id为必填参数
        appid、mchid、nonce_str不需要填入
        """
        if not self.cert_key or not self.cert:
            raise WeixinPayError("退款申请接口需要双向证书")
        url = "https://api.mch.weixin.qq.com/secapi/pay/refund"
        return self._fetch(url, data, True)

    def refund_query(self, data):
        """
        查询退款
        提交退款申请后，通过调用该接口查询退款状态。退款有一定延时，
        用零钱支付的退款20分钟内到账，银行卡支付的退款3个工作日后重新查询退款状态。
        out_refund_no、out_trade_no、transaction_id、refund_id四个参数必填一个
        appid、mchid、nonce_str不需要填入
        """
        url = "https://api.mch.weixin.qq.com/pay/refundquery"
        return self._fetch(url, data)

    def download_bill(self, bill_date, bill_type="ALL", **data):
        """
        下载对账单
        bill_date、bill_type为必填参数
        appid、mchid、nonce_str不需要填入
        """
        url = "https://api.mch.weixin.qq.com/pay/downloadbill"
        data.setdefault("bill_date", bill_date)
        data.setdefault("bill_type", bill_type)

        if "bill_date" not in data:
            raise WeixinPayError("对账单接口中，缺少必填参数bill_date")

        return self._fetch(url, data)

    class Meta:
        verbose_name = "微信支付"
        verbose_name_plural = verbose_name
        db_table = 'weixin_pay'

class AliPay(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    app_id = models.CharField(max_length=20)
    notify_url = models.CharField(max_length=100, null=True,blank=True,
            verbose_name='回调链接')
    ali_pub_key = models.TextField('证书ali_pub_key', null=True, blank=True)
    app_pri_key = models.TextField('证书app_pri_key', null=True, blank=True)
    app_pub_key = models.TextField('证书app_pub_key', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def conf(self):
        return dict(app_id=self.app_id,
                charset='utf-8',
                sign_type='RSA2',
                version='1.0',
                notify_url=self.notify_url)

    @property
    def refund_url(self):
        return 'https://openapi.alipay.com/gateway.do'
    class Meta:
        verbose_name = "支付宝支付"
        verbose_name_plural = verbose_name
        db_table = 'ali_pay'

    def RAS_sign(self, string):
        """传入字符串:需encode():"""
        private_key = rsa.PrivateKey.load_pkcs1(self.app_pri_key)
#        private_key = self.app_pri_key

        sign = rsa.sign(string.encode(), private_key, 'SHA-256')
        return base64.b64encode(sign).decode('utf-8')

    @staticmethod
    def nonce_str():
        char = string.ascii_letters + string.digits
        return "".join(random.choice(char) for _ in range(32))

    def dict_sort(self, raw):
        """字典排序"""
        raw = [(k, str(raw[k]) if isinstance(raw[k], int) else raw[k])
               for k in sorted(raw.keys())]
        s = "&".join("=".join(kv) for kv in raw if kv[1])
        return s

    def get_sign(self, dict_object):
        return self.RAS_sign(self.dict_sort(dict_object))

    def face_pay(self, dict_object):
        """
        :param dict_object:
                    out_trade_no 订单号
                    auth_code 付款码
                    total_amount 金额
                    subject 订单标题
        :return: dict
        """
        # 业务参数
        dict_object['product_code'] = 'FACE_TO_FACE_PAYMENT'
        dict_object['scene'] = 'bar_code'
        data = self.conf
        # 添加公共参数
        data['method'] = 'alipay.trade.pay'
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['biz_content'] = json.dumps(dict_object)
        # 拼接
        sign_string = self.dict_sort(data)
        # 签名
        sign = self.RAS_sign(sign_string)
        # 对所有一级参数 url_encode
        for k, v in data.items():
            data[k] = urllib.parse.quote(v)
        data = self.dict_sort(data) + '&sign=' + urllib.parse.quote(sign)

        res = requests.get(url=self.refund_url, params=data).json()
        return res
        # import pdb;pdb.set_trace()
        # 把 sign url_encode 加在排序的后面
        # return self.dict_sort(data) + '&sign=' + urllib.parse.quote(sign)
    def precreate(self, dict_object):
        """
        :param dict_object:
                    out_trade_no
                    total_amount
                    subject
        :return: dict
        """
        # 业务参数
        data = self.conf
        # 添加公共参数
        data['method'] = 'alipay.trade.precreate'
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['biz_content'] = json.dumps(dict_object)
        # 拼接
        sign_string = self.dict_sort(data)
        # 签名
        sign = self.RAS_sign(sign_string)
        # 对所有一级参数 url_encode
        for k, v in data.items():
            data[k] = urllib.parse.quote(v)
        # 把 sign url_encode 加在排序的后面
        data = self.dict_sort(data) + '&sign=' + urllib.parse.quote(sign)
        res = requests.get(url=self.refund_url, params=data).json()
        return res


    def app_pay(self, dict_object):
        """
        :param dict_object:
                    out_trade_no
                    total_amount
        :return: dict
        """
        # 业务参数
        dict_object['product_code'] = 'QUICK_MSECURITY_PAY'
        #dict_object['subject'] = '电子签名vip升级'
        # dict_object['timeout_express'] = '30m'
        # dict_object['seller_id'] = 'tdjshun@126.com'
        #dict_object['seller_id'] = 'zhangyufeng@jetcloudtech.com'
        data = self.conf
        # 添加公共参数
        data['method'] = 'alipay.trade.app.pay'
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['biz_content'] = json.dumps(dict_object)
        # 拼接
        sign_string = self.dict_sort(data)
        # 签名
        sign = self.RAS_sign(sign_string)
        # 对所有一级参数 url_encode
        for k, v in data.items():
            data[k] = urllib.parse.quote(v)
        # 把 sign url_encode 加在排序的后面
        return self.dict_sort(data) + '&sign=' + urllib.parse.quote(sign)

    def order_query(self, dict_object):
        """
        :param dict_object:
                    out_trade_no
        :return: dict
        """

        data = self.conf
        # 添加公共参数
        data['method'] = 'alipay.trade.query'
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['biz_content'] = json.dumps(dict_object)
        # 拼接
        sign_string = self.dict_sort(data)
        # 签名
        sign = self.RAS_sign(sign_string)
        # 对所有一级参数 url_encode
        for k, v in data.items():
            data[k] = urllib.parse.quote(v)
        # 把 sign url_encode 加在排序的后面
        data = self.dict_sort(data) + '&sign=' + urllib.parse.quote(sign)
        res = requests.get(url=self.refund_url, params=data).json()
        return res

    def refund(self, unit_no, refund_amount):
        out_request_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + \
                         str(time.time()).replace('.', '')[-4:]
        dict_object = {
            'out_trade_no': unit_no,
            'refund_amount': str(refund_amount),
            'out_request_no': out_request_no,  # 分次退款订单号
        }
        # 添加公共参数
        data = self.conf
        data['method'] = 'alipay.trade.refund'
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['biz_content'] = json.dumps(dict_object)
        # 拼接
        sign_string = self.dict_sort(data)
        # 签名
        data['sign'] = self.RAS_sign(sign_string)
        r = requests.get(url=self.refund_url, params=data).json()
        print('退款回调', r)
        return r['alipay_trade_refund_response'], out_request_no

    # 验证签名
    def verify_sign(self, dict_object):
        if not len(dict_object) > 0:
            return False
        sign_type = dict_object.pop('sign_type')
        sign = dict_object.pop('sign')
        sign_string = self.dict_sort(dict_object)

        if sign_type.upper() == "RSA2":
            try:
                pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(self.ali_pub_key)
                base_sign = base64.b64decode(sign)
                if rsa.verify(sign_string.encode(), base_sign, pubkey):
                    print("----------verify sign success----------")
                    return True
            # except rsa.pkcs1.VerificationError:
            except:
                print("----------verify sign failed----------")
                return False
        else:
            # 支付宝当前仅支持 RSA 加密，未来也许会有其他类型
            return False
        return False

    # 验证是否是支付宝发来的通知
    def verify_url(self, partner, notify_id):
        """
        :param partner: 卖家支付宝用户ID。 seller_id
        :param notify_id: 通知校验ID
        :return:
        """
        payload = {'service': 'notify_verify', 'partner': partner, 'notify_id': notify_id}
        r = requests.get(self.alipay_url, params=payload)
        result = r.text
        print('11111', r.text)
        if result.upper() == "TRUE":
            print("----------verify url success----------")
            return True
        return False


