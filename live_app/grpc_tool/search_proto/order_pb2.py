# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='order.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\024com.jyzh.jetpet.grpc'),
  serialized_pb=_b('\n\x0border.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"e\n\x0b\x42\x61nkAccount\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03num\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"y\n\x08VipPrice\x12\x0e\n\x06switch\x18\x01 \x01(\x08\x12\x10\n\x08use_test\x18\x02 \x01(\x08\x12\x11\n\tper_month\x18\x03 \x01(\x01\x12\x13\n\x0bthree_month\x18\x04 \x01(\x01\x12\x11\n\thalf_year\x18\x05 \x01(\x01\x12\x10\n\x08per_year\x18\x06 \x01(\x01\"g\n\x08VipGoods\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06period\x18\x04 \x01(\x05\x12\x0f\n\x07\x63utdown\x18\x05 \x01(\x01\x12\x11\n\tavg_price\x18\x06 \x01(\x01\"i\n\tDonateReq\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\twith_gift\x18\x02 \x01(\x08\x12\x12\n\naddress_id\x18\x03 \x01(\x05\x12\x11\n\ttotal_fee\x18\x04 \x01(\x01\x12\x10\n\x08pay_type\x18\x05 \x01(\x05\"\x8d\x01\n\x10\x44onateOfflineReq\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\twith_gift\x18\x02 \x01(\x08\x12\x12\n\naddress_id\x18\x03 \x01(\x05\x12\x11\n\ttotal_fee\x18\x04 \x01(\x01\x12\x0c\n\x04\x62\x61nk\x18\x08 \x01(\t\x12\x10\n\x08\x62\x61nk_num\x18\t \x01(\t\x12\r\n\x05proof\x18\n \x01(\t\"2\n\x08\x42yVipReq\x12\x14\n\x0cvip_goods_id\x18\x01 \x01(\x05\x12\x10\n\x08pay_type\x18\x02 \x01(\x05\"0\n\x07PayType\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03pic\x18\x03 \x01(\t\"\xed\x01\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04user\x18\x02 \x01(\x05\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x11\n\twith_gift\x18\x04 \x01(\x08\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\x05\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06status\x18\x07 \x01(\x05\x12\x0c\n\x04\x62\x61nk\x18\x08 \x01(\t\x12\r\n\x05proof\x18\n \x01(\t\x12\x11\n\ttotal_fee\x18\x0c \x01(\x01\x12\x10\n\x08pay_type\x18\r \x01(\x05\x12\x11\n\torder_num\x18\x0e \x01(\tB\x16\n\x14\x63om.jyzh.jetpet.grpcb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BANKACCOUNT = _descriptor.Descriptor(
  name='BankAccount',
  full_name='BankAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='BankAccount.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='BankAccount.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='BankAccount.num', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='BankAccount.create_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=48,
  serialized_end=149,
)


_VIPPRICE = _descriptor.Descriptor(
  name='VipPrice',
  full_name='VipPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch', full_name='VipPrice.switch', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_test', full_name='VipPrice.use_test', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_month', full_name='VipPrice.per_month', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='three_month', full_name='VipPrice.three_month', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_year', full_name='VipPrice.half_year', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_year', full_name='VipPrice.per_year', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=151,
  serialized_end=272,
)


_VIPGOODS = _descriptor.Descriptor(
  name='VipGoods',
  full_name='VipGoods',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='VipGoods.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='VipGoods.price', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='VipGoods.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='VipGoods.period', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cutdown', full_name='VipGoods.cutdown', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_price', full_name='VipGoods.avg_price', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=274,
  serialized_end=377,
)


_DONATEREQ = _descriptor.Descriptor(
  name='DonateReq',
  full_name='DonateReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='DonateReq.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_gift', full_name='DonateReq.with_gift', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address_id', full_name='DonateReq.address_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_fee', full_name='DonateReq.total_fee', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_type', full_name='DonateReq.pay_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=379,
  serialized_end=484,
)


