from ofp.consts import *
from ofp.enums import *
from ofp.types import *

class GenericStruct(object):
    def __init__(self, **kwargs):
        for a in kwargs:
            try:
                field = getattr(self, a)
                field.value = kwargs[a]
            except AttributeError:
                raise OFPException("Attribute error: %s" % a)

    def pack(self):
        hexa = ""
        for field in self.Meta.build_order:
            hexa += getattr(self, field).pack()
        return hexa

    def unpack_from(self, buff):
        begin = 0
        for field in self.Meta.build_order:
            size = getattr(self, field).get_size()
            getattr(self,field).unpack_from(buff, offset=begin)
            begin += size

    def get_size(self):
        tot = 0
        for field in self.Meta.build_order:
            tot += getattr(self, field).get_size()
        return tot


class OFPHeader(GenericStruct):
    class Meta:
        # TODO: Remove build_order attribute. To do that, we need
        # figure out how get attributes in defined order.
        build_order=('version', 'type', 'length', 'xid')

    def __init__(self, *args, **kwargs):
        self.version = UBInt8(OFP_VERSION)
        self.type = UBInt8(OFPType.OFPT_HELLO)
        self.length = UBInt16()
        self.xid = UBInt32()

        self.update_length()

        super(OFPHeader, self).__init__(*args, **kwargs)

    def update_length(self, length = None):
        self.length.value = length if length else self.get_size()
