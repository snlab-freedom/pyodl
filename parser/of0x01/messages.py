from parser.of0x01.structs import *
from parser.of0x01.consts import *
from parser.of0x01.enums import *
from parser.of0x01.types import *

class GenericMessage(GenericStruct):
    def __init__(self, *args, **kwargs):
        self.header = OFPHeader(type = self.Meta.msg_type)

class OFPHello(GenericMessage):
    class Meta:
        msg_type = OFPType.OFPT_HELLO
        build_order = ('header', 'body')

    def __init__(self, *args, **kwargs):
        self.body = UBInt8()
        super(OFPHello, self).__init__(*args, **kwargs)

class OFPError(GenericMessage):
    class Meta:
        msg_type = OFPType.OFPT_ERROR
        build_order = ('header', 'type', 'code')

    def __init__(self, *args, **kwargs):
        self.type = UBInt16()
        self.code = UBInt16()
        self.data = UBInt8()
        super(OFPError, self).__init__(*args, **kwargs)
