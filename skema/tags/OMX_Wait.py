# Copyright (C) 2011-2015 Aratelia Limited - Juan A. Rubio
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
import time

from skema.utils import log_line
from skema.utils import log_result
from skema.utils import log_api


class tag_OMX_Wait(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        delay_in_seconds = element.get('delay')
        log_api ("%s '%s'" \
            % (element.tag, delay_in_seconds))

        time.sleep(float(delay_in_seconds))

        log_line ()
        msg = "Waited '" + delay_in_seconds + "' seconds"
        log_result (msg, "OMX_ErrorNone")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_Wait")
