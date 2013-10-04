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
from skema.omxil12 import get_string_from_il_enum
from skema.omxil12 import OMX_PARAM_CONTENTURITYPE
from skema.omxil12 import OMX_GetParameter

from skema.utils import log_api
from skema.utils import log_line
from skema.utils import log_param
from skema.utils import log_result

from ctypes import c_char_p
from ctypes import sizeof
from ctypes import cast
from ctypes import byref


class tag_OMX_GetContentURI(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        indexstr = "OMX_IndexParamContentURI"
        alias = element.get('alias')
        name = context.cnames[alias]
#        This param struct does not have a port index.
#        portstr = element.get('port')
        log_api ("%s '%s' '%s'" \
                       % (element.tag, indexstr, name))
        handle = context.handles[alias]
        index = get_il_enum_from_string(indexstr)
        param_type = OMX_PARAM_CONTENTURITYPE
        param_struct = param_type()
        param_struct.nSize = sizeof(param_type)

#        This param struct does not have a port index.
#        if (portstr != None):
#            param_struct.nPortIndex = int(portstr)

        if (handle != None):
            omxerror = OMX_GetParameter(handle, index, byref(param_struct))
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")

            uristr = c_char_p()
            uristr = cast(param_struct.contentURI, c_char_p)

            log_line ()
            log_line ("%s" % param_struct.__class__.__name__, 1)
            for name, _ in param_type._fields_:
                if (name == "nVersion"):
                    log_line ("%s -> '%08x'" \
                                    % (name, param_struct.nVersion.nVersion), 1)
                elif (name == "contentURI"):
                    log_param (name, uristr.value, 1)
                else:
                    log_param (name, str(getattr(param_struct, name)), 1)

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

tagobj = skema.tag.SkemaTag(tagname="OMX_GetContentURI")
