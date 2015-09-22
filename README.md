# README

This is a python library and sample scripts to handle OpenDayLight instance.

## Installing

You need at least a python2.7 installed. Also install the python modules
dependencies:

```
 $ sudo pip install -r requirements.txt
```

## Running

First export the PYTHONPATH env:

```
 $ export PYTHONPATH=.:$PYTHONPATH
```

Also, you need to export the variables with the server address/port and your
credentials:

```
$ export ODL_URL="http://127.0.0.1:8080"
$ export ODL_USER="admin"
$ export ODL_PASS="admin"
```

## Examples

For examples, please visit the `scripts` folder.

## Web server

For SC15 demo we need a way to export the topology and nodes information.  For
this reason there is a `webserver` folder, where is a Flex webserver project.

If you would like to run the webserver, please execute:

```
$ python webserver/web.py
```

After that you should be able to point your browser to
`http://YOUR_SERVER:5000/`.

## Running queries from curl

To insert and remove flows, you can use this library (see `scripts` folder), but
if you need to test using curl directly please open `CURL.md`.

## Parsing OpenFlow messages

Please open `PARSER.md`.
