# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/assay_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/assay_metadata.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\x1aga4gh/assay_metadata.proto\x12\x05ga4gh\x1a\x1cgoogle/protobuf/struct.proto\"\xc5\x03\n\nExperiment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1b\n\x13message_create_time\x18\x04 \x01(\t\x12\x1b\n\x13message_update_time\x18\x05 \x01(\t\x12\x10\n\x08run_time\x18\x06 \x01(\t\x12\x10\n\x08molecule\x18\x07 \x01(\t\x12\x10\n\x08strategy\x18\x08 \x01(\t\x12\x11\n\tselection\x18\t \x01(\t\x12\x0f\n\x07library\x18\n \x01(\t\x12\x16\n\x0elibrary_layout\x18\x0b \x01(\t\x12\x18\n\x10instrument_model\x18\x0c \x01(\t\x12\x1c\n\x14instrument_data_file\x18\r \x01(\t\x12\x19\n\x11sequencing_center\x18\x0e \x01(\t\x12\x15\n\rplatform_unit\x18\x0f \x01(\t\x12)\n\x04info\x18\x10 \x03(\x0b\x32\x1b.ga4gh.Experiment.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\"\xed\x01\n\x08\x41nalysis\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x0f\n\x07updated\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x10\n\x08software\x18\x07 \x03(\t\x12\'\n\x04info\x18\x08 \x03(\x0b\x32\x19.ga4gh.Analysis.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXPERIMENT_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='ga4gh.Experiment.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.Experiment.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.Experiment.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=521,
)

_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='ga4gh.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.Experiment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.Experiment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.Experiment.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_create_time', full_name='ga4gh.Experiment.message_create_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_update_time', full_name='ga4gh.Experiment.message_update_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run_time', full_name='ga4gh.Experiment.run_time', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='molecule', full_name='ga4gh.Experiment.molecule', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='ga4gh.Experiment.strategy', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selection', full_name='ga4gh.Experiment.selection', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='library', full_name='ga4gh.Experiment.library', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='library_layout', full_name='ga4gh.Experiment.library_layout', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument_model', full_name='ga4gh.Experiment.instrument_model', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument_data_file', full_name='ga4gh.Experiment.instrument_data_file', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencing_center', full_name='ga4gh.Experiment.sequencing_center', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_unit', full_name='ga4gh.Experiment.platform_unit', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='ga4gh.Experiment.info', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EXPERIMENT_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=521,
)


_ANALYSIS_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='ga4gh.Analysis.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.Analysis.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.Analysis.InfoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=521,
)

_ANALYSIS = _descriptor.Descriptor(
  name='Analysis',
  full_name='ga4gh.Analysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.Analysis.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.Analysis.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.Analysis.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='ga4gh.Analysis.created', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='ga4gh.Analysis.updated', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ga4gh.Analysis.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='software', full_name='ga4gh.Analysis.software', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='ga4gh.Analysis.info', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ANALYSIS_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=761,
)

_EXPERIMENT_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_EXPERIMENT_INFOENTRY.containing_type = _EXPERIMENT
_EXPERIMENT.fields_by_name['info'].message_type = _EXPERIMENT_INFOENTRY
_ANALYSIS_INFOENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_ANALYSIS_INFOENTRY.containing_type = _ANALYSIS
_ANALYSIS.fields_by_name['info'].message_type = _ANALYSIS_INFOENTRY
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['Analysis'] = _ANALYSIS

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXPERIMENT_INFOENTRY,
    __module__ = 'ga4gh.assay_metadata_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.Experiment.InfoEntry)
    ))
  ,
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'ga4gh.assay_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Experiment)
  ))
_sym_db.RegisterMessage(Experiment)
_sym_db.RegisterMessage(Experiment.InfoEntry)

Analysis = _reflection.GeneratedProtocolMessageType('Analysis', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _ANALYSIS_INFOENTRY,
    __module__ = 'ga4gh.assay_metadata_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.Analysis.InfoEntry)
    ))
  ,
  DESCRIPTOR = _ANALYSIS,
  __module__ = 'ga4gh.assay_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Analysis)
  ))
_sym_db.RegisterMessage(Analysis)
_sym_db.RegisterMessage(Analysis.InfoEntry)


_EXPERIMENT_INFOENTRY.has_options = True
_EXPERIMENT_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ANALYSIS_INFOENTRY.has_options = True
_ANALYSIS_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
