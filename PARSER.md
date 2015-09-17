# Parsing OpenFlow messages

This parser is not completed. But at least you can parse OF1.0 Error Messages
(Most important message during debbuging).

If you have a tcpdump/wireshark raw bytes file, it is very easy to parse.

Here is a example of OF1.0 Error Message Packet:

```
$ hexdump -C /tmp/of_file
00000000  01 01 00 54 00 00 11 ec  00 03 00 04 01 0e 00 48  |...T...........H|
00000010  00 00 11 ec 00 32 20 ce  00 00 00 00 00 00 00 00  |.....2 .........|
00000020  00 00 00 00 00 00 ff ff  00 00 08 00 00 06 00 00  |................|
00000030  00 00 00 00 0a 00 00 01  00 00 00 00 00 00 00 00  |................|
00000040  00 00 00 0a 00 00 00 00  00 00 00 c8 ff ff ff ff  |................|
00000050  ff ff 00 00                                       |....|
00000054
```

And here how you should parse:

```python
from parser.of0x01.messages import OFPError

error = OFPError()
fp = file('/tmp/of_file')
error.unpack_from(fp.read())
print error.type.value, error.code.value
3 4
```

Following the OF1.0 Specification, type 3 is `OFPET_FLOW_MOD_FAILED`, and for
this type, code 4 is `OFPFMFC_BAD_COMMAND`.
