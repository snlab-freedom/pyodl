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
from odl.exceptions import ODL404, FlowNotFound

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
        """
        Queries the server and retrieve a updated table.
        """
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
        """
        Return a dict with all flows in operational endpoint (in this table).
        """
        try:
            flows = self.table['flow']
        except KeyError:
            flows = []

        result = {}
        for flow in flows:
            obj = ODLFlow(flow, self)
            result[obj.id] = obj
        return result

    def get_config_flows(self):
        """
        Return a dict with all flows in config endpoint (in this table).
        """
        try:
            flows = self.config_table['flow']
        except KeyError:
            flows = []

        result = {}
        for flow in flows:
            obj = ODLFlow(flow, self)
            result[obj.id] = obj
        return result

    def get_flow_by_id(self, id):
        """
        Return a flow from this table, based on id.
        """
        # For now, this is only used in config context.
        flows = self.get_config_flows()
        try:
            return flows[id]
        except KeyError:
            raise FlowNotFound("Flow id %s not found" % id)

    def put_flow_from_data(self, data, flow_id):
        """
        Insert a flow in this table (config endpoint) based on raw xml data.
        """
        odl_instance = self.node.odl_instance
        endpoint = self.config_endpoint + 'flow/' + flow_id
        return odl_instance.put(endpoint,
                                data=data,
                                content="application/xml")

    def delete_flows(self):
        """
        Delete all flows in this table (config endpoint).
        """
        flows = self.get_config_flows()
        for flow in flows.values():
           flow.delete()
