## Copyright (C) 2013 Red Hat, Inc.

### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sos.plugintools


class openstack_heat(sos.plugintools.PluginBase):
    """openstack related information
    """

    optionList = [("log", "gathers openstack-heat logs", "slow", False)]

    packages = ('openstack-heat-api',
                'openstack-heat-api-cfn',
                'openstack-heat-api-cloudwatch',
                'openstack-heat-cli',
                'openstack-heat-common',
                'openstack-heat-engine',
                'python-heatclient')

    def setup(self):
        # Heat
        self.collectExtOutput(
            "heat-manage db_version",
            suggest_filename="heat_db_version")
        self.addCopySpec("/etc/heat/")
        self.addCopySpec("/var/log/heat/")


