# Copyright (C) 2011-2014 Aratelia Limited - Juan A. Rubio
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

from skema.omxil12 import get_string_from_il_enum
from skema.omxil12 import OMX_TeardownTunnel

from skema.utils import log_api
from skema.utils import log_result


class tag_OMX_TeardownTunnel(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        outcomp = element.get('outcomp')
        outcompname = context.cnames[outcomp]
        outport = element.get('outport')

        incomp = element.get('incomp')
        incompname = context.cnames[incomp]
        inport = element.get('inport')
        log_api ("%s '%s:Port-%d' <->  '%s:Port-%d'" \
                       % (element.tag, outcompname, \
                              int(outport), incompname, int(inport)))
        outhdl = context.handles[outcomp]
        inhdl  = context.handles[incomp]

        if (outhdl != None and inhdl != None):
            omxerror = OMX_TeardownTunnel(outhdl, int(outport), inhdl, int(inport))
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")

            log_result (element.tag, err)

            if (err == "OMX_ErrorNone"):
                return 0
            else:
                return interror

        else:
            log_result (element.tag, "OMX_ErrorUndefined")
            return get_il_enum_from_string("OMX_ErrorUndefined")

tagobj = skema.tag.SkemaTag(tagname="OMX_TeardownTunnel")
