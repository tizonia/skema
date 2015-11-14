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

from skema.utils import log_api
from skema.utils import log_result


class tag_OMX_BaseProfileUseEGLImages(skema.tag.SkemaTag):
    """

    """
    def run(self, element, context):
        alias       = element.get('alias')
        name        = context.cnames[alias]
        portstr     = element.get('port')
        howmanystr  = element.get('howmany')

        log_api ("%s %s:Port-%s' 'Howmany:%s'" \
                     % (element.tag, name, portstr, howmanystr))

        context.base_profile_mgr.use_egl_images(alias, portstr, howmanystr)

        log_result (element.tag, "OMX_ErrorNone")

        return 0

tagobj = skema.tag.SkemaTag(tagname="OMX_BaseProfileUseEGLImages")
