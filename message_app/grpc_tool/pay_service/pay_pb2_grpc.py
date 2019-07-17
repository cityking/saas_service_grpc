# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import pay_pb2 as pay__pb2


class WeixinPayStub(object):
  """微信支付
  定义服务,用在rpc传输中
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.OrderQuery = channel.unary_unary(
        '/weixin.WeixinPay/OrderQuery',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.UnifiedOrder = channel.unary_unary(
        '/weixin.WeixinPay/UnifiedOrder',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.CloseOrder = channel.unary_unary(
        '/weixin.WeixinPay/CloseOrder',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.Refund = channel.unary_unary(
        '/weixin.WeixinPay/Refund',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.RefundQuery = channel.unary_unary(
        '/weixin.WeixinPay/RefundQuery',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.Micropay = channel.unary_unary(
        '/weixin.WeixinPay/Micropay',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )


class WeixinPayServicer(object):
  """微信支付
  定义服务,用在rpc传输中
  """

  def OrderQuery(self, request, context):
    """查询订单
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnifiedOrder(self, request, context):
    """统一下单
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseOrder(self, request, context):
    """关闭订单
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Refund(self, request, context):
    """退款
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RefundQuery(self, request, context):
    """退款查询
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Micropay(self, request, context):
    """付款码支付
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WeixinPayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'OrderQuery': grpc.unary_unary_rpc_method_handler(
          servicer.OrderQuery,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'UnifiedOrder': grpc.unary_unary_rpc_method_handler(
          servicer.UnifiedOrder,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'CloseOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CloseOrder,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'Refund': grpc.unary_unary_rpc_method_handler(
          servicer.Refund,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'RefundQuery': grpc.unary_unary_rpc_method_handler(
          servicer.RefundQuery,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'Micropay': grpc.unary_unary_rpc_method_handler(
          servicer.Micropay,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'weixin.WeixinPay', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AliPayStub(object):
  """支付宝支付
  定义服务,用在rpc传输中
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FacePay = channel.unary_unary(
        '/weixin.AliPay/FacePay',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.Precreate = channel.unary_unary(
        '/weixin.AliPay/Precreate',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.AppPay = channel.unary_unary(
        '/weixin.AliPay/AppPay',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.OrderQuery = channel.unary_unary(
        '/weixin.AliPay/OrderQuery',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )
    self.Refund = channel.unary_unary(
        '/weixin.AliPay/Refund',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )


class AliPayServicer(object):
  """支付宝支付
  定义服务,用在rpc传输中
  """

  def FacePay(self, request, context):
    """面对面付款码支付
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Precreate(self, request, context):
    """预创建订单，适用扫码支付
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AppPay(self, request, context):
    """app支付 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OrderQuery(self, request, context):
    """订单查询
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Refund(self, request, context):
    """退款
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AliPayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FacePay': grpc.unary_unary_rpc_method_handler(
          servicer.FacePay,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'Precreate': grpc.unary_unary_rpc_method_handler(
          servicer.Precreate,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'AppPay': grpc.unary_unary_rpc_method_handler(
          servicer.AppPay,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'OrderQuery': grpc.unary_unary_rpc_method_handler(
          servicer.OrderQuery,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
      'Refund': grpc.unary_unary_rpc_method_handler(
          servicer.Refund,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'weixin.AliPay', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TibetanCalendarStub(object):
  """藏历
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.QueryCalendar = channel.unary_unary(
        '/weixin.TibetanCalendar/QueryCalendar',
        request_serializer=pay__pb2.json.SerializeToString,
        response_deserializer=pay__pb2.json.FromString,
        )


class TibetanCalendarServicer(object):
  """藏历
  """

  def QueryCalendar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TibetanCalendarServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'QueryCalendar': grpc.unary_unary_rpc_method_handler(
          servicer.QueryCalendar,
          request_deserializer=pay__pb2.json.FromString,
          response_serializer=pay__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'weixin.TibetanCalendar', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
