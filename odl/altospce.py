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
    def __init__(self, odl_instance):
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

    def get_path_request(self, data):
        endpoint = "/restconf/operations/alto-spce:get-path"
        response = self.odl_instance.post(endpoint,
                                          data = data)
        return response

    def parse_response(self, *output):
        """
        Parse the response from RPC.
        """
        result_src_dst = output_src_dst["output"]
        result_dst_src = output_dst_src["output"]
        result = {"error-code": "OK"}
        for r in output:
            if r['output']['error-code'] != 'OK':
                result['error-code'] = 'ERROR'
                break
        if result['error-code'] == 'OK':
            paths = []
            for r in output:
                paths.append(r['output']['path'])
            result['path'] = paths
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
        response = []
        for p in path:
            data = json.dump({"input": {"path": p}})
            response.append(self.remove_request(data))
        return self.parse_response(*response)

    def get_path(self, src, dst):
        """
        Query a path between source ip and destination ip.
        """
        data = json.dumps({"input": {"endpoint": {"src": src, "dst": dst}}})
        response = self.get_path_request(data)
        return response["output"]

    def get_all_paths(self):
        """
        Query all existing paths set by spce.
        """
        paths = []
        hosts = self.get_all_hosts()
        pairs = [(src, dst) for src in hosts for dst in hosts if src != dst]
        for src, dst in pairs:
            response = self.get_path(src, dst)
            if response["error-code"] == "OK":
                path = {}
                path['path'] = response['path']
                if 'bandwidth' in response.keys():
                    path['tc'] = response['bandwidth']
                paths.append(path)
        return paths

    def get_all_hosts(self):
        hosts = set()
        nodes = self.odl_instance.topology.get_nodes()
        for node in nodes.values():
            if node['node-id'].split(':')[0] == 'host':
                for addr in node['host-tracker-service:addresses']:
                    hosts.add(addr['ip'])
        return list(hosts)

    def parse_tc_response(self, response):
        result = {"error-code": "ERROR", "path": "NULL"}
        result_src_dst = response["output"]
        if result_src_dst["error-code"] == "OK":
            result["error-code"] = "OK"
            if "path" in result_src_dst.keys():
                result["path"] = result_src_dst["path"]
        return result

    def set_tc(self, src, dst, bd, bs):
        """
        Tc seting up, updating and removing are both one way!
        Traffic controlling for the path between source ip and destination ip.
        """
        endpoint = "/restconf/operations/alto-spce:rate-limiting-setup"
        data_src_dst = json.dumps({
            "input": {
                "endpoint": {
                    "src": src,
                    "dst": dst
                },
                "limited-rate": bd,
                "burst-size": bs
            }
        })
        response = self.odl_instance.post(endpoint= endpoint,
                                          data = data_src_dst)
        return self.parse_tc_response(response)

    def update_tc(self, src, dst, bd, bs):
        """
        Tc seting up, updating and removing are both one way!
        Update traffic controlling for the path between source ip and destination ip
        """
        endpoint = "/restconf/operations/alto-spce:rate-limiting-update"
        data_src_dst = json.dumps({
            "input": {
                "endpoint": {
                    "src": src,
                    "dst": dst
                },
                "limited-rate": bd,
                "burst-size": bs
            }
        })
        response = self.odl_instance.post(endpoint = endpoint,
                                          data = data_src_dst)
        return self.parse_tc_response(response)

    def remove_tc(self, path):
        """
        Tc seting up, updating and removing are both one way!
        """
        endpoint = "/restconf/operations/alto-spce:rate-limiting-remove"
        data = json.dumps({"input": {"path": path}})
        response = self.odl_instance.post(endpoint = endpoint,
                                          data = data)
        result = {"error-code": "ERROR"}
        result_src_dst = response["output"]
        if result_src_dst["error-code"] == "OK":
            result["error-code"] = "OK"
        return result

    def add_drop_meter(self, node_id, meter_id, bd, bs):
        endpoint = "/restconf/config/opendaylight-inventory:nodes/node/" \
                   + node_id + "/meter/" + str(meter_id)
        meter_data = json.dumps({
            "meter": {
                "meter-id": meter_id,
                "flags": "meter-kbps meter-burst",
                "container-name": "altospce rate limiting container",
                "meter-name": "altospce rate limiting",
                "meter-band-headers": {
                    "meter-band-header": {
                        "band-id": 0,
                        "meter-band-types": {
                            "flags": "ofpmbt-drop"
                        },
                        "drop-rate": bd,
                        "drop-burst-size": bs
                    }
                }
            }
        })
        response = self.odl_instance.put(endpoint = endpoint,
                                         data = meter_data)

    def remove_drop_meter(self, node_id, meter_id):
        endpoint = "/restconf/config/opendaylight-inventory:nodes/node/" \
                   + node_id + "/meter/" + str(meter_id)
        response = self.odl_instance.delete(endpoint = endpoint)

    def get_bandwidth_topology(self):
        endpoint = "/restconf/operations/alto-spce:get-bandwidth-topology"
        response = self.odl_instance.post(endpoint)
        if response['error-code'] == 'OK':
            return {
                'tpid-map': json.loads(response['tpid-map']),
                'bandwidth-topology': json.loads(response['bandwidth-topology'])
            }
        else:
            return {
                'tpid-map': [],
                'bandwidth-topology': []
            }
