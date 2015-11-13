# Copyright (C) 2011-2015 Aratelia Limited - Juan A. Rubio
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

import os
import re
import pwd
import skema.tag

from skema.utils import log_api
from skema.utils import log_result


class tag_OMX_BaseProfilePort(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias        = element.get('alias')
        name         = context.cnames[alias]
        portstr      = element.get('port')
        allocatorstr = element.get('allocator')
        modestr      = element.get('mode')
        uristr       = element.get('uri')

        # Replace '$USER' and '$HOME' strings wih the actual representations
        uristr = re.sub("\$USER", pwd.getpwuid(os.getuid())[0], uristr, 1)
        uristr = re.sub("\$HOME", pwd.getpwuid(os.getuid())[5], uristr, 1)

        log_api ("%s %s:Port-%d' 'Allocator:%s' 'Mode:%s' 'Uri:%s'" \
                     % (element.tag, name, int(portstr),           \
                            allocatorstr, modestr, uristr))

        context.base_profile_mgr.manage_port(alias, portstr, allocatorstr,
                                             modestr, uristr)

        log_result (element.tag, "OMX_ErrorNone")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_BaseProfilePort")
