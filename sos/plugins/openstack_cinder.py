## Copyright (C) 2009 Red Hat, Inc., Joey Boggs <jboggs@redhat.com>
## Copyright (C) 2012 Rackspace US, Inc., Justin Shepherd <jshepher@rackspace.com>
## Copyright (C) 2013 Red Hat, Inc., Flavio Percoco <fpercoco@redhat.com>
## Copyright (C) 2013 Red Hat, Inc., Jeremy Agee <jagee@redhat.com>

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

import os

import sos.plugintools


class openstack_cinder(sos.plugintools.PluginBase):
    """openstack cinder related information
    """

    optionList = [("log", "gathers openstack cinder logs", "slow", True),
                   ("db", "gathers openstack cinder db version", "slow", False)]

    packages = ('openstack-cinder',
                'python-cinder',
                'python-cinderclient')

    def setup(self):
        if self.getOption("db"):
            self.collectExtOutput("cinder-manage db version",
                         suggest_filename="cinder_db_version")

        self.addCopySpec("/etc/sudoers.d/cinder")
        self.addCopySpec("/etc/cinder/")

        if self.getOption("log"):
            self.addCopySpec("/var/log/cinder/")


