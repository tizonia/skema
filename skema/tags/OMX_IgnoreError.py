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

from skema.omxil12 import get_il_enum_from_string
from skema.omxil12 import OMX_EventCmdComplete
from skema.omxil12 import OMX_EventBufferFlag
from skema.omxil12 import OMX_EventPortSettingsChanged

from skema.utils import log_line
from skema.utils import log_result
from skema.utils import log_api


class tag_OMX_IgnoreError(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('comp')
        name = context.cnames[alias]
        errstr = element.get('err')
        ndata2str = element.get('ndata2')
        log_api ("%s '%s' '%s' '%s'" \
            % (element.tag, name, errstr, ndata2str))
        handle = context.handles[alias]
        err = get_il_enum_from_string(errstr)
        # TODO: Check we are receiving an error code
        #err = get_string_from_il_enum(interror, "OMX_Error")

        if (handle != None):
            context.ignored_error_events[handle.value].append(err)
        else:
            log_line ()
            log_line ("Unknown handle")
            return get_il_enum_from_string("OMX_ErrorUndefined")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_IgnoreError")
