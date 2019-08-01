# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import tools_pb2 as tools__pb2


class ToolsServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadFile = channel.unary_unary(
        '/ToolsServer/UploadFile',
        request_serializer=tools__pb2.File.SerializeToString,
        response_deserializer=tools__pb2.FileResponse.FromString,
        )
    self.SendMessage = channel.unary_unary(
        '/ToolsServer/SendMessage',
        request_serializer=tools__pb2.Message.SerializeToString,
        response_deserializer=tools__pb2.MessageResponse.FromString,
        )


class ToolsServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UploadFile(self, request, context):
    """文件上传
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendMessage(self, request, context):
    """发送短信
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ToolsServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadFile': grpc.unary_unary_rpc_method_handler(
          servicer.UploadFile,
          request_deserializer=tools__pb2.File.FromString,
          response_serializer=tools__pb2.FileResponse.SerializeToString,
      ),
      'SendMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SendMessage,
          request_deserializer=tools__pb2.Message.FromString,
          response_serializer=tools__pb2.MessageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ToolsServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
