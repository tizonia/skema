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

from skema.omxil12 import *

from skema.utils import log_api
from skema.utils import log_line
from skema.utils import log_param
from skema.utils import log_result

from ctypes import *
from xml.etree.ElementTree import ElementTree as et

class tag_OMX_GetComponentVersion(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias = element.get('alias')
        name = context.cnames[alias]
        log_api ("%s '%s'" % (element.tag, name))
        handle = context.handles[alias]
        cname = OMX_STRING()
        #cname = create_string_buffer(OMX_MAX_STRINGNAME_SIZE)
        cversion = OMX_VERSIONTYPE()
        specversion = OMX_VERSIONTYPE()
        cuuid = OMX_UUIDTYPE()
        if (handle != None):
            omxerror = OMX_GetComponentVersion(handle, cname,
                                               byref(cversion),
                                               byref(specversion),
                                               byref(cuuid))
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")

            log_line ()
            log_line ("Component Version", 1)
            for name, val in struct_anon_1._fields_:
                log_param (name, str(getattr(cversion.s, name)), 2)

            log_line ()
            log_line ("Spec Version", 1)
            for name, val in struct_anon_1._fields_:
                log_param (name, str(getattr(specversion.s, name)), 2)

            log_result(element.tag, err)

        else:
            log_line ("%s -> '%s %s'" \
                % (element.tag, \
                       "Could not find handle for", context.cnames[alias]))

tagobj = skema.tag.SkemaTag(tagname="OMX_GetComponentVersion")
