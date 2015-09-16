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

import json
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

#    # Add all nodes
#    for node in tp_nodes:
#        graph.add_node(node['node-id'])

    result = []
    # Add all edges
    for link in links:
        source = link['source']['source-node']
        target = link['destination']['dest-node']
        result.append({'source': source, 'target': target})

    print json.dumps(result)
