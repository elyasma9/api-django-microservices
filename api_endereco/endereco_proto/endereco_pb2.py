# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endereco_proto/endereco.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='endereco_proto/endereco.proto',
  package='endereco',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x65ndereco_proto/endereco.proto\x12\x08\x65ndereco\x1a\x1bgoogle/protobuf/empty.proto\"p\n\x08\x45ndereco\x12\x13\n\x0b\x63\x64_endereco\x18\x01 \x01(\t\x12\x0b\n\x03\x63\x65p\x18\x02 \x01(\t\x12\x12\n\nlogradouro\x18\x03 \x01(\t\x12\x0e\n\x06\x62\x61irro\x18\x04 \x01(\t\x12\x0e\n\x06\x63idade\x18\x05 \x01(\t\x12\x0e\n\x06\x65stado\x18\x06 \x01(\t\"\x15\n\x13\x45nderecoListRequest\".\n\x17\x45nderecoRetrieveRequest\x12\x13\n\x0b\x63\x64_endereco\x18\x01 \x01(\t2\xb9\x02\n\x12\x45nderecoController\x12=\n\x04List\x12\x1d.endereco.EnderecoListRequest\x1a\x12.endereco.Endereco\"\x00\x30\x01\x12\x32\n\x06\x43reate\x12\x12.endereco.Endereco\x1a\x12.endereco.Endereco\"\x00\x12\x43\n\x08Retrieve\x12!.endereco.EnderecoRetrieveRequest\x1a\x12.endereco.Endereco\"\x00\x12\x32\n\x06Update\x12\x12.endereco.Endereco\x1a\x12.endereco.Endereco\"\x00\x12\x37\n\x07\x44\x65stroy\x12\x12.endereco.Endereco\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ENDERECO = _descriptor.Descriptor(
  name='Endereco',
  full_name='endereco.Endereco',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cd_endereco', full_name='endereco.Endereco.cd_endereco', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cep', full_name='endereco.Endereco.cep', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logradouro', full_name='endereco.Endereco.logradouro', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bairro', full_name='endereco.Endereco.bairro', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cidade', full_name='endereco.Endereco.cidade', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estado', full_name='endereco.Endereco.estado', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=72,
  serialized_end=184,
)


_ENDERECOLISTREQUEST = _descriptor.Descriptor(
  name='EnderecoListRequest',
  full_name='endereco.EnderecoListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=186,
  serialized_end=207,
)


_ENDERECORETRIEVEREQUEST = _descriptor.Descriptor(
  name='EnderecoRetrieveRequest',
  full_name='endereco.EnderecoRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cd_endereco', full_name='endereco.EnderecoRetrieveRequest.cd_endereco', index=0,
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
  serialized_start=209,
  serialized_end=255,
)

DESCRIPTOR.message_types_by_name['Endereco'] = _ENDERECO
DESCRIPTOR.message_types_by_name['EnderecoListRequest'] = _ENDERECOLISTREQUEST
DESCRIPTOR.message_types_by_name['EnderecoRetrieveRequest'] = _ENDERECORETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endereco = _reflection.GeneratedProtocolMessageType('Endereco', (_message.Message,), {
  'DESCRIPTOR' : _ENDERECO,
  '__module__' : 'endereco_proto.endereco_pb2'
  # @@protoc_insertion_point(class_scope:endereco.Endereco)
  })
_sym_db.RegisterMessage(Endereco)

EnderecoListRequest = _reflection.GeneratedProtocolMessageType('EnderecoListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENDERECOLISTREQUEST,
  '__module__' : 'endereco_proto.endereco_pb2'
  # @@protoc_insertion_point(class_scope:endereco.EnderecoListRequest)
  })
_sym_db.RegisterMessage(EnderecoListRequest)

EnderecoRetrieveRequest = _reflection.GeneratedProtocolMessageType('EnderecoRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENDERECORETRIEVEREQUEST,
  '__module__' : 'endereco_proto.endereco_pb2'
  # @@protoc_insertion_point(class_scope:endereco.EnderecoRetrieveRequest)
  })
_sym_db.RegisterMessage(EnderecoRetrieveRequest)



_ENDERECOCONTROLLER = _descriptor.ServiceDescriptor(
  name='EnderecoController',
  full_name='endereco.EnderecoController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=258,
  serialized_end=571,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='endereco.EnderecoController.List',
    index=0,
    containing_service=None,
    input_type=_ENDERECOLISTREQUEST,
    output_type=_ENDERECO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='endereco.EnderecoController.Create',
    index=1,
    containing_service=None,
    input_type=_ENDERECO,
    output_type=_ENDERECO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='endereco.EnderecoController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_ENDERECORETRIEVEREQUEST,
    output_type=_ENDERECO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='endereco.EnderecoController.Update',
    index=3,
    containing_service=None,
    input_type=_ENDERECO,
    output_type=_ENDERECO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='endereco.EnderecoController.Destroy',
    index=4,
    containing_service=None,
    input_type=_ENDERECO,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENDERECOCONTROLLER)

DESCRIPTOR.services_by_name['EnderecoController'] = _ENDERECOCONTROLLER

# @@protoc_insertion_point(module_scope)