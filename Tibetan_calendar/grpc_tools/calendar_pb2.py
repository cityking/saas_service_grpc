# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calendar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2

from common_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='calendar.proto',
  package='com.zhibeifw.proto',
  syntax='proto3',
  serialized_options=_b('H\001\210\001\000'),
  serialized_pb=_b('\n\x0e\x63\x61lendar.proto\x12\x12\x63om.zhibeifw.proto\x1a\x0c\x63ommon.proto\"\xc4\x01\n\rProtoCalendar\x12\x11\n\tgregorian\x18\x01 \x01(\x05\x12\x0f\n\x07\x63hinese\x18\x02 \x01(\x05\x12\x0f\n\x07tibetan\x18\x03 \x01(\x05\x12\x0f\n\x07holiday\x18\x04 \x01(\t\x12\x10\n\x08shareUrl\x18\x05 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\x12\x0b\n\x03img\x18\x07 \x01(\t\x12\x13\n\x0btibetanYear\x18\x08 \x01(\t\x12\x14\n\x0ctibetanMonth\x18\t \x01(\t\x12\x12\n\ntibetanDay\x18\n \x01(\t\"/\n\x10ProtoCalendarReq\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\r\n\x05month\x18\x03 \x01(\x05\"f\n\x15ProtoCalendarListResp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12/\n\x04list\x18\x03 \x03(\x0b\x32!.com.zhibeifw.proto.ProtoCalendar\"P\n\x16ProtoCalendarRangeResp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0c\n\x04\x66rom\x18\x03 \x01(\x05\x12\n\n\x02to\x18\x04 \x01(\x05\x32\xcf\x01\n\x0f\x43\x61lendarService\x12Y\n\x04list\x12$.com.zhibeifw.proto.ProtoCalendarReq\x1a).com.zhibeifw.proto.ProtoCalendarListResp\"\x00\x12\x61\n\x11getGregorianRange\x12\x1e.com.zhibeifw.proto.ProtoEmpty\x1a*.com.zhibeifw.proto.ProtoCalendarRangeResp\"\x00\x42\x05H\x01\x88\x01\x00P\x00\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,],
  public_dependencies=[common__pb2.DESCRIPTOR,])




_PROTOCALENDAR = _descriptor.Descriptor(
  name='ProtoCalendar',
  full_name='com.zhibeifw.proto.ProtoCalendar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gregorian', full_name='com.zhibeifw.proto.ProtoCalendar.gregorian', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chinese', full_name='com.zhibeifw.proto.ProtoCalendar.chinese', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tibetan', full_name='com.zhibeifw.proto.ProtoCalendar.tibetan', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='holiday', full_name='com.zhibeifw.proto.ProtoCalendar.holiday', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shareUrl', full_name='com.zhibeifw.proto.ProtoCalendar.shareUrl', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='com.zhibeifw.proto.ProtoCalendar.content', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img', full_name='com.zhibeifw.proto.ProtoCalendar.img', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tibetanYear', full_name='com.zhibeifw.proto.ProtoCalendar.tibetanYear', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tibetanMonth', full_name='com.zhibeifw.proto.ProtoCalendar.tibetanMonth', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tibetanDay', full_name='com.zhibeifw.proto.ProtoCalendar.tibetanDay', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=249,
)


_PROTOCALENDARREQ = _descriptor.Descriptor(
  name='ProtoCalendarReq',
  full_name='com.zhibeifw.proto.ProtoCalendarReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='com.zhibeifw.proto.ProtoCalendarReq.year', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='com.zhibeifw.proto.ProtoCalendarReq.month', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=298,
)


_PROTOCALENDARLISTRESP = _descriptor.Descriptor(
  name='ProtoCalendarListResp',
  full_name='com.zhibeifw.proto.ProtoCalendarListResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='com.zhibeifw.proto.ProtoCalendarListResp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='com.zhibeifw.proto.ProtoCalendarListResp.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='com.zhibeifw.proto.ProtoCalendarListResp.list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=402,
)


_PROTOCALENDARRANGERESP = _descriptor.Descriptor(
  name='ProtoCalendarRangeResp',
  full_name='com.zhibeifw.proto.ProtoCalendarRangeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='com.zhibeifw.proto.ProtoCalendarRangeResp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='com.zhibeifw.proto.ProtoCalendarRangeResp.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='com.zhibeifw.proto.ProtoCalendarRangeResp.from', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='com.zhibeifw.proto.ProtoCalendarRangeResp.to', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=484,
)

_PROTOCALENDARLISTRESP.fields_by_name['list'].message_type = _PROTOCALENDAR
DESCRIPTOR.message_types_by_name['ProtoCalendar'] = _PROTOCALENDAR
DESCRIPTOR.message_types_by_name['ProtoCalendarReq'] = _PROTOCALENDARREQ
DESCRIPTOR.message_types_by_name['ProtoCalendarListResp'] = _PROTOCALENDARLISTRESP
DESCRIPTOR.message_types_by_name['ProtoCalendarRangeResp'] = _PROTOCALENDARRANGERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoCalendar = _reflection.GeneratedProtocolMessageType('ProtoCalendar', (_message.Message,), dict(
  DESCRIPTOR = _PROTOCALENDAR,
  __module__ = 'calendar_pb2'
  # @@protoc_insertion_point(class_scope:com.zhibeifw.proto.ProtoCalendar)
  ))
_sym_db.RegisterMessage(ProtoCalendar)

ProtoCalendarReq = _reflection.GeneratedProtocolMessageType('ProtoCalendarReq', (_message.Message,), dict(
  DESCRIPTOR = _PROTOCALENDARREQ,
  __module__ = 'calendar_pb2'
  # @@protoc_insertion_point(class_scope:com.zhibeifw.proto.ProtoCalendarReq)
  ))
_sym_db.RegisterMessage(ProtoCalendarReq)

ProtoCalendarListResp = _reflection.GeneratedProtocolMessageType('ProtoCalendarListResp', (_message.Message,), dict(
  DESCRIPTOR = _PROTOCALENDARLISTRESP,
  __module__ = 'calendar_pb2'
  # @@protoc_insertion_point(class_scope:com.zhibeifw.proto.ProtoCalendarListResp)
  ))
_sym_db.RegisterMessage(ProtoCalendarListResp)

ProtoCalendarRangeResp = _reflection.GeneratedProtocolMessageType('ProtoCalendarRangeResp', (_message.Message,), dict(
  DESCRIPTOR = _PROTOCALENDARRANGERESP,
  __module__ = 'calendar_pb2'
  # @@protoc_insertion_point(class_scope:com.zhibeifw.proto.ProtoCalendarRangeResp)
  ))
_sym_db.RegisterMessage(ProtoCalendarRangeResp)


DESCRIPTOR._options = None

_CALENDARSERVICE = _descriptor.ServiceDescriptor(
  name='CalendarService',
  full_name='com.zhibeifw.proto.CalendarService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=487,
  serialized_end=694,
  methods=[
  _descriptor.MethodDescriptor(
    name='list',
    full_name='com.zhibeifw.proto.CalendarService.list',
    index=0,
    containing_service=None,
    input_type=_PROTOCALENDARREQ,
    output_type=_PROTOCALENDARLISTRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getGregorianRange',
    full_name='com.zhibeifw.proto.CalendarService.getGregorianRange',
    index=1,
    containing_service=None,
    input_type=common__pb2._PROTOEMPTY,
    output_type=_PROTOCALENDARRANGERESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALENDARSERVICE)

DESCRIPTOR.services_by_name['CalendarService'] = _CALENDARSERVICE

# @@protoc_insertion_point(module_scope)
