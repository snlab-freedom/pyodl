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
from odl.exceptions import NodeNotFound, TableNotFound, FlowNotFound

from argparse import ArgumentParser

import os
import sys
import argparse

if __name__ == "__main__":
    try:
        server = os.environ["ODL_URL"]
        user = os.environ["ODL_USER"]
        password = os.environ["ODL_PASS"]
    except KeyError:
        print "Please provide all environment vairables."
        print "Read the README.md for more information."
        sys.exit(1)

    parser = ArgumentParser(description='Delete a flow from table node.')
    parser.add_argument('-n', '--node', help='Node ID', nargs=1)
    parser.add_argument('-t', '--table', help='Table ID', nargs=1)
    parser.add_argument('-i', '--id', help='Flow ID', nargs=1)

    args = parser.parse_args()

    if (args.node is None or
        args.table is None or
        args.id is None):
        parser.print_help()
        sys.exit(1)

    credentials = (user, password)
    odl = ODLInstance(server, credentials)

    try:
        # Get the node object
        node = odl.get_node_by_id(args.node[0])

        # Get the table object
        table = node.get_table_by_id(args.table[0])

        # Get the flow object
        flow = table.get_flow_by_id(args.id[0])

        # Remove flow
        flow.delete()

    except (NodeNotFound, TableNotFound, FlowNotFound) as e:
        print e
        sys.exit()
