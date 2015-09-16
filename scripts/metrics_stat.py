import httplib2
import requests
import json
import sys
from requests.exceptions import ConnectionError

# Connect to the ODL Controller
# Return a JSON object
def ODLConnect(url, user, pas):
    try:
        r = requests.get(url, auth=(user, pas))
        decoded = json.loads(r.text)
        return decoded
    except ConnectionError as e:
        print ("Error to Connect at: ", url)
        print e
        return -1

# Receives a JSON ODL object and the Switch
# Returns the sum of byte count and packet count for each flow
def SUMFlowAgg(jobj,switch):
    
    aggFlowByte=0;
    aggFlowPacket=0;
    
    for key in jobj['nodes']['node']:
        if key['flow-node-inventory:serial-number'] == switch:
            for keyA in key['flow-node-inventory:table']:
                for keyB in keyA['opendaylight-flow-statistics:aggregate-flow-statistics']:
                    if keyB == 'byte-count':
                        aggFlowByte = aggFlowByte + keyA['opendaylight-flow-statistics:aggregate-flow-statistics'][keyB]
                    if keyB == 'packet-count':
                        aggFlowPacket = aggFlowPacket + keyA['opendaylight-flow-statistics:aggregate-flow-statistics'][keyB]
        else:
            next

    return (aggFlowByte, aggFlowPacket)

# Receives a JSON ODL object and the Switch
# Returns the Aggregate available in switch
#def FlowAggr(jobj,switch):
#
#    for key in jobj['nodes']['node']:
#        if key['flow-node-inventory:serial-number'] == switch:




obj = ODLConnect("http://131.215.207.57:8080/restconf/operational/opendaylight-inventory:nodes/", "admin", "admin")
by, cnt = SUMFlowAgg(obj,"QTFCA61380001")
print by
print cnt
#print 'Switch: QTFCA61380001, Bytes: %d, Packets: %d' % by, cnt

#Metric(obj,"flow-node-inventory:description")
