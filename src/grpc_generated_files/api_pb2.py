# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\"+\n\nApiRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x0b\x41piResponse\x12\x10\n\x08response\x18\x01 \x01(\t2/\n\x03\x41pi\x12(\n\x0b\x41piEndpoint\x12\x0b.ApiRequest\x1a\x0c.ApiResponseb\x06proto3'
)




_APIREQUEST = _descriptor.Descriptor(
  name='ApiRequest',
  full_name='ApiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ApiRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='ApiRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=13,
  serialized_end=56,
)


_APIRESPONSE = _descriptor.Descriptor(
  name='ApiResponse',
  full_name='ApiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='ApiResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=58,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['ApiRequest'] = _APIREQUEST
DESCRIPTOR.message_types_by_name['ApiResponse'] = _APIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApiRequest = _reflection.GeneratedProtocolMessageType('ApiRequest', (_message.Message,), {
  'DESCRIPTOR' : _APIREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:ApiRequest)
  })
_sym_db.RegisterMessage(ApiRequest)

ApiResponse = _reflection.GeneratedProtocolMessageType('ApiResponse', (_message.Message,), {
  'DESCRIPTOR' : _APIRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:ApiResponse)
  })
_sym_db.RegisterMessage(ApiResponse)



_API = _descriptor.ServiceDescriptor(
  name='Api',
  full_name='Api',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=138,
  methods=[
  _descriptor.MethodDescriptor(
    name='ApiEndpoint',
    full_name='Api.ApiEndpoint',
    index=0,
    containing_service=None,
    input_type=_APIREQUEST,
    output_type=_APIRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['Api'] = _API

# @@protoc_insertion_point(module_scope)
