# from base64 import b64decode
import grpc
import json
from pay_app.message_grpc import client

from . import tools_pb2, tools_pb2_grpc#, charge_pb2, charge_pb2_grpc
from .tool import b64_upload
from .PhoneNumberVerificator import pnv

def msg_send_before(biz_id=None, biz_name=None):
    biz_info = client.query_businessinfo(biz_id)
    if biz_info["status"] == "success":
         return biz_info["business_info"]["msg_num"] > 0
    return False

def msg_send_after(biz_id, phone, content):
    res = client.add_msg_send_record(biz_id, phone,content)
    return res["status"] == "success"




class ToolsHandler(tools_pb2_grpc.ToolsServerServicer):

    def UploadFile(self, request, context):
        """文件上传"""
        # import ipdb;ipdb.set_trace()
        url = b64_upload(request.file_code)
        return tools_pb2.FileResponse(
            message=url, status=200
        )

    def SendMessage(self, request, context):
        """发送短信"""
        phone = request.phone
        content = request.content

        msg_send_before(biz_id=1)
        if pnv.send(phone, content):
            msg_send_after(biz_id, phone, content)
            return tools_pb2.MessageResponse(status=200, msg="发送成功")
        else:
            return tools_pb2.MessageResponse(status=400, msg="发送失败")


