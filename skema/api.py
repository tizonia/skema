# Copyright (C) 2011-2013 Aratelia Limited - Juan A. Rubio
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
Public API for extending Skema
"""
from abc import abstractmethod, abstractproperty


class SkemaSuiteIf(object):
    """
    Skema test suite.

    Abstract class for skema test suite classes.
    """

    @abstractmethod
    def install(self):
        """
        Install the test suite.

        This creates an install directory under the user's XDG_DATA_HOME
        directory to mark that the suite is installed.  The installer's
        install() method is then called from this directory to complete any
        test specific install that may be needed.
        """

    @abstractmethod
    def uninstall(self):
        """
        Uninstall the test suite.

        Uninstalling just recursively removes the test specific directory under
        the user's XDG_DATA_HOME directory.  This will both mark the suite as
        removed, and clean up any files that were installed under that
        directory.  Dependencies are intentionally not removed by this.
        """

    @abstractmethod
    def run(self, quiet=False):
        # TODO: Document me
        pass

    @abstractmethod
    def parse(self, resultname):
        # TODO: Document me
        pass

class SkemaTagIf(object):
    """
    Skema tag.

    Abstract class for skema tag classes.
    """

    @abstractmethod
    def install(self):
        """
        Install the tag.

        This creates an install directory under the user's XDG_DATA_HOME
        directory to mark that the tag is installed.  The installer's
        install() method is then called from this directory to complete any
        test specific install that may be needed.
        """

    @abstractmethod
    def uninstall(self):
        """
        Uninstall the test tag.

        Uninstalling just recursively removes the test specific directory under
        the user's XDG_DATA_HOME directory.  This will both mark the tag as
        removed, and clean up any files that were installed under that
        directory.  Dependencies are intentionally not removed by this.
        """

    @abstractmethod
    def run(self, element, context):
        # TODO: Document me
        pass
