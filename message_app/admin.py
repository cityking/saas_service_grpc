from django.contrib import admin

from message_app.models import Business, MsgRecord, ChargePackage, Order, PayInfo

# Register your models here.
admin.site.register(Business)
admin.site.register(MsgRecord)
admin.site.register(ChargePackage)
admin.site.register(Order)
admin.site.register(PayInfo)



