# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamberry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamberry.proto',
  package='gen.proto.streamberry',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11streamberry.proto\x12\x15gen.proto.streamberry\"\x17\n\x07GetPage\x12\x0c\n\x04page\x18\x01 \x01(\x03\x62\x06proto3'
)




_GETPAGE = _descriptor.Descriptor(
  name='GetPage',
  full_name='gen.proto.streamberry.GetPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='gen.proto.streamberry.GetPage.page', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=44,
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['GetPage'] = _GETPAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPage = _reflection.GeneratedProtocolMessageType('GetPage', (_message.Message,), {
  'DESCRIPTOR' : _GETPAGE,
  '__module__' : 'streamberry_pb2'
  # @@protoc_insertion_point(class_scope:gen.proto.streamberry.GetPage)
  })
_sym_db.RegisterMessage(GetPage)


# @@protoc_insertion_point(module_scope)
