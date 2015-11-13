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
import shlex
from subprocess import Popen

import skema.tag
from skema.utils import log_line
from skema.utils import log_result
from skema.utils import log_api

class tag_OMX_StartSubProcess(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('alias')
        cmdlinestr = element.get('cmdline')

        # Replace '$USER' and '$HOME' strings wih the actual representations
        cmdlinestr = re.sub("\$USER", pwd.getpwuid(os.getuid())[0], cmdlinestr, 0)
        cmdlinestr = re.sub("\$HOME", pwd.getpwuid(os.getuid())[5], cmdlinestr, 0)

        log_api ("%s '%s' '%s'" \
            % (element.tag, alias, cmdlinestr))

        args = shlex.split(cmdlinestr)
        process = Popen(args)
        context.subprocesses[alias] = process

        log_line ()
        msg = "Started sub-process '" + alias + "' with PID " + str(context.subprocesses[alias].pid)
        log_result (msg, "OMX_ErrorNone")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_StartSubProcess")
