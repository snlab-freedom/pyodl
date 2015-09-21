import httplib2
import requests
import json
import sys
import os
from requests.exceptions import ConnectionError

# Connect to the ODL Controller
# Return a JSON object
def odl_connect(url, user, pas):
    try:
        r = requests.get(url, auth=(user, pas))
        decoded = json.loads(r.text)
        return decoded
    except ConnectionError as e:
        print ("Error to Connect at: ", url)
        print e
        return -1

# Receives a JSON ODL object and the Switch
# Returns Aggregate metrics (bytes and pkt count) for each table
def sum_flowagg(jobj,switch):

    aggflowbyte=0;
    aggflowpacket=0;

    for key in jobj['nodes']['node']:
        if key['flow-node-inventory:serial-number'] == switch:
            for keyA in key['flow-node-inventory:table']:
                for keyB in keyA['opendaylight-flow-statistics:aggregate-flow-statistics']:
                    if keyB == 'byte-count':
                        aggflowbyte = aggflowbyte + keyA['opendaylight-flow-statistics:aggregate-flow-statistics'][keyB]
                    if keyB == 'packet-count':
                        aggflowpacket = aggflowpacket + keyA['opendaylight-flow-statistics:aggregate-flow-statistics'][keyB]
        else:
            next

    return (aggflowbyte, aggflowpacket)

# Receives a JSON ODL object and the Switch
# Returns the sum of bytes and pkts count for each flow to compare against Aggregate
def sum_flowmetric(jobj,switch):




## Main
try:
    server = os.environ["ODL_URL"]
    user = os.environ["ODL_USER"]
    password = os.environ["ODL_PASS"]
except KeyError:
    print "Please provide all environment vairables."
    print "Read the README.md for more information."
    sys.exit(1)

#credentials = (user, password)
obj = odl_connect(server, user, password)
by, cnt = sum_flowagg(obj,"QTFCA61380001")
print by
print cnt
#print 'Switch: QTFCA61380001, Bytes: %d, Packets: %d' % by, cnt

#Metric(obj,"flow-node-inventory:description")
