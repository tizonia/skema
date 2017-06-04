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
from skema.omxil12 import OMX_EventPortFormatDetected

from skema.utils import log_line
from skema.utils import log_result
from skema.utils import log_api


class tag_OMX_ResetEvent(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('comp')
        name = context.cnames[alias]
        evtstr = element.get('evt')
        log_api ("%s '%s' '%s'" \
            % (element.tag, name, evtstr ))
        handle = context.handles[alias]
        evt = get_il_enum_from_string(evtstr)

        if (handle != None):
            if (evt == OMX_EventCmdComplete):
                context.cmdevents[handle.value].clear()

            elif (evt == OMX_EventBufferFlag):
                context.eosevents[handle.value].clear()

            elif (evt == OMX_EventPortSettingsChanged):
                context.settings_changed_events[handle.value].clear()

            elif (evt == OMX_EventPortFormatDetected):
                context.format_detected_events[handle.value].clear()

            else:
                log_line ()
                log_line ("Unhandled event %s" % (evtstr))
                return get_il_enum_from_string("OMX_ErrorNotImplemented")
        else:
            log_line ()
            log_line ("Unknown handle")
            return get_il_enum_from_string("OMX_ErrorUndefined")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_ResetEvent")
