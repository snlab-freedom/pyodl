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

# NOTE! You dont need to specify the flow id and the table id.
#       This data is read from your raw xml file.

from odl.topology import ODLTopology
from odl.instance import ODLInstance
from odl.exceptions import NodeNotFound, TableNotFound

from of.flow import GenericFlow

from argparse import ArgumentParser

import os
import sys
import argparse

import xml.etree.ElementTree as ET

if __name__ == "__main__":
    try:
        server = os.environ["ODL_URL"]
        user = os.environ["ODL_USER"]
        password = os.environ["ODL_PASS"]
    except KeyError:
        print "Please provide all environment vairables."
        print "Read the README.md for more information."
        sys.exit(1)

    parser = ArgumentParser(description='Insert a flow in a table node.')

    parser.add_argument('-i',
                        '--input',
                        help='Input XML tempalte flow file',
                        nargs=1)
    parser.add_argument('-n',
                        '--node',
                        help='Node ID',
                        nargs=1)
    parser.add_argument('-t',
                        '--table',
                        help='Table ID',
                        nargs=1)


    args = parser.parse_args()

    if (args.input is None or
        args.node is None or
        args.table is None):
        parser.print_help()
        sys.exit(1)

    credentials = (user, password)
    odl = ODLInstance(server, credentials)

    try:
        # Get the node object
        node = odl.get_node_by_id(args.node[0])

        # Get the table object
        table = node.get_table_by_id(args.table[0])

        # Creates a generic flow object
        flow = GenericFlow(name = "teste", table = table)

        # Insert the flow
        table.put_flow_from_template(filename = args.input[0],
                                     flow = flow)

    except (IOError, NodeNotFound, TableNotFound) as e:
        print e
        sys.exit()
