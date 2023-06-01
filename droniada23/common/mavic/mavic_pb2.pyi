from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Telemetry(_message.Message):
    __slots__ = ["altitude", "heading", "lat", "long"]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    altitude: float
    heading: float
    lat: float
    long: float
    def __init__(self, lat: _Optional[float] = ..., long: _Optional[float] = ..., heading: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...
