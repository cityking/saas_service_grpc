from django.contrib import admin
from pay_app.models import WeixinPay, AliPay

# Register your models here.
admin.site.register(WeixinPay)
admin.site.register(AliPay)
