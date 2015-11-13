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

from subprocess import Popen

import skema.tag
from skema.utils import log_line
from skema.utils import log_result
from skema.utils import log_api

class tag_OMX_StopSubProcess(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('alias')

        log_api ("%s '%s'" \
            % (element.tag, alias))

        pid = context.subprocesses[alias].pid
        context.subprocesses[alias].terminate()
        del context.subprocesses[alias]

        log_line ()
        msg = "Stopped sub-process '" + alias + "' with PID " + str(pid)
        log_result (msg, "OMX_ErrorNone")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_StopSubProcess")
