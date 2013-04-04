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

from skema.omxil12 import get_string_from_il_enum
from skema.omxil12 import get_il_enum_from_string
from skema.omxil12 import OMX_AUDIO_PORTDEFINITIONTYPE
from skema.omxil12 import OMX_VIDEO_PORTDEFINITIONTYPE
from skema.omxil12 import OMX_IMAGE_PORTDEFINITIONTYPE
from skema.omxil12 import OMX_OTHER_PORTDEFINITIONTYPE
from skema.omxil12 import OMX_GetParameter
from skema.omxil12 import OMX_SetParameter

from skema.utils import log_line
from skema.utils import log_api
from skema.utils import log_result

from ctypes import sizeof
from ctypes import byref

def decode_audio_portdef (param_struct, param2_type):
    log_line ("%s" % param2_type.__name__, 1)
    for name, _ in param2_type._fields_:
        if (name == "eEncoding"):
            encstr = get_string_from_il_enum (\
                getattr(param_struct.format.audio, name), \
                    "OMX_AUDIO_Coding")
            log_line ("%s -> '%s'" \
                          % (name, encstr),2)
        else:
            log_line ("%s -> '%s'" \
                          % (name, getattr(param_struct.format.audio, name)),2)


def decode_video_portdef (param_struct, param2_type):
    log_line ("%s" % param2_type.__name__, 1)
    for name, _ in param2_type._fields_:
        if (name == "eCompressionFormat"):
            encstr = get_string_from_il_enum (\
                getattr(param_struct.format.video, name), \
                    "OMX_VIDEO_Coding")
            log_line ("%s -> '%s'" \
                          % (name, encstr),2)
        elif (name == "eColorFormat"):
            encstr = get_string_from_il_enum (\
                getattr(param_struct.format.video, name), \
                    "OMX_COLOR_Format")
            log_line ("%s -> '%s'" \
                          % (name, encstr),2)
        else:
            log_line ("%s -> '%s'" \
                          % (name, getattr(param_struct.format.video, name)),2)


def decode_image_portdef (param_struct, param2_type):
    log_line ("%s" % param2_type.__name__, 1)
    for name, _ in param2_type._fields_:
        if (name == "eCompressionFormat"):
            encstr = get_string_from_il_enum (\
                getattr(param_struct.format.image, name), \
                    "OMX_IMAGE_Coding")
            log_line ("%s -> '%s'" \
                          % (name, encstr),2)
        elif (name == "eColorFormat"):
            encstr = get_string_from_il_enum (\
                getattr(param_struct.format.image, name), \
                    "OMX_COLOR_Format")
            log_line ("%s -> '%s'" \
                          % (name, encstr),2)
        else:
            log_line ("%s -> '%s'" \
                          % (name, getattr(param_struct.format.image, name)),2)

def encode_audio_portdef (param_struct, param2_type, element):
    for name, _ in param2_type._fields_:
        for name2, val2 in element.items():
            if (name2 == name):
                setattr(param_struct.format.audio, name, int(val2))


def encode_video_portdef (param_struct, param2_type, element):
    for name, _ in param2_type._fields_:
        for name2, val2 in element.items():
            if (name2 == name):
                setattr(param_struct.format.video, name, int(val2))


def encode_image_portdef (param_struct, param2_type, element):
    for name, _ in param2_type._fields_:
        for name2, val2 in element.items():
            if (name2 == name):
                setattr(param_struct.format.image, name, int(val2))


def encode_other_portdef (param_struct, param2_type, element):
    for name, _ in param2_type._fields_:
        for name2, val2 in element.items():
            if (name2 == name):
                setattr(param_struct.format.other, name, int(val2))


