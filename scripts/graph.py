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

import networkx as nx
import os
import sys

if __name__ == "__main__":
    try:
        server = os.environ["ODL_URL"]
        user = os.environ["ODL_USER"]
        password = os.environ["ODL_PASS"]
    except KeyError:
        print "Please provide all environment vairables."
        print "Read the README.md for more information."
        sys.exit(1)

    credentials = (user, password)

    odl = ODLInstance(server, credentials)
    topology = ODLTopology(server, credentials, odl)
    links = topology.get_links()
    tp_nodes = topology.get_nodes()

    graph = nx.Graph()

    # Add all nodes
    for node in tp_nodes:
        graph.add_node(node['node-id'])

    # Add all edges
    for link in links:
        source = link['source']['source-node']
        destination = link['destination']['dest-node']
        graph.add_edge(source, destination)

    # Get the shortest path between two nodes
    node1 = "host:00:02:c9:42:68:40"
    node2 = "host:00:02:c9:42:69:c0"
    try:
        print nx.shortest_path(graph, node1, node2)
    except nx.exception.NetworkXError as e:
        print "ERROR", e
