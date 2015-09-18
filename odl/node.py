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

from odl.connector import ODLConnector
from odl.table import ODLTable
from odl.exceptions import TableNotFound

class ODLNode(object):
    """
    This class represents a node (or a switch) in OpenDayLight.
    """
    def __init__(self, node, odl_instance):
        self.node = node
        self.odl_instance = odl_instance

    def __repr__(self):
        return "<ODLNode: %s>" % self.id

    @property
    def id(self):
        return self.node['id']

    @property
    def description(self):
        return self.node['flow-node-inventory:description']

    @property
    def ip_address(self):
        return self.node['flow-node-inventory:ip-address']

    @property
    def manufacturer(self):
        return self.node['flow-node-inventory:manufacturer']

    @property
    def serial_number(self):
        return self.node['flow-node-inventory:serial-number']

    @property
    def hardware(self):
        return self.node['flow-node-inventory:hardware']

    @property
    def software(self):
        return self.node['flow-node-inventory:software']

    def get_tables(self):
        tables = self.node['flow-node-inventory:table']
        result = {}
        for table in tables:
            obj = ODLTable(table, self)
            result[obj.id] = obj
        return result

    def get_table_by_id(self, id):
        tables = self.get_tables()
        try:
            return tables[int(id)]
        except KeyError:
            raise TableNotFound("Table %s not found" % id)

    def get_connectors(self):
        connectors = self.node['node-connector']
        result = {}
        for connector in connectors:
            obj = ODLConnector(connector, self)
            result[obj.id] = obj
        return result

    def get_connector_by_id(self, id):
        connectors = self.get_connectors()
        try:
            return connectors[id]
        except KeyError:
            return None

    def clear_flows(self):
        pass

    def remove_flow(self, flow):
        pass

    def add_flow(self, flow):
        pass
