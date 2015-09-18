# Curl

#### Getting table 0 of openflow:1 in /config/ data store:

```bash
$ curl -v -X GET -H "Accept: application/json" --user ${ODL_USER}:${ODL_PASS} \
      ${ODL_URL}/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/ | python -mjson.tool
```

#### Getting table 0 of openflow:1 in /operational/ data store:

```bash
$ curl -v -X GET -H "Accept: application/json" --user ${ODL_USER}:${ODL_PASS} \
      ${ODL_URL}/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0/ | python -mjson.tool
```
#### Inserting flow id 1 in table 0 of openflow:1 node:

```
$ curl -v -X PUT -H "Content-Type: application/xml" -H "Accept: application/json" --user ${ODL_USER:${ODL_PASS} \
  --data "@flows/sample01.xml" ${ODL_URL}/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1 | python -mjson.tool
```

*Note 1:* Replace openflow:1 with your node id.

*Note 2:* Flow id url must MATCH with the `flows/sample01.xml` file id.

*Note 3:* If you are trying to insert a new flow with the same id, please, first
remove the flow with a `DELETE` request. ODL ignores any FLOW MOD messages.

