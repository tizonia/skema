# Copyright (C) 2011-2013 Aratelia Limited - Juan A. Rubio
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


class tag_OMX_ExpectEvent(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('comp')
        name = context.cnames[alias]
        evtstr = element.get('evt')
        ndata1str = element.get('ndata1')
        ndata2str = element.get('ndata2')
        timeoutstr = element.get('timeout')
        log_api ("%s '%s' '%s' '%s' '%s'" \
            % (element.tag, name, evtstr, ndata1str, ndata2str))
        handle = context.handles[alias]
        evt = get_il_enum_from_string(evtstr)
        #ndata1 = get_il_enum_from_string(ndata1str)

        if (handle != None):
            if (evt == OMX_EventCmdComplete):
                if (context.cmdevents[handle.value].is_set()):
                    context.cmdevents[handle.value].clear()
                    log_line ()
                    log_line ("%s '%s' '%s' '%s' was received OK"     \
                                    % (element.tag, name, evtstr, ndata2str), 1)
                else:
                    log_line ()
                    log_line ("%s Waiting for '%s' '%s' from '%s'"    \
                                    % (element.tag, evtstr, ndata2str, name), 1)
                    context.cmdevents[handle.value].wait(int(timeoutstr))
                    if (context.cmdevents[handle.value].is_set()):
                        log_line ()
                        log_line ("%s '%s' '%s' '%s' received OK"     \
                                      % (element.tag, name, evtstr, ndata2str))
                    else:
                        msg = element.tag + " '" + name + "' " + " '" \
                            + evtstr + "' " + ndata2str + "'"
                        log_line ()
                        log_result (msg, "OMX_ErrorTimeout")
                        return get_il_enum_from_string("OMX_ErrorTimeout")

            elif (evt == OMX_EventBufferFlag):
                if (context.eosevents[handle.value].is_set()):
                    context.eosevents[handle.value].clear()
                    log_line ()
                    log_line ("%s '%s' '%s' was received OK"          \
                                    % (element.tag, name, evtstr), 1)
                else:
                    log_line ()
                    log_line ("%s Waiting for '%s' from '%s'"         \
                                    % (element.tag, evtstr, name), 1)
                    context.eosevents[handle.value].wait(int(timeoutstr))
                    if (context.eosevents[handle.value].is_set()):
                        log_line ()
                        log_line ("%s '%s' '%s' received OK"          \
                                        % (element.tag, name, evtstr))
                    else:
                        msg = element.tag + " '" + name + "' " + " '" \
                            + evtstr + "'"
                        log_line ()
                        log_result (msg, "OMX_ErrorTimeout")
                        return get_il_enum_from_string("OMX_ErrorTimeout")

            elif (evt == OMX_EventPortSettingsChanged):
                if (context.settings_changed_events[handle.value].is_set()):
                    context.settings_changed_events[handle.value].clear()
                    log_line ()
                    log_line ("%s '%s' '%s' was received OK"            \
                                    % (element.tag, name, evtstr), 1)
                else:
                    log_line ()
                    log_line ("%s Waiting for '%s' from '%s'"           \
                                    % (element.tag, evtstr, name), 1)
                    context.settings_changed_events[handle.value].      \
                        wait(int(timeoutstr))
                    if (context.settings_changed_events[handle.value].is_set()):
                        log_line ()
                        log_line ("%s '%s' '%s' received OK"            \
                                        % (element.tag, name, evtstr))
                    else:
                        msg = element.tag + " '" + name + "' " + " '" + \
                            evtstr + "'"
                        log_line ()
                        log_result (msg, "OMX_ErrorTimeout")
                        return get_il_enum_from_string("OMX_ErrorTimeout")
            else:
                log_line ()
                log_line ("Unhandled event %s" % (evtstr))
                return get_il_enum_from_string("OMX_ErrorNotImplemented")
        else:
            log_line ()
            log_line ("Unknown handle")
            return get_il_enum_from_string("OMX_ErrorUndefined")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_ExpectEvent")
