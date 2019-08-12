# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: paypal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='paypal.proto',
  package='paypal',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cpaypal.proto\x12\x06paypal\"B\n\x04Item\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03sku\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x10\n\x08quantity\x18\x04 \x01(\x05\"f\n\x10PaymentCreateReq\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\r\n\x05total\x18\x01 \x01(\x02\x12\x1b\n\x05items\x18\x02 \x03(\x0b\x32\x0c.paypal.Item\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"X\n\x10PaymentCreateRsp\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x11\n\tpaymentId\x18\x03 \x01(\t\x12\x14\n\x0c\x61pproval_url\x18\x04 \x01(\t\"J\n\x11PaymentExecuteReq\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12\x11\n\tpaymentId\x18\x01 \x01(\t\x12\x0f\n\x07PayerID\x18\x02 \x01(\t\"i\n\x11PaymentExecuteRsp\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\t\x12\x11\n\tpaymentId\x18\x04 \x01(\t\x12\x14\n\x0c\x61pproval_url\x18\x05 \x01(\t2\x9c\x01\n\tPaypalPay\x12\x45\n\rPaymentCreate\x12\x18.paypal.PaymentCreateReq\x1a\x18.paypal.PaymentCreateRsp\"\x00\x12H\n\x0ePaymentExecute\x12\x19.paypal.PaymentExecuteReq\x1a\x19.paypal.PaymentExecuteRsp\"\x00\x62\x06proto3')
)




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='paypal.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='paypal.Item.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sku', full_name='paypal.Item.sku', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='paypal.Item.price', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='paypal.Item.quantity', index=3,
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
  serialized_start=24,
  serialized_end=90,
)


_PAYMENTCREATEREQ = _descriptor.Descriptor(
  name='PaymentCreateReq',
  full_name='paypal.PaymentCreateReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='paypal.PaymentCreateReq.client_id', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='paypal.PaymentCreateReq.total', index=1,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='paypal.PaymentCreateReq.items', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='paypal.PaymentCreateReq.description', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=92,
  serialized_end=194,
)


_PAYMENTCREATERSP = _descriptor.Descriptor(
  name='PaymentCreateRsp',
  full_name='paypal.PaymentCreateRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='paypal.PaymentCreateRsp.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='paypal.PaymentCreateRsp.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paymentId', full_name='paypal.PaymentCreateRsp.paymentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approval_url', full_name='paypal.PaymentCreateRsp.approval_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=196,
  serialized_end=284,
)


_PAYMENTEXECUTEREQ = _descriptor.Descriptor(
  name='PaymentExecuteReq',
  full_name='paypal.PaymentExecuteReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='paypal.PaymentExecuteReq.client_id', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paymentId', full_name='paypal.PaymentExecuteReq.paymentId', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='PayerID', full_name='paypal.PaymentExecuteReq.PayerID', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=286,
  serialized_end=360,
)


_PAYMENTEXECUTERSP = _descriptor.Descriptor(
  name='PaymentExecuteRsp',
  full_name='paypal.PaymentExecuteRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='paypal.PaymentExecuteRsp.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='paypal.PaymentExecuteRsp.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='paypal.PaymentExecuteRsp.result', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paymentId', full_name='paypal.PaymentExecuteRsp.paymentId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approval_url', full_name='paypal.PaymentExecuteRsp.approval_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=362,
  serialized_end=467,
)

_PAYMENTCREATEREQ.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['PaymentCreateReq'] = _PAYMENTCREATEREQ
DESCRIPTOR.message_types_by_name['PaymentCreateRsp'] = _PAYMENTCREATERSP
DESCRIPTOR.message_types_by_name['PaymentExecuteReq'] = _PAYMENTEXECUTEREQ
DESCRIPTOR.message_types_by_name['PaymentExecuteRsp'] = _PAYMENTEXECUTERSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'paypal_pb2'
  # @@protoc_insertion_point(class_scope:paypal.Item)
  ))
_sym_db.RegisterMessage(Item)

PaymentCreateReq = _reflection.GeneratedProtocolMessageType('PaymentCreateReq', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTCREATEREQ,
  __module__ = 'paypal_pb2'
  # @@protoc_insertion_point(class_scope:paypal.PaymentCreateReq)
  ))
_sym_db.RegisterMessage(PaymentCreateReq)

PaymentCreateRsp = _reflection.GeneratedProtocolMessageType('PaymentCreateRsp', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTCREATERSP,
  __module__ = 'paypal_pb2'
  # @@protoc_insertion_point(class_scope:paypal.PaymentCreateRsp)
  ))
_sym_db.RegisterMessage(PaymentCreateRsp)

PaymentExecuteReq = _reflection.GeneratedProtocolMessageType('PaymentExecuteReq', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTEXECUTEREQ,
  __module__ = 'paypal_pb2'
  # @@protoc_insertion_point(class_scope:paypal.PaymentExecuteReq)
  ))
_sym_db.RegisterMessage(PaymentExecuteReq)

PaymentExecuteRsp = _reflection.GeneratedProtocolMessageType('PaymentExecuteRsp', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTEXECUTERSP,
  __module__ = 'paypal_pb2'
  # @@protoc_insertion_point(class_scope:paypal.PaymentExecuteRsp)
  ))
_sym_db.RegisterMessage(PaymentExecuteRsp)



_PAYPALPAY = _descriptor.ServiceDescriptor(
  name='PaypalPay',
  full_name='paypal.PaypalPay',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=470,
  serialized_end=626,
  methods=[
  _descriptor.MethodDescriptor(
    name='PaymentCreate',
    full_name='paypal.PaypalPay.PaymentCreate',
    index=0,
    containing_service=None,
    input_type=_PAYMENTCREATEREQ,
    output_type=_PAYMENTCREATERSP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PaymentExecute',
    full_name='paypal.PaypalPay.PaymentExecute',
    index=1,
    containing_service=None,
    input_type=_PAYMENTEXECUTEREQ,
    output_type=_PAYMENTEXECUTERSP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYPALPAY)

DESCRIPTOR.services_by_name['PaypalPay'] = _PAYPALPAY

# @@protoc_insertion_point(module_scope)