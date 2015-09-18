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

class ODLFlow(object):
    """
    This class represents a switch table in OpenDayLight.
    """
    def __init__(self, flow, table):
        self.flow = flow
        self.table = table

    def __repr__(self):
        return "<ODLFlow: %s>" % self.id

    @property
    def id(self):
        return self.flow['id']

    @property
    def priority(self):
        return self.flow['priority']

    @property
    def idle_timeout(self):
        return self.flow['idle-timeout']

    @property
    def hard_timeout(self):
        return self.flow['hard-timeout']

    @property
    def cookie(self):
        return self.flow['cookie']

    def _get_flow_stats(self):
        try:
            return self.flow['opendaylight-flow-statistics:flow-statistics']
        except KeyError:
            return {}

    def get_byte_count(self):
        stats = self._get_flow_stats()
        try:
            return stats['byte-count']
        except KeyError:
            return None

    def get_packet_count(self):
        stats = self._get_flow_stats()
        try:
            return stats['packet-count']
        except KeyError:
            return None
