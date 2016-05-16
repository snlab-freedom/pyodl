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

from odl.exceptions import ODL404

import re

class ODLMeter(object):
    """
    This class represents a switch table in OpenDayLight.
    """
    def __init__(self, xml, table):
        self.xml = xml
        self.table = table
        self.active = False

    def __repr__(self):
        return "<ODLMeter: %s>" % self.id

    @property
    def id(self):
        return self.xml['meter-id']

    @property
    def flags(self):
        try:
            return self.xml['flags']
        except KeyError:
            return ""

    @property
    def meter_drop_info(self):
        try:
            meter_band_header = self.xml["meter-band-headers"]["meter-band-header"][0]
        except KeyError as e:
            meter_band_header = {}
        result = {}
        if meter_band_header == {}:
            return result
        else:
            flags_str = str(self.flags)
            if flags_str.find('meter-kbps') != -1:
                flags_str = "meter-kbps"
            result = {'drop-rate': meter_band_header["drop-rate"],
                      'band-burst-size': meter_band_header["drop-burst-size"],
                      'flags': flags_str}
        return result


    def _get_meter_stats(self):
        try:
            return self.xml['opendaylight-meter-statistics:meter-statistics']
        except KeyError:
            return {}
