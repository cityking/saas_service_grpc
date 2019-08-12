from django.urls import path
from pay_app import views

urlpatterns = [
    path('weixin_order/', views.WeixinOrderView.as_view()),
    path('weixin_refund/', views.WeixinRefundView.as_view()),
    path('weixin_micropay/', views.WeixinMicropayView.as_view()),
    path('pay_callback/', views.PayCallbackView.as_view()),
    path('paypal_callback/', views.PayPalCallbackView.as_view()),
]
