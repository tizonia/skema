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
from skema.event import *

from skema.utils import log_api
from skema.utils import log_result

from ctypes import *
from xml.etree.ElementTree import ElementTree as et

class tag_OMX_GetHandle(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        name = element.get('name')
        alias = element.get('alias')
        expectstr = element.get('expect', default='OMX_ErrorNone')
        context.cnames[alias] = name
        context.aliases[name] = alias

        log_api ("%s '%s' Expected '%s'" % (element.tag, name, expectstr))

        handle = OMX_HANDLETYPE()
        EVT_HDLER_TYPE = CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE,
                                   OMX_PTR, OMX_EVENTTYPE, OMX_U32, OMX_U32,
                                   OMX_PTR)
        EBD_CBACK_TYPE = CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE,
                                   OMX_PTR, POINTER(OMX_BUFFERHEADERTYPE))
        FBD_CBACK_TYPE = CFUNCTYPE(UNCHECKED(OMX_ERRORTYPE), OMX_HANDLETYPE,
                                   OMX_PTR, POINTER(OMX_BUFFERHEADERTYPE))

        context.cbacks.EventHandler = EVT_HDLER_TYPE(my_evt_hdler)
        context.cbacks.EmptyBufferDone = EBD_CBACK_TYPE(my_ebd_cback)
        context.cbacks.FillBufferDone = FBD_CBACK_TYPE(my_fbd_cback)

        omxerror = OMX_GetHandle(byref(handle), name, None,
                                 byref(context.cbacks))

        interror = int(omxerror & 0xffffffff)
        err = get_string_from_il_enum(interror, "OMX_Error")

        if (expectstr == err):
            if (interror == OMX_ErrorNone):
                context.handles[alias] = handle
                context.cnames2[handle.value] = name
                context.cmdevents[handle.value] = threading.Event()
                context.eosevents[handle.value] = threading.Event()
            else:
                context.handles[alias] = OMX_HANDLETYPE()

        log_result (element.tag, err)

tagobj = skema.tag.SkemaTag(tagname="OMX_GetHandle")
