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

from odl.topology import ODLTopology
from odl.instance import ODLInstance

if __name__ == "__main__":
    server = "http://131.215.207.90:8080"
    credentials = ("admin", "admin")

    odl = ODLInstance(server, credentials)
    nodes = odl.get_nodes()
    for node in nodes.values():
        print "Node:", node.id, node.description
        print "-"*80
        connectors = node.get_connectors()
        for connector in connectors.values():
            print "%40s %20s %20s" % (connector.id,
                                      connector.hardware_address,
                                      connector.name)
