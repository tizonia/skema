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

class tag_OMX_ComponentNameEnum(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):

        log_api ("%s" % element.tag)

        cname = OMX_STRING()

        cnamelen = OMX_U32()
        cnamelen = OMX_MAX_STRINGNAME_SIZE

        index = OMX_U32()
        index = 0

        err = OMX_ERRORTYPE()
        log_line ()

        while True:

            omxerror = OMX_ComponentNameEnum(cname, cnamelen, index)
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")
            if (err == "OMX_ErrorNoMore"):
                break;

            log_line ("Component at index #%d : %s" % (index, cname),  1)
            index = index + 1;

        if (err == "OMX_ErrorNoMore"):
            log_result(element.tag, "OMX_ErrorNone")

tagobj = skema.tag.SkemaTag(tagname="OMX_ComponentNameEnum")
