# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import live_pb2 as live__pb2
#import live_pb2 as live__pb2


class LiveManagementStub(object):
  """测试地址 192.168.3.217
  端口 8800

  直播管理
  定义服务,用在rpc传输中
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLiveList = channel.unary_unary(
        '/live_app.LiveManagement/GetLiveList',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.AddLive = channel.unary_unary(
        '/live_app.LiveManagement/AddLive',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.UpdateLive = channel.unary_unary(
        '/live_app.LiveManagement/UpdateLive',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.DeleteLive = channel.unary_unary(
        '/live_app.LiveManagement/DeleteLive',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.GetLatestLive = channel.unary_unary(
        '/live_app.LiveManagement/GetLatestLive',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )


class LiveManagementServicer(object):
  """测试地址 192.168.3.217
  端口 8800

  直播管理
  定义服务,用在rpc传输中
  """

  def GetLiveList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestLive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LiveManagementServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLiveList': grpc.unary_unary_rpc_method_handler(
          servicer.GetLiveList,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'AddLive': grpc.unary_unary_rpc_method_handler(
          servicer.AddLive,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'UpdateLive': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLive,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'DeleteLive': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLive,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'GetLatestLive': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestLive,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'live_app.LiveManagement', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PlayBackManagementStub(object):
  """定义服务,用在rpc传输中
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPlayBackList = channel.unary_unary(
        '/live_app.PlayBackManagement/GetPlayBackList',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.AddPlayBack = channel.unary_unary(
        '/live_app.PlayBackManagement/AddPlayBack',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.UpdatePlayBack = channel.unary_unary(
        '/live_app.PlayBackManagement/UpdatePlayBack',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.DeletePlayBack = channel.unary_unary(
        '/live_app.PlayBackManagement/DeletePlayBack',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.GetNoAddPlayBack = channel.unary_unary(
        '/live_app.PlayBackManagement/GetNoAddPlayBack',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )


class PlayBackManagementServicer(object):
  """定义服务,用在rpc传输中
  """

  def GetPlayBackList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPlayBack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePlayBack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePlayBack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNoAddPlayBack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PlayBackManagementServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPlayBackList': grpc.unary_unary_rpc_method_handler(
          servicer.GetPlayBackList,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'AddPlayBack': grpc.unary_unary_rpc_method_handler(
          servicer.AddPlayBack,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'UpdatePlayBack': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePlayBack,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'DeletePlayBack': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePlayBack,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'GetNoAddPlayBack': grpc.unary_unary_rpc_method_handler(
          servicer.GetNoAddPlayBack,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'live_app.PlayBackManagement', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class LiveStreamManagementStub(object):
  """定义服务,用在rpc传输中
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLiveStreams = channel.unary_unary(
        '/live_app.LiveStreamManagement/GetLiveStreams',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.AddLiveStream = channel.unary_unary(
        '/live_app.LiveStreamManagement/AddLiveStream',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.UpdateLiveStream = channel.unary_unary(
        '/live_app.LiveStreamManagement/UpdateLiveStream',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )
    self.DeleteLiveStream = channel.unary_unary(
        '/live_app.LiveStreamManagement/DeleteLiveStream',
        request_serializer=live__pb2.json.SerializeToString,
        response_deserializer=live__pb2.json.FromString,
        )


class LiveStreamManagementServicer(object):
  """定义服务,用在rpc传输中
  """

  def GetLiveStreams(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLiveStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLiveStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLiveStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LiveStreamManagementServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLiveStreams': grpc.unary_unary_rpc_method_handler(
          servicer.GetLiveStreams,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'AddLiveStream': grpc.unary_unary_rpc_method_handler(
          servicer.AddLiveStream,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'UpdateLiveStream': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLiveStream,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
      'DeleteLiveStream': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLiveStream,
          request_deserializer=live__pb2.json.FromString,
          response_serializer=live__pb2.json.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'live_app.LiveStreamManagement', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))