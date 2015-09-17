from ofp.structs import *
from ofp.consts import *
from ofp.enums import *
from ofp.types import *

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
