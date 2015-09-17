from struct import pack, unpack_from, calcsize

class GenericType(object):
    def __init__(self, value = 0):
        self.value = value

    def pack(self):
        return pack(self.Meta.fmt, self.value)

    def unpack_from(self, buff, offset=0):
        self.value = unpack_from(self.Meta.fmt, buff, offset)[0]

    def get_size(self):
        return calcsize(self.Meta.fmt)


class UBInt8(GenericType):
    class Meta:
        fmt = ">B"


class UBInt16(GenericType):
    class Meta:
        fmt = ">H"


class UBInt32(GenericType):
    class Meta:
        fmt = ">I"


class UBInt64(GenericType):
    class Meta:
        fmt = ">Q"
