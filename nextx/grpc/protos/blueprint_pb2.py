# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blueprint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x62lueprint.proto\x12\nblueprints\"v\n\x0cItemMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07pattern\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x0e\n\x0c_descriptionB\n\n\x08_pattern\"X\n\x10ItemNomenclature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\x9e\x02\n\tCheckItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x05order\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x10\n\x03min\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x10\n\x03max\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x11\n\x04\x64\x61te\x18\x05 \x01(\x03H\x03\x88\x01\x01\x12\x12\n\x05\x61lias\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x13\n\x06\x61\x63tive\x18\x07 \x01(\x08H\x05\x88\x01\x01\x12*\n\x08metadata\x18\x08 \x03(\x0b\x32\x18.blueprints.ItemMetadata\x12+\n\x05items\x18\t \x03(\x0b\x32\x1c.blueprints.ItemNomenclatureB\x08\n\x06_orderB\x06\n\x04_minB\x06\n\x04_maxB\x07\n\x05_dateB\x08\n\x06_aliasB\t\n\x07_active\"3\n\x07\x44\x61yPart\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\"?\n\x05State\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\xd3\x03\n\tBlueprint\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\x05owner\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06output\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0cpublished_at\x18\x06 \x01(\x03H\x03\x88\x01\x01\x12\x1f\n\x12published_pilot_at\x18\x07 \x01(\x03H\x04\x88\x01\x01\x12\x13\n\x06\x61\x63tive\x18\x08 \x01(\x08H\x05\x88\x01\x01\x12\x1d\n\x10temperature_unit\x18\t \x01(\tH\x06\x88\x01\x01\x12%\n\x05state\x18\n \x01(\x0b\x32\x11.blueprints.StateH\x07\x88\x01\x01\x12*\n\rday_part_info\x18\x0b \x03(\x0b\x32\x13.blueprints.DayPart\x12*\n\x0b\x63heck_items\x18\x0c \x03(\x0b\x32\x15.blueprints.CheckItemB\x08\n\x06_ownerB\x0e\n\x0c_descriptionB\t\n\x07_outputB\x0f\n\r_published_atB\x15\n\x13_published_pilot_atB\t\n\x07_activeB\x13\n\x11_temperature_unitB\x08\n\x06_state\"0\n\"BusinessUnitActiveBlueprintRequest\x12\n\n\x02id\x18\x01 \x01(\t\"l\n#BusinessUnitActiveBlueprintResponse\x12\x32\n\x0e\x61\x63tive_project\x18\x01 \x01(\x0b\x32\x15.blueprints.BlueprintH\x00\x88\x01\x01\x42\x11\n\x0f_active_project\"+\n\x1d\x42usinessUnitBlueprintsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"I\n\x1e\x42usinessUnitBlueprintsResponse\x12\'\n\x08projects\x18\x01 \x03(\x0b\x32\x15.blueprints.Blueprint2\x84\x02\n\x10\x42lueprintService\x12x\n\x15GetActiveProjectForBU\x12..blueprints.BusinessUnitActiveBlueprintRequest\x1a/.blueprints.BusinessUnitActiveBlueprintResponse\x12v\n\x1dGetBusinessUnitActiveProjects\x12).blueprints.BusinessUnitBlueprintsRequest\x1a*.blueprints.BusinessUnitBlueprintsResponseb\x06proto3')



_ITEMMETADATA = DESCRIPTOR.message_types_by_name['ItemMetadata']
_ITEMNOMENCLATURE = DESCRIPTOR.message_types_by_name['ItemNomenclature']
_CHECKITEM = DESCRIPTOR.message_types_by_name['CheckItem']
_DAYPART = DESCRIPTOR.message_types_by_name['DayPart']
_STATE = DESCRIPTOR.message_types_by_name['State']
_BLUEPRINT = DESCRIPTOR.message_types_by_name['Blueprint']
_BUSINESSUNITACTIVEBLUEPRINTREQUEST = DESCRIPTOR.message_types_by_name['BusinessUnitActiveBlueprintRequest']
_BUSINESSUNITACTIVEBLUEPRINTRESPONSE = DESCRIPTOR.message_types_by_name['BusinessUnitActiveBlueprintResponse']
_BUSINESSUNITBLUEPRINTSREQUEST = DESCRIPTOR.message_types_by_name['BusinessUnitBlueprintsRequest']
_BUSINESSUNITBLUEPRINTSRESPONSE = DESCRIPTOR.message_types_by_name['BusinessUnitBlueprintsResponse']
ItemMetadata = _reflection.GeneratedProtocolMessageType('ItemMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ITEMMETADATA,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.ItemMetadata)
  })
