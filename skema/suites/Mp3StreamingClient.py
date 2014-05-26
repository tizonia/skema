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

import os
import skema.suite

SUITENAME="Mp3StreamingClient"
SCRIPTPATH = [str(os.path.join(os.path.dirname(os.path.realpath( __file__ )),
                               'Mp3StreamingClient.xml'))]
PATTERN = "^(?P<test_case_id>\w+):\W+(?P<measurement>\d+\.\d+)"

instobj = skema.suite.SkemaSuiteInstaller(suitename=SUITENAME,
                                            scriptpath=SCRIPTPATH)
runobj = skema.suite.SkemaSuiteRunner()
parserobj = skema.suite.SkemaSuiteParser(
    pattern=PATTERN,
    appendall={'units':'MB/s', 'result':'pass'})
suiteobj = skema.suite.SkemaSuite(suitename=SUITENAME, installer=instobj,
                                    runner=runobj, parser=parserobj)
