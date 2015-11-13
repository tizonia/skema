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

import skema.tag

from skema.omxil12 import get_il_enum_from_string
from skema.omxil12 import get_string_from_il_enum
from skema.omxil12 import OMX_SendCommand
from skema.omxil12 import OMX_CommandPortEnable 
from skema.omxil12 import OMX_CommandPortDisable 

from skema.utils import log_api
from skema.utils import log_result

#from ctypes import *


class tag_OMX_SendCommand(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('comp')
        name = context.cnames[alias]
        cmdstr = element.get('cmd')
        nparam1str = element.get('nparam1')
        cmddatastr = element.get('cmddata')
        log_api ("%s '%s' '%s' '%s' '%s'" \
                       % (element.tag, name, cmdstr, nparam1str, cmddatastr))
        handle = context.handles[alias]
        cmd = get_il_enum_from_string(cmdstr)
        if (cmd == OMX_CommandPortEnable or cmd == OMX_CommandPortDisable):
            # nParam1 is the port index to be enabled/disabled, not an enum
            nparam1 = int(nparam1str)
        else:
            nparam1 = get_il_enum_from_string(nparam1str)

        if (handle != None):
            context.cmdevents[handle.value].clear()
            omxerror = OMX_SendCommand(handle, cmd, nparam1, None)
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")

        log_result (element.tag + " '" + name + "'", err)

        if (err == "OMX_ErrorNone"):
            return 0
        else:
            return interror

tagobj = skema.tag.SkemaTag(tagname="OMX_SendCommand")
