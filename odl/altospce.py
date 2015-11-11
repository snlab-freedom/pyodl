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
#          - Xiao Lin <linxiao9292 AT outlook DOT com>
#
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import json

class ALTOSpce(object):
    """
    Request Wrapper for ALTO SPCE (Simple Path Computation Engine) module.
    """
    def __init__(self, server, credentials, odl_instance):
        self.server = server
        self.credentials = credentials
        self.odl_instance = odl_instance
        self.headers = { 'Content-type' : 'application/json' }

    def setup_request(self, data):
        endpoint = "/restconf/operations/alto-spce:alto-spce-setup"
        response = self.odl_instance.post(endpoint,
                                          data = data)
        return response

    def remove_request(self, data):
        endpoint = "/restconf/operations/alto-spce:alto-spce-remove"
        response = self.odl_instance.post(endpoint,
                                          data = data)

    def parse_response(output_data):
        """
        Parse the response from RPC.
        """
        result = json.loads(output_data)["output"]
        pass
        return result

    def path_to_str(path):
        """
        Convert the path object to string.
        """
        pass
        return ""

    def path_setup(self, src, dst, objective_metrics=[] , constraint_metric=[]):
        data_src_dst = json.dumps({
            "input": {
                "endpoint": {
                    "src": src,
                    "dst": dst
                },
                "objective-metrics": objective_metrics,
                "constraint-metric": constraint_metric
            }
        })
        result = parse_response(self.setup_request(data_src_dst))
        data_dst_src = json.dumps({
            "input": {
                "endpoint": {
                    "src": dst,
                    "dst": src
                },
                "objective-metrics": objective_metrics,
                "constraint-metric": constraint_metric
            }
        })
        result = parse_response(self.setup_request(data_dst_src))

    def path_remove(self, path):
        data = json.dumps({"input": {"path": path_to_str(path)}})
        self.remove_request(data)
