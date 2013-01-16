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

from skema.omxil12 import OMX_Deinit
from skema.omxil12 import get_string_from_il_enum

from skema.utils import log_api
from skema.utils import log_result

class tag_OMX_Deinit(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        log_api ("%s" % element.tag)
        omxerror = OMX_Deinit()
        interror = int(omxerror & 0xffffffff)
        err = get_string_from_il_enum(interror, "OMX_Error")
        log_result (element.tag, err)

tagobj = skema.tag.SkemaTag(tagname="OMX_Deinit")
