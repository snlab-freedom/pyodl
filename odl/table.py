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

from odl.flow import ODLFlow
from odl.exceptions import ODL404

import json

class ODLTable(object):
    """
    This class represents a switch table in OpenDayLight.
    """
    def __init__(self, table, node):
        self.table = table
        self.config_table = {}
        self.node = node

        base = "/restconf/operational/opendaylight-inventory:nodes"
        self.endpoint = "%s/node/%s/table/%s/" % (base,
                                                  self.node.id,
                                                  self.id)

        self.config_endpoint = self.endpoint.replace("operational",
                                                     "config")

        # Update table json
        self.update()

    def __repr__(self):
        return "<ODLTable: %s>" % self.id

    @property
    def id(self):
        return self.table['id']

    def update(self):
        odl_instance = self.node.odl_instance
        result = odl_instance.get(self.endpoint)
        self.table = result['flow-node-inventory:table'][0]

        try:
            result = odl_instance.get(self.config_endpoint)
            self.config_table = result['flow-node-inventory:table'][0]
        except ODL404 as e:
            #print "DEBUG: Config for this table not found"
            pass

    def get_operational_flows(self):
        try:
            flows = self.table['flow']
        except KeyError:
            flows = []

        return map(lambda x: ODLFlow(x, self), flows)

    def get_config_flows(self):
        try:
            flows = self.config_table['flow']
        except KeyError:
            flows = []

        return map(lambda x: ODLFlow(x, self), flows)
