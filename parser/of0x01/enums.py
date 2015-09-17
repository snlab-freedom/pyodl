class GenericEnum(object):
    def get_name(self, value):
        for p, v in vars(self.__class__).iteritems():
            if v == value:
                return p
        return "UNKNOWN"


class OFPType(GenericEnum):
    """
    Message Type
    """
    # Symetric/Immutable messages
    OFPT_HELLO = 0
    OFPT_ERROR = 1
    OFPT_ECHO_REQUEST = 2
    OFPT_ECHO_REPLY = 3
    OFPT_VENDOR = 4

    # Switch configuration messages
    # Controller/Switch messages
    OFPT_FEATURES_REQUEST = 5
    OFPT_FEATURES_REPLY = 6
    OFPT_GET_CONFIG_REQUEST = 7
    OFPT_GET_CONFIG_REPLY = 8
    OFPT_SET_CONFIG = 9

    # Async messages
    OFPT_PACKET_IN = 10
    OFPT_FLOW_REMOVED = 11
    OFPT_PORT_STATUS = 12

    # Controller command messages
    # Controller/switch message
    OFPT_PACKET_OUT = 13
    OFPT_FLOW_MOD = 14
    OFPT_PORT_MOD = 15

    # Statistics messages
    # Controller/Switch message
    OFPT_STATS_REQUEST = 16
    OFPT_STATS_REPLY = 17

    # Barrier messages
    # Controller/Switch message
    OFPT_BARRIER_REQUEST = 18
    OFPT_BARRIER_REPLY = 19

    # Queue Configuration messages
    # Controller/Switch message
    OFPT_QUEUE_GET_CONFIG_REQUEST = 20
    OFPT_QUEUE_GET_CONFIG_REPLY = 21

class OFPErrorType(GenericEnum):
    """
    Error Type
    """
    OFPET_HELLO_FAILED = 0     # Hello protocol failed.
    OFPET_BAD_REQUEST = 1      # Request was not understood.
    OFPET_BAD_ACTION = 2       # Error in action description.
    OFPET_FLOW_MOD_FAILED = 3  # Problem modifying flow entry.
    OFPET_PORT_MOD_FAILED = 4  # Port mod request failed.
    OFPET_QUEUE_OP_FAILED = 5  # Queue operation failed.


