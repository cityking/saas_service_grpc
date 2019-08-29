from django.db import models
import time
from message_app.grpc_tool.pay_service.client import unified_order, precreate, weixin_order_query, ali_order_query

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    msg_num = models.IntegerField('短信余量', default=0)

    def __str__(self):
        return self.name

    def get_info(self):
        return dict(business_id=self.id,
                name=self.name, msg_num=self.msg_num)

    class Meta:
        verbose_name = "商户"
        verbose_name_plural = verbose_name
        db_table = 'msg_business'

class MsgRecord(models.Model):
    business = models.ForeignKey(Business, verbose_name='商户', on_delete=None)
    phone = models.CharField('手机号', max_length=20)
    content = models.CharField('内容', max_length=500)
    create_time = models.DateTimeField('发送时间', auto_now_add=True)
    state = models.IntegerField('状态', default=1)

    def __str__(self):
        return self.phone



    class Meta:
        verbose_name = "短信记录"
        verbose_name_plural = verbose_name
        db_table = 'msg_record'

class ChargePackage(models.Model):
    title = models.CharField('标题', max_length=30, null=True)
    price = models.FloatField('价格', default=0)
    charge_num = models.IntegerField('充值条数', default=0)


    def __str__(self):
        return self.title

    def get_info(self):
        return dict(title=self.title,
                price=self.price, charge_num=self.charge_num)

    class Meta:
        verbose_name = "充值套餐"
        verbose_name_plural = verbose_name
        db_table = 'msg_charge_package'

class Order(models.Model):
    order_no = models.CharField('订单号', max_length=20)
    business = models.ForeignKey(Business, verbose_name='商户', on_delete=None)
    charge_num = models.IntegerField('充值条数', default=0)
    price = models.FloatField('价格', default=0)
    pay_type = models.IntegerField('支付方式', default=1) #1 支付宝 2 微信
    create_time = models.DateTimeField('充值时间', auto_now_add=True)
    state = models.IntegerField('状态', default=0) #0 未支付 1 已支付

    def __str__(self):
        return self.order_no

    def get_app_id(self):
        pay_info = PayInfo.objects.filter(business=self.business,
                pay_type=self.pay_type).first()
        if not pay_info:
            return None
        app_id = pay_info.app_id
        return app_id

    @classmethod
    def get_order_no(cls):
        now = time.time()
        import random
        num = now + random.randint(0, 1000000)
        return str(num).replace('.', '')

    def get_info(self):
        return dict(order_no=self.order_no,
                charge_num=self.charge_num,
                price=self.price,
                pay_type=self.pay_type,
                create_time=self.create_time.strftime('%Y-%m-%d'))

    def pay_order(self):
        app_id = self.get_app_id()
        if self.pay_type == 2:
            data = unified_order(app_id, self.order_no, '短信充值',self.price,
                    self.id, 'NATIVE')
            if data['return_code'] == 'SUCCESS' and data['return_msg'] == 'OK':
                return data['code_url']
            else:
                return None
        elif self.pay_type == 1:
            data = precreate(app_id, self.order_no, self.price, '短信充值')
            print(data)
            if data['alipay_trade_precreate_response']['code'] == '10000' and data['alipay_trade_precreate_response']['msg'] == 'Success':
                return data['alipay_trade_precreate_response']['qr_code']
            else:
                return None

    def query_pay_state(self):
        app_id = self.get_app_id()
        if self.pay_type == 1:
            data = ali_order_query(app_id, self.order_no)

            if data['alipay_trade_query_response']['code'] == '10000' and\
                data['alipay_trade_query_response']['msg'] == 'Success' and\
                data['alipay_trade_query_response']['trade_status']:
                return True
            else:
                return None

        elif self.pay_type == 2:
            data = weixin_order_query(app_id, self.order_no)
            if data['return_code'] == 'SUCCESS' and data['return_msg'] == 'OK' and data['trade_state'] == 'SUCCESS':
                return True
            else:
                return None


    def get_info(self):
        return dict(order_no=self.order_no,
                business=self.business.name,
                charge_num=self.charge_num,
                price=self.price,
                pay_type=self.pay_type)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name
        db_table = 'msg_order'

class PayInfo(models.Model):
    business = models.ForeignKey(Business, verbose_name='商户', on_delete=None)
    pay_type = models.IntegerField('支付方式', default=1) #1 支付宝支付 2 微信支付
    app_id = models.CharField(max_length=50)

    def __str__(self):
        return self.pay_type

    def get_pay_type(self):
        if self.pay_type == 1:
            return '支付宝支付'
        else:
            return '微信支付'


    class Meta:
        verbose_name = "支付信息"
        verbose_name_plural = verbose_name
        db_table = 'msg_pay_info'

