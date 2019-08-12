import grpc
import json
import time
from . import paypal_pb2, paypal_pb2_grpc
import hashlib


_HOST = 'localhost'
_PORT = '8801'

conn = grpc.insecure_channel(_HOST + ':' + _PORT)

def str_md5(string):
    md = hashlib.md5()
    md.update(string.encode())
    res = md.hexdigest()
    return res


def payment_create():
    client = paypal_pb2_grpc.PaypalPayStub(channel=conn)

    req = paypal_pb2.PaymentCreateReq(client_id='AcEDucP7esIyXneuPawC-yOSGVI4V5VWbiGtCxXiylrtFE0UvZtftQtZHaLSqJTj08pB1CICdjS6bKAs',
            total=100)
    item = req.items.add()
    item.name = 'ceshi'
    item.sku='778888'
    item.price = 100
    item.quantity = 1

    response = client.PaymentCreate(req)

    return response

def payment_execute(paymentId, PayerID):
    client = paypal_pb2_grpc.PaypalPayStub(channel=conn)

    req = paypal_pb2.PaymentExecuteReq(client_id='AcEDucP7esIyXneuPawC-yOSGVI4V5VWbiGtCxXiylrtFE0UvZtftQtZHaLSqJTj08pB1CICdjS6bKAs',
            paymentId=paymentId,
            PayerID=PayerID)

    response = client.PaymentExecute(req)

    return response




