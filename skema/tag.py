# Copyright (C) 2011-2014 Aratelia Limited - Juan A. Rubio
#
# Portions Copyright (C) 2010 Linaro
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

"""
Skema's tag-related base classes
"""

import os
import shutil

from skema.api import SkemaTagIf
from skema.config import get_config


class SkemaTag(SkemaTagIf):
    """Base class for defining skema's test tags.

    This can be used by test definition files to create an object that contains
    the building blocks for installing tests, running them, and parsing the
    results.

    tagsdir - name of the test tag
    """
    def __init__(self, tagname):
        self.tagsdir = tagname
        self.origdir = os.path.abspath(os.curdir)

    def install(self):
        """Install the test tag.

        This creates an install directory under the user's XDG_DATA_HOME
        directory to mark that the tag is installed.  The installer's
        install() method is then called from this directory to complete any
        test specific install that may be needed.
        """
        #if not self.installer:
        #    raise RuntimeError("no installer defined for '%s'" %
        #                        self.tagsdir)

        config = get_config()
        tagsdir = os.path.join(config.tagsdir, self.tagsdir)
        if os.path.exists(tagsdir):
            raise RuntimeError("%s is already installed" % self.tagsdir)
        os.makedirs(tagsdir)
        os.chdir(tagsdir)
        #try:
        #    self.installer.install()
        #except Exception as strerror:
        #    self.uninstall()
        #    raise
        #finally:
        os.chdir(self.origdir)

    def uninstall(self):
        """Uninstall the test tag.

        Uninstalling just recursively removes the test specific directory
        under the user's XDG_DATA_HOME directory.  This will both mark
        the test as removed, and clean up any files that were downloaded
        or installed under that directory.  Dependencies are intentionally
        not removed by this.
        """
        os.chdir(self.origdir)
        config = get_config()
        path = os.path.join(config.tagsdir, self.tagsdir)
        if os.path.exists(path):
            shutil.rmtree(path)

    # def _savetestdata(self, analyzer_assigned_uuid):
    #     TIMEFORMAT = '%Y-%m-%dT%H:%M:%SZ'
    #     bundle = {
    #         'format': 'Dashboard Bundle Format 1.2',
    #         'test_runs': [
    #             {
    #                 'test_id': self.tagsdir,
    #                 'analyzer_assigned_date': self.runner.starttime.strftime(TIMEFORMAT),
    #                 'analyzer_assigned_uuid': analyzer_assigned_uuid,
    #                 'time_check_performed': False,
    #                 'test_results': []
    #             }
    #         ]
    #     }
    #     filename = os.path.join(self.resultsdir, 'testdata.json')
    #     write_file(DocumentIO.dumps(bundle), filename)

    def run(self, element, context):
        raise NotImplementedError("%s: tag defined but not implemented!" %
                                  self.tagsdir)