class tag_OMX_SetParameter(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        indexstr = element.get('index')
        alias = element.get('alias')
        name = context.cnames[alias]
        portstr = element.get('port')

        log_api ("%s '%s' '%s:Port-%d'" \
                        % (element.tag, indexstr, name, int(portstr)))

        handle = context.handles[alias]
        index = get_il_enum_from_string(indexstr)
        param_type = skema.omxil12.__all_indexes__[indexstr]
        param_struct = param_type()
        param_struct.nSize = sizeof(param_type)

        if (portstr != None):
            param_struct.nPortIndex = int(portstr)

        if (handle != None):
            omxerror = OMX_GetParameter(handle, index, byref(param_struct))
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")

            for name, val in param_type._fields_:
                for name2, val2 in element.items():
                    if (name2 == name):
                        setattr(param_struct, name, int(val2))

            if (indexstr == "OMX_IndexParamPortDefinition"):
                domstr = get_string_from_il_enum \
                    (getattr(param_struct, "eDomain"), "OMX_PortDomain")

                if (domstr == "OMX_PortDomainAudio"):
                    param2_type = OMX_AUDIO_PORTDEFINITIONTYPE
                    encode_audio_portdef(param_struct, param2_type, element)
                elif (domstr == "OMX_PortDomainVideo"):
                    param2_type = OMX_VIDEO_PORTDEFINITIONTYPE
                    encode_video_portdef(param_struct, param2_type, element)
                elif (domstr == "OMX_PortDomainImage"):
                    param2_type = OMX_IMAGE_PORTDEFINITIONTYPE
                    encode_image_portdef(param_struct, param2_type, element)
                elif (domstr == "OMX_PortDomainOther"):
                    param2_type = OMX_OTHER_PORTDEFINITIONTYPE
                    encode_other_portdef(param_struct, param2_type, element)


            omxerror = OMX_SetParameter(handle, index, byref(param_struct))
            interror = int(omxerror & 0xffffffff)
            domstr = ""
            err = get_string_from_il_enum(interror, "OMX_Error")
            log_line ()
            log_line ("%s" % param_struct.__class__.__name__, 1)
            for name, val in param_type._fields_:
                if (name == "nVersion"):
                    log_line ("%s -> '%08x'" \
                                    % (name, param_struct.nVersion.nVersion), 1)
                elif (name == "eDir"):
                    dirstr = get_string_from_il_enum \
                        (getattr(param_struct, name), "OMX_Dir")
                    log_line ("%s -> '%s'" % (name, dirstr), 1)
                elif (name == "eDomain"):
                    domstr = get_string_from_il_enum \
                        (getattr(param_struct, name), "OMX_PortDomain")
                    log_line ("%s -> '%s'" % (name, domstr), 1)
                elif (name == "format"):

                    if (domstr == "OMX_PortDomainAudio"):
                        param2_type = OMX_AUDIO_PORTDEFINITIONTYPE
                        decode_audio_portdef (param_struct, param2_type)
                    elif (domstr == "OMX_PortDomainVideo"):
                        param2_type = OMX_VIDEO_PORTDEFINITIONTYPE
                        decode_video_portdef (param_struct, param2_type)
                    elif (domstr == "OMX_PortDomainImage"):
                        param2_type = OMX_IMAGE_PORTDEFINITIONTYPE
                        decode_image_portdef (param_struct, param2_type)
                    elif (domstr == "OMX_PortDomainOther"):
                        param2_type = OMX_OTHER_PORTDEFINITIONTYPE
                        decode_other_portdef (param_struct, param2_type)

                else:
                    log_line ("%s -> '%s'" \
                        % (name, getattr(param_struct, name)), 1)

            log_result(element.tag, err)

            if (err == "OMX_ErrorNone"):
                return 0
            else:
                return interror
        else:
            log_line ("%s -> '%s %s'" \
                          % (element.tag, \
                                 "Could not find handle for", context.cnames[alias]))
            return get_il_enum_from_string("OMX_ErrorUndefined")

tagobj = skema.tag.SkemaTag(tagname="OMX_SetParameter")
