# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import charge_pb2 as charge__pb2


class MessageChargeStub(object):
  """测试地址 192.168.3.217
  端口 8800

  短信充值
  定义服务,用在rpc传输中
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.QueryBusinessInfo = channel.unary_unary(
        '/message_app.MessageCharge/QueryBusinessInfo',
        request_serializer=charge__pb2.json.SerializeToString,
        response_deserializer=charge__pb2.json.FromString,
        )
    self.AddMsgSendRecord = channel.unary_unary(
        '/message_app.MessageCharge/AddMsgSendRecord',
        request_serializer=charge__pb2.json.SerializeToString,
        response_deserializer=charge__pb2.json.FromString,
        )
    self.GetChargeInfo = channel.unary_unary(
        '/message_app.MessageCharge/GetChargeInfo',
        request_serializer=charge__pb2.json.SerializeToString,
        response_deserializer=charge__pb2.json.FromString,
        )
    self.UnifiedOrder = channel.unary_unary(
        '/message_app.MessageCharge/UnifiedOrder',
        request_serializer=charge__pb2.json.SerializeToString,
        response_deserializer=charge__pb2.json.FromString,
        )
    self.CheckOrder = channel.unary_unary(
        '/message_app.MessageCharge/CheckOrder',
        request_serializer=charge__pb2.json.SerializeToString,
        response_deserializer=charge__pb2.json.FromString,
        )
    self.QueryOrderList = channel.unary_unary(
        '/message_app.MessageCharge/QueryOrderList',
        request_serializer=charge__pb2.json.SerializeToString,
        response_deserializer=charge__pb2.json.FromString,
        )


class MessageChargeServicer(object):
  """测试地址 192.168.3.217
  端口 8800

  短信充值
  定义服务,用在rpc传输中
  """

  def QueryBusinessInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddMsgSendRecord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChargeInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnifiedOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryOrderList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessageChargeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'QueryBusinessInfo': grpc.unary_unary_rpc_method_handler(
          servicer.QueryBusinessInfo,
          request_deserializer=charge__pb2.json.FromString,
          response_serializer=charge__pb2.json.SerializeToString,
      ),
      'AddMsgSendRecord': grpc.unary_unary_rpc_method_handler(
          servicer.AddMsgSendRecord,
          request_deserializer=charge__pb2.json.FromString,
          response_serializer=charge__pb2.json.SerializeToString,
      ),
      'GetChargeInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetChargeInfo,
          request_deserializer=charge__pb2.json.FromString,
          response_serializer=charge__pb2.json.SerializeToString,
      ),
      'UnifiedOrder': grpc.unary_unary_rpc_method_handler(
          servicer.UnifiedOrder,
          request_deserializer=charge__pb2.json.FromString,
          response_serializer=charge__pb2.json.SerializeToString,
      ),
      'CheckOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CheckOrder,
          request_deserializer=charge__pb2.json.FromString,
          response_serializer=charge__pb2.json.SerializeToString,
      ),
      'QueryOrderList': grpc.unary_unary_rpc_method_handler(
          servicer.QueryOrderList,
          request_deserializer=charge__pb2.json.FromString,
          response_serializer=charge__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'message_app.MessageCharge', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
