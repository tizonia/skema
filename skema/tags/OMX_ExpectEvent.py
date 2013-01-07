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

import sys
import skema.tag
import threading

from skema.omxil12 import *

from skema.utils import log_line
from skema.utils import log_api
from skema.utils import log_result

from ctypes import *
from xml.etree.ElementTree import ElementTree as et

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
                    log_line ("%s '%s' '%s' has already been received OK" \
                                    % (element.tag, name, evtstr), 1)
                else:
                    log_line ()
                    log_line ("%s Waiting for '%s' from '%s'" \
                                    % (element.tag, evtstr, name), 1)
                    context.cmdevents[handle.value].wait(int(timeoutstr))
                    if (context.cmdevents[handle.value].is_set()):
                        log_line ("%s '%s' '%s' has been received OK" \
                                        % (element.tag, name, evtstr))
                    else:
                        log_line
                        log_line ("%s '%s' '%s' TIMEDOUT" \
                                        % (element.tag, name, evtstr), 1)
            elif (evt == OMX_EventBufferFlag):
                if (context.eosevents[handle.value].is_set()):
                    context.eosevents[handle.value].clear()
                    log_line ()
                    log_line ("%s '%s' '%s' has already been received OK" \
                                    % (element.tag, name, evtstr), 1)
                else:
                    log_line ()
                    log_line ("%s Waiting for '%s' from '%s'" \
                                    % (element.tag, evtstr, name), 1)
                    context.eosevents[handle.value].wait(int(timeoutstr))
                    if (context.eosevents[handle.value].is_set()):
                        log_line ()
                        log_line ("%s '%s' '%s' has been received OK" \
                                        % (element.tag, name, evtstr))
                    else:
                        log_line ()
                        log_line ("%s '%s' '%s' TIMEDOUT" \
                                        % (element.tag, name, evtstr))
            elif (evt == OMX_EventPortSettingsChanged):
                if (context.eosevents[handle.value].is_set()):
                    context.eosevents[handle.value].clear()
                    log_line ()
                    log_line ("%s '%s' '%s' has already been received OK" \
                                    % (element.tag, name, evtstr), 1)
                else:
                    log_line ()
                    log_line ("%s Waiting for '%s' from '%s'" \
                                    % (element.tag, evtstr, name), 1)
                    context.eosevents[handle.value].wait(int(timeoutstr))
                    if (context.eosevents[handle.value].is_set()):
                        log_line ()
                        log_line ("%s '%s' '%s' has been received OK" \
                                        % (element.tag, name, evtstr))
                    else:
                        log_line ()
                        log_line ("%s '%s' '%s' TIMEDOUT" \
                                        % (element.tag, name, evtstr))

tagobj = skema.tag.SkemaTag(tagname="OMX_ExpectEvent")
