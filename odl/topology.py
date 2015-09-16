#!/usr/bin/env python
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#          - Beraldo Leal <beraldo AT ncc DOT unesp DOT br>
#
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import json
import sys
import requests

#from odl.link import ODLLink

class ODLTopology(object):
    def __init__(self, server, credentials, odl_instance):
        self.server = server
        self.credentials = credentials
        self.odl_instance = odl_instance
        self.headers = { 'Content-type' : 'application/json' }

    def get_topology(self):
        endpoint = "/restconf/operational/network-topology:network-topology/"

        try:
            response = requests.get(self.server + endpoint,
                                    headers=self.headers,
                                    auth=self.credentials)
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)

        # Consider any status other than 2xx an error
        if not response.status_code // 100 == 2:
            print "Error: Unexpected response", format(response)
            sys.exit(2)

        return json.loads(response.text)['network-topology']['topology'][0]

    def get_nodes(self):
        topology = self.get_topology()
        return topology['node']

    def get_links(self):
        topology = self.get_topology()
        try:
            return topology['link']
        except KeyError:
            return []
#        for link in topology['link']:
#            yield ODLLink(link, self.odl_instance)
