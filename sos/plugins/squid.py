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
import os

class squid(sos.plugintools.PluginBase):
    """squid related information
    """

    optionList = [("logsize", "max size (MiB) to collect per syslog file", "", 15)]

    def checkenabled(self):
        self.files = [ "/etc/squid/squid.conf" ]
        self.packages = [ "squid" ]
        return sos.plugintools.PluginBase.checkenabled(self)

    def setup(self):
        self.addCopySpec("/etc/squid/squid.conf")
        logsize = self.getOption("logsize")
                              sizelimit = logsize)  
        self.addCopySpecLimit("/var/log/sqid/access.log",
                              sizelimit = logsize)  
        self.addCopySpecLimit("/var/log/sqid/cache.log",
                              sizelimit = logsize)  
        self.addCopySpecLimit("/var/log/sqid/squid.out",
                              sizelimit = logsize)  
        return

