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

import os
import sys
import threading

from ctypes import *
from omxil12 import *

from skema.utils import log_line
from skema.utils import log_api
from skema.utils import log_result

from skema.config import get_config

def my_evt_hdler(a, b, c, d, e, f):
    evtstr = get_string_from_il_enum(c, "OMX_Event")
    config = get_config()
    name = str()
    name = config.cnames2[a]

    if (c == OMX_EventCmdComplete):
        config.cmdevents[a].set()
        cmdstr       = get_string_from_il_enum(d, "OMX_Command")
        if (d == OMX_CommandStateSet):
            statestr = get_string_from_il_enum(e, "OMX_State")
            log_line ()
            log_api("EventHandler '%s'" % (name))
            log_line ()
            log_line ("Received -> '%s' '%s' '%s'"  \
                            % (evtstr, cmdstr, statestr), 1)
    elif (c == OMX_EventBufferFlag):
        config.eosevents[a].set()
        log_line ()
        log_api("EventHandler '%s'"  % (name))
        log_line ()
        log_line ("Received -> '%s' Port '%d'"      \
                        % (evtstr, d), 1)
    elif (c == OMX_EventPortSettingsChanged):
        config.settings_changed_events[a].set()
        log_line ()
        log_api("EventHandler '%s'"  % (name))
        log_line ()
        log_line ("Received -> '%s' Port '%d'"      \
                        % (evtstr, d), 1)
    elif (c == OMX_EventError):
        interror     = int(d & 0xffffffff)
        log_line ()
        log_api("EventHandler '%s'"  % (name))
        log_line ()
        log_line ("Received -> '%s' '%s' Port '%d'" \
                  % (evtstr, get_string_from_il_enum(interror, "OMX_Error"), e), 1)
        if len(config.ignored_error_events) != 0:
            if interror in config.ignored_error_events[a]:
                log_line ("Ignored -> '%s' '%s' Port '%d'" \
                          % (evtstr, get_string_from_il_enum(interror, "OMX_Error"), e), 1)
            else:
                config.error_events[a].append(interror)
        else:
            config.error_events[a].append(interror)

    return 0

def my_ebd_cback(a, b, c):
    config = get_config()
    name   = config.cnames2[a]
    alias  = config.aliases[name]
    handle = config.handles[alias]
    config.base_profile_mgr.empty_buffer_done(handle,alias,c)
    return 0

def my_fbd_cback(a, b, c):
    config = get_config()
    name   = config.cnames2[a]
    alias  = config.aliases[name]
    handle = config.handles[alias]
    config.base_profile_mgr.fill_buffer_done(handle,alias,c)
    return 0
