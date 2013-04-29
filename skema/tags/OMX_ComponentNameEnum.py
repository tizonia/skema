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

from skema.omxil12 import OMX_STRING
from skema.omxil12 import OMX_U32
from skema.omxil12 import OMX_MAX_STRINGNAME_SIZE
from skema.omxil12 import OMX_ERRORTYPE
from skema.omxil12 import OMX_ComponentNameEnum
from skema.omxil12 import get_string_from_il_enum

from skema.utils import log_api
from skema.utils import log_line
from skema.utils import log_result

from ctypes import c_ubyte
from ctypes import c_char
from ctypes import c_char_p
from ctypes import POINTER
from ctypes import cast

class tag_OMX_ComponentNameEnum(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):

        log_api ("%s" % element.tag)

        cname = (c_ubyte * OMX_MAX_STRINGNAME_SIZE)()
        cnamelen = OMX_U32()
        cnamelen = OMX_MAX_STRINGNAME_SIZE

        index = OMX_U32()
        index = 0

        err = OMX_ERRORTYPE()
        log_line ()

        while True:

            omxerror = OMX_ComponentNameEnum(cast(cname, POINTER(c_char)),
                                             cnamelen, index)
            interror = int(omxerror & 0xffffffff)
            err = get_string_from_il_enum(interror, "OMX_Error")
            if (err == "OMX_ErrorNoMore") or (err != "OMX_ErrorNone"):
                break

            log_line ("Component at index #%d : %s" \
                          % (index, cast(cname, c_char_p).value),  1)
            index = index + 1

        if (err == "OMX_ErrorNoMore"):
            log_result(element.tag, "OMX_ErrorNone")
            return 0
        else:
            log_result(element.tag, err)
            return interror

tagobj = skema.tag.SkemaTag(tagname="OMX_ComponentNameEnum")
