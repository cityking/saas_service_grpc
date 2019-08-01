# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tools.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tools.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0btools.proto\"+\n\x04\x46ile\x12\x11\n\tfile_code\x18\x01 \x03(\t\x12\x10\n\x08\x61pp_name\x18\x03 \x01(\t\")\n\x07Message\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"/\n\x0c\x46ileResponse\x12\x0f\n\x07message\x18\x01 \x03(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\".\n\x0fMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t2\\\n\x0bToolsServer\x12\"\n\nUploadFile\x12\x05.File\x1a\r.FileResponse\x12)\n\x0bSendMessage\x12\x08.Message\x1a\x10.MessageResponseB\x1d\n\x1bio.grpc.examples.helloworldb\x06proto3')
)




_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_code', full_name='File.file_code', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='File.app_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=58,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='Message.phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='Message.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=101,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='FileResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='FileResponse.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=150,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='MessageResponse.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='MessageResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'tools_pb2'
  # @@protoc_insertion_point(class_scope:File)
  ))
_sym_db.RegisterMessage(File)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'tools_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)

FileResponse = _reflection.GeneratedProtocolMessageType('FileResponse', (_message.Message,), dict(
  DESCRIPTOR = _FILERESPONSE,
  __module__ = 'tools_pb2'
  # @@protoc_insertion_point(class_scope:FileResponse)
  ))
_sym_db.RegisterMessage(FileResponse)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGERESPONSE,
  __module__ = 'tools_pb2'
  # @@protoc_insertion_point(class_scope:MessageResponse)
  ))
_sym_db.RegisterMessage(MessageResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.grpc.examples.helloworld'))

_TOOLSSERVER = _descriptor.ServiceDescriptor(
  name='ToolsServer',
  full_name='ToolsServer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=200,
  serialized_end=292,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='ToolsServer.UploadFile',
    index=0,
    containing_service=None,
    input_type=_FILE,
    output_type=_FILERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='ToolsServer.SendMessage',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOOLSSERVER)

DESCRIPTOR.services_by_name['ToolsServer'] = _TOOLSSERVER

# @@protoc_insertion_point(module_scope)
