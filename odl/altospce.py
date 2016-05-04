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
        return response

    def parse_response(self, output_src_dst, output_dst_src):
        """
        Parse the response from RPC.
        """
        result_src_dst = output_src_dst["output"]
        result_dst_src = output_dst_src["output"]
        result = {"error-code": "ERROR"}
        if result_dst_src["error-code"] == "OK" and result_dst_src["error-code"] == "OK":
            result["error-code"] = "OK"
            if "path" in result_src_dst.keys() and "path" in result_dst_src.keys():
                result["path"] = [result_src_dst["path"], result_dst_src["path"]]
        return result

    def path_setup(self, src, dst, objective_metrics=[] , constraint_metric=[]):
        """
        Setup a round-trip path between source ip and destination ip.
        """
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
        return self.parse_response(self.setup_request(data_dst_src),
                              self.setup_request(data_src_dst))

    def path_remove(self, path):
        """
        Remove a round trip.
        """
        data = json.dumps({"input": {"path": path[0]}})
        response_src_dst = self.remove_request(data)
        data = json.dumps({"input": {"path": path[1]}})
        response_dst_src = self.remove_request(data)
        return self.parse_response(response_src_dst, response_dst_src)

    def get_path(self, src, dst):
        """
        Query a path between source ip and destination ip.
        """
        pass

    def set_tc(self, src, dst, bd, bs):
        """
        Traffic controlling for the path between source ip and destination ip.
        """
        pass
