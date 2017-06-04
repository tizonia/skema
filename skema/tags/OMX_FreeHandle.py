# Copyright (C) 2011-2017 Aratelia Limited - Juan A. Rubio
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
from skema.omxil12 import OMX_FreeHandle

from skema.utils import log_api
from skema.utils import log_line
from skema.utils import log_result

class tag_OMX_FreeHandle(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('alias')
        log_api ("%s '%s'" \
                       % (element.tag, context.cnames[alias]))
        handle = context.handles[alias]
        if (handle != None):
            omxerror = OMX_FreeHandle(handle)
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")
            log_result (element.tag, err)
            if (err == "OMX_ErrorNone"):
                return 0
            else:
                return interror

        else:
            log_line ("%s -> '%s %s'" \
                % (element.tag, \
                       "Could not find handle for", context.cnames[alias]))
            return get_il_enum_from_string("OMX_ErrorUndefined")

tagobj = skema.tag.SkemaTag(tagname="OMX_FreeHandle")
