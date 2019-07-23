from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .tool import image_upload
from .handler import *
from django.http import JsonResponse

# Create your views here.



@csrf_exempt
def upload(request):
    """上传文件"""
    request.files = request.FILES
    urls = image_upload(request, 'file')
    url = urls[0] if urls else ''
    response = JsonResponse({"url":url})
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
    response['Access-Control-Allow-Headers'] = '*'
    response['Access-Control-Allow-Credentials'] = True
    return response

def send_message(request):
    data = request.GET

    biz_id = data["biz_id"]
    phone = data['phone']
    content = data["content"]

    msg_send_before(biz_id=biz_id)
    if pnv.send(phone, content):
        msg_send_after(biz_id, phone, content)
        response = JsonResponse({"status":200, "msg":"发送成功"})
    else:
        response = JsonResponse({"status":400, "msg":"发送失败"})

    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
    response['Access-Control-Allow-Headers'] = '*'
    response['Access-Control-Allow-Credentials'] = True
    return response