_sym_db.RegisterMessage(ItemMetadata)

ItemNomenclature = _reflection.GeneratedProtocolMessageType('ItemNomenclature', (_message.Message,), {
  'DESCRIPTOR' : _ITEMNOMENCLATURE,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.ItemNomenclature)
  })
_sym_db.RegisterMessage(ItemNomenclature)

CheckItem = _reflection.GeneratedProtocolMessageType('CheckItem', (_message.Message,), {
  'DESCRIPTOR' : _CHECKITEM,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.CheckItem)
  })
_sym_db.RegisterMessage(CheckItem)

DayPart = _reflection.GeneratedProtocolMessageType('DayPart', (_message.Message,), {
  'DESCRIPTOR' : _DAYPART,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.DayPart)
  })
_sym_db.RegisterMessage(DayPart)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.State)
  })
_sym_db.RegisterMessage(State)

Blueprint = _reflection.GeneratedProtocolMessageType('Blueprint', (_message.Message,), {
  'DESCRIPTOR' : _BLUEPRINT,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.Blueprint)
  })
_sym_db.RegisterMessage(Blueprint)

BusinessUnitActiveBlueprintRequest = _reflection.GeneratedProtocolMessageType('BusinessUnitActiveBlueprintRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUSINESSUNITACTIVEBLUEPRINTREQUEST,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.BusinessUnitActiveBlueprintRequest)
  })
_sym_db.RegisterMessage(BusinessUnitActiveBlueprintRequest)

BusinessUnitActiveBlueprintResponse = _reflection.GeneratedProtocolMessageType('BusinessUnitActiveBlueprintResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUSINESSUNITACTIVEBLUEPRINTRESPONSE,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.BusinessUnitActiveBlueprintResponse)
  })
_sym_db.RegisterMessage(BusinessUnitActiveBlueprintResponse)

BusinessUnitBlueprintsRequest = _reflection.GeneratedProtocolMessageType('BusinessUnitBlueprintsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUSINESSUNITBLUEPRINTSREQUEST,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.BusinessUnitBlueprintsRequest)
  })
_sym_db.RegisterMessage(BusinessUnitBlueprintsRequest)

BusinessUnitBlueprintsResponse = _reflection.GeneratedProtocolMessageType('BusinessUnitBlueprintsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUSINESSUNITBLUEPRINTSRESPONSE,
  '__module__' : 'blueprint_pb2'
  # @@protoc_insertion_point(class_scope:blueprints.BusinessUnitBlueprintsResponse)
  })
_sym_db.RegisterMessage(BusinessUnitBlueprintsResponse)

_BLUEPRINTSERVICE = DESCRIPTOR.services_by_name['BlueprintService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ITEMMETADATA._serialized_start=31
  _ITEMMETADATA._serialized_end=149
  _ITEMNOMENCLATURE._serialized_start=151
  _ITEMNOMENCLATURE._serialized_end=239
  _CHECKITEM._serialized_start=242
  _CHECKITEM._serialized_end=528
  _DAYPART._serialized_start=530
  _DAYPART._serialized_end=581
  _STATE._serialized_start=583
  _STATE._serialized_end=646
  _BLUEPRINT._serialized_start=649
  _BLUEPRINT._serialized_end=1116
  _BUSINESSUNITACTIVEBLUEPRINTREQUEST._serialized_start=1118
  _BUSINESSUNITACTIVEBLUEPRINTREQUEST._serialized_end=1166
  _BUSINESSUNITACTIVEBLUEPRINTRESPONSE._serialized_start=1168
  _BUSINESSUNITACTIVEBLUEPRINTRESPONSE._serialized_end=1276
  _BUSINESSUNITBLUEPRINTSREQUEST._serialized_start=1278
  _BUSINESSUNITBLUEPRINTSREQUEST._serialized_end=1321
  _BUSINESSUNITBLUEPRINTSRESPONSE._serialized_start=1323
  _BUSINESSUNITBLUEPRINTSRESPONSE._serialized_end=1396
  _BLUEPRINTSERVICE._serialized_start=1399
  _BLUEPRINTSERVICE._serialized_end=1659
# @@protoc_insertion_point(module_scope)