_DONATEOFFLINEREQ = _descriptor.Descriptor(
  name='DonateOfflineReq',
  full_name='DonateOfflineReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='DonateOfflineReq.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_gift', full_name='DonateOfflineReq.with_gift', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address_id', full_name='DonateOfflineReq.address_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_fee', full_name='DonateOfflineReq.total_fee', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank', full_name='DonateOfflineReq.bank', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_num', full_name='DonateOfflineReq.bank_num', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='DonateOfflineReq.proof', index=6,
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
  serialized_start=487,
  serialized_end=628,
)


_BYVIPREQ = _descriptor.Descriptor(
  name='ByVipReq',
  full_name='ByVipReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vip_goods_id', full_name='ByVipReq.vip_goods_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_type', full_name='ByVipReq.pay_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=630,
  serialized_end=680,
)


_PAYTYPE = _descriptor.Descriptor(
  name='PayType',
  full_name='PayType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PayType.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='PayType.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pic', full_name='PayType.pic', index=2,
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
  serialized_start=682,
  serialized_end=730,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Order.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='Order.user', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='Order.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_gift', full_name='Order.with_gift', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Order.address', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='Order.create_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Order.status', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank', full_name='Order.bank', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='Order.proof', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_fee', full_name='Order.total_fee', index=9,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_type', full_name='Order.pay_type', index=10,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_num', full_name='Order.order_num', index=11,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=733,
  serialized_end=970,
)

_BANKACCOUNT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORDER.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['BankAccount'] = _BANKACCOUNT
DESCRIPTOR.message_types_by_name['VipPrice'] = _VIPPRICE
DESCRIPTOR.message_types_by_name['VipGoods'] = _VIPGOODS
DESCRIPTOR.message_types_by_name['DonateReq'] = _DONATEREQ
DESCRIPTOR.message_types_by_name['DonateOfflineReq'] = _DONATEOFFLINEREQ
DESCRIPTOR.message_types_by_name['ByVipReq'] = _BYVIPREQ
DESCRIPTOR.message_types_by_name['PayType'] = _PAYTYPE
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BankAccount = _reflection.GeneratedProtocolMessageType('BankAccount', (_message.Message,), dict(
  DESCRIPTOR = _BANKACCOUNT,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:BankAccount)
  ))
_sym_db.RegisterMessage(BankAccount)

VipPrice = _reflection.GeneratedProtocolMessageType('VipPrice', (_message.Message,), dict(
  DESCRIPTOR = _VIPPRICE,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:VipPrice)
  ))
_sym_db.RegisterMessage(VipPrice)

VipGoods = _reflection.GeneratedProtocolMessageType('VipGoods', (_message.Message,), dict(
  DESCRIPTOR = _VIPGOODS,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:VipGoods)
  ))
_sym_db.RegisterMessage(VipGoods)

DonateReq = _reflection.GeneratedProtocolMessageType('DonateReq', (_message.Message,), dict(
  DESCRIPTOR = _DONATEREQ,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:DonateReq)
  ))
_sym_db.RegisterMessage(DonateReq)

DonateOfflineReq = _reflection.GeneratedProtocolMessageType('DonateOfflineReq', (_message.Message,), dict(
  DESCRIPTOR = _DONATEOFFLINEREQ,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:DonateOfflineReq)
  ))
_sym_db.RegisterMessage(DonateOfflineReq)

ByVipReq = _reflection.GeneratedProtocolMessageType('ByVipReq', (_message.Message,), dict(
  DESCRIPTOR = _BYVIPREQ,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:ByVipReq)
  ))
_sym_db.RegisterMessage(ByVipReq)

PayType = _reflection.GeneratedProtocolMessageType('PayType', (_message.Message,), dict(
  DESCRIPTOR = _PAYTYPE,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:PayType)
  ))
_sym_db.RegisterMessage(PayType)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
  DESCRIPTOR = _ORDER,
  __module__ = 'order_pb2'
  # @@protoc_insertion_point(class_scope:Order)
  ))
_sym_db.RegisterMessage(Order)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)