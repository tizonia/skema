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

from skema.omxil12 import __all_indexes__ as omxil12_indexes
from skema.omxil12 import get_string_from_il_enum
from skema.omxil12 import get_il_enum_from_string
from skema.omxil12 import OMX_GetConfig
from skema.omxil12 import OMX_SetConfig

from skema.utils import log_line
from skema.utils import log_api
from skema.utils import log_result

from ctypes import sizeof
from ctypes import byref


class tag_OMX_SetConfig(skema.tag.SkemaTag):
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

        param_type         = omxil12_indexes[indexstr]
        param_struct       = param_type()
        param_struct.nSize = sizeof(param_type)

        if (portstr != None):
            param_struct.nPortIndex = int(portstr)

        if (handle != None):
            omxerror = OMX_GetConfig(handle, index, byref(param_struct))
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")

            for name, val in param_type._fields_:
                for name2, val2 in element.items():
                    if (name2 == name):
                        setattr(param_struct, name, int(val2))


            omxerror = OMX_SetConfig(handle, index, byref(param_struct))
            interror = int(omxerror & 0xffffffff)
            domstr = ""
            err = get_string_from_il_enum(interror, "OMX_Error")
            log_line ()
            log_line ("%s" % param_struct.__class__.__name__, 1)
            for name, val in param_type._fields_:
                if (name == "nVersion"):
                    log_line ("%s -> '%08x'" \
                                    % (name, param_struct.nVersion.nVersion), 1)
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

tagobj = skema.tag.SkemaTag(tagname="OMX_SetConfig")
