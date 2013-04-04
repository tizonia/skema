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
Skema's suite-related base classes
"""

import os
import glob
import re
import shutil
import time
import logging

from commands import getstatusoutput
from datetime import datetime
from uuid import uuid1

from skema.api import SkemaSuiteIf
from skema.config import get_config
from skema.suiteutils import run_suite
from skema.utils import log_line
from skema.omxil12 import get_string_from_il_enum

class SkemaSuite(SkemaSuiteIf):
    """Base class for defining Skema test suites.

    This can be used by test definition files to create an object that contains
    the building blocks for installing tests, running them, and parsing the
    results.

    suitename - name of the test suite
    version - version of the test suite
    installer - SkemaInstaller instance to use
    runner - SkemaRunner instance to use
    parser - SkemaParser instance to use
    """
    def __init__(self, suitename, version="", installer=None, runner=None,
                 parser=None):
        self.suitename = suitename
        self.version = version
        self.installer = installer
        self.runner = runner
        self.parser = parser
        self.origdir = os.path.abspath(os.curdir)

    def install(self):
        """Install the test suite.

        This creates an install directory under the user's XDG_DATA_HOME
        directory to mark that the test is installed.  The installer's
        install() method is then called from this directory to complete any
        test specific install that may be needed.
        """
        if not self.installer:
            raise RuntimeError("no installer defined for '%s'" %
                                self.suitename)
        config = get_config()
        suitesdir = os.path.join(config.suitesdir, self.suitename)
        if os.path.exists(suitesdir):
            raise RuntimeError("%s is already installed" % self.suitename)
        os.makedirs(suitesdir)
        os.chdir(suitesdir)
        try:
            self.installer.install()
        except Exception as strerror:
            self.uninstall()
            raise
        finally:
            os.chdir(self.origdir)

    def uninstall(self):
        """Uninstall the test suite.

        Uninstalling just recursively removes the test specific directory
        under the user's XDG_DATA_HOME directory.  This will both mark
        the test as removed, and clean up any files that were downloaded
        or installed under that directory.  Dependencies are intentionally
        not removed by this.
        """
        os.chdir(self.origdir)
        config = get_config()
        path = os.path.join(config.suitesdir, self.suitename)
        if os.path.exists(path):
            shutil.rmtree(path)

    def _savetestdata(self, analyzer_assigned_uuid):
        TIMEFORMAT = '%Y-%m-%dT%H:%M:%SZ'
        bundle = {
            'format': 'Dashboard Bundle Format 1.2',
            'test_runs': [
                {
                    'test_id': self.suitename,
                    'analyzer_assigned_date': self.runner.starttime.strftime(TIMEFORMAT),
                    'analyzer_assigned_uuid': analyzer_assigned_uuid,
                    'time_check_performed': False,
                    'test_results': []
                }
            ]
        }
        #filename = os.path.join(self.resultsdir, 'testdata.json')
        #write_file(DocumentIO.dumps(bundle), filename)

    def run(self, quiet=False):
        if not self.runner:
            raise RuntimeError("no test runner defined for '%s'" %
                                self.suitename)
        config = get_config()
        uuid = str(uuid1())
        suitesdir = os.path.join(config.suitesdir, self.suitename)
        resultname = (self.suitename +
                      str(time.mktime(datetime.utcnow().timetuple())))
        self.resultsdir = os.path.join(config.resultsdir, resultname)
        os.makedirs(self.resultsdir)
        result = 0
        try:
            os.chdir(suitesdir)
            scriptpath = glob.glob( os.path.join(suitesdir, '*.xml') )[0]
            result = self.runner.run(scriptpath,
                            self.resultsdir, quiet=quiet)
            self._savetestdata(uuid)
        finally:
            os.chdir(self.origdir)
        # result_id = os.path.basename(self.resultsdir)

        # TODO: Replace print with log_line
        # log_line ("%s : COMPLETED WITH RESULT '%s'" \
        #               % (self.suitename, \
        #                      get_string_from_il_enum(result, "OMX_Error")))
        # log_line ("%s : Log files can be found in '%s'" \
        #               % (self.suitename, self.resultsdir))
        print ("[%s] COMPLETED WITH RESULT '%s'" \
                   % (self.suitename, \
                          get_string_from_il_enum(result, "OMX_Error")))
        print("[%s] Log files can be found in '%s'" % (self.suitename, \
                                                           self.resultsdir))
        return result

    def parse(self, resultname):
        if not self.parser:
            raise RuntimeError("no test parser defined for '%s'" %
                                self.suitename)
        config = get_config()
        resultsdir = os.path.join(config.resultsdir, resultname)
        os.chdir(resultsdir)
        self.parser.parse()
        os.chdir(self.origdir)


class SkemaSuiteInstaller(object):
    """Base class for defining an installer object.

    This class can be used as-is for simple installers, or extended for more
    advanced funcionality.

    suitename - name of the test suite
    scriptpath - xml file with the list of tests to be executed
    """
    def __init__(self, suitename, scriptpath, **kwargs):
        self.suitename = suitename
        self.scriptpath = scriptpath

    def _installscript(self):
        if not self.scriptpath:
            return 0
        config = get_config()
        suitesdir = os.path.join(config.suitesdir, self.suitename)
        cmd = "cp %s" % "".join(self.scriptpath)
        cmd = "%s %s" % (cmd, "".join(suitesdir))
        rc, output = getstatusoutput(cmd)
        if rc:
            raise RuntimeError("Dependency installation failed. %d : %s" %(rc,output))

    def install(self):
        self._installscript()

class SkemaSuiteRunner(object):
    """Base class for defining an test runner object.

    This class can be used as-is for simple execution with the expectation
    that the run() method will be called from the directory where the test
    was installed.  Steps, if used, should handle changing directories from
    there to the directory where the test was extracted if necessary.
    This class can also be extended for more advanced funcionality.

    """
    def __init__(self):
        self.testoutput = []

    def _runsteps(self, scriptpath, resultsdir, quiet=False):
        outputlog = os.path.join(resultsdir, 'outputlog.txt')
        outputlog2 = os.path.join(resultsdir, 'outputlog2.txt')
        logging.basicConfig (filename=outputlog2, filemode='w', \
                                 format='%(asctime)s - %(levelname)s : %(message)s', \
                                 level=logging.DEBUG)
        logging.info("log")

        result = 0
        with open(outputlog, 'a') as fd:
            config = get_config()
            config.quiet = quiet
            temp = config.fd
            config.fd = fd
            result = run_suite(scriptpath)
            config.fd = temp
        logging.shutdown()
        return result

    def run(self, scriptpath, resultsdir, quiet=False):
        self.starttime = datetime.utcnow()
        result = self._runsteps(scriptpath, resultsdir, quiet=quiet)
        self.endtime = datetime.utcnow()
        return result


class SkemaSuiteParser(object):
    """Base class for defining a test parser

    This class can be used as-is for simple results parsers, but will
    likely need to be extended slightly for many.  If used as it is,
    the parse() method should be called while already in the results
    directory and assumes that a file for test output will exist called
    testoutput.log.

    pattern - regexp pattern to identify important elements of test output
        For example: If your testoutput had lines that look like:
            "test01:  PASS", then you could use a pattern like this:
            "^(?P<testid>\w+):\W+(?P<result>\w+)"
            This would result in identifying "test01" as testid and
            "PASS" as result.  Once parse() has been called,
            self.results.test_results[] contains a list of dicts of all the
            key,value pairs found for each test result
    fixupdict - dict of strings to convert test results to standard strings
        For example: if you want to standardize on having pass/fail results
            in lower case, but your test outputs them in upper case, you could
            use a fixupdict of something like: {'PASS':'pass','FAIL':'fail'}
    appendall - Append a dict to the test_results entry for each result.
        For example: if you would like to add units="MB/s" to each result:
            appendall={'units':'MB/s'}
    """
    def __init__(self, pattern=None, fixupdict=None, appendall={}):
        self.pattern = pattern
        self.fixupdict = fixupdict
        self.results = {'test_results':[]}
        self.appendall = appendall

    def _find_testid(self, id):
        for x in self.results['test_results']:
            if x['testid'] == id:
                return self.results['test_results'].index(x)

    def parse(self):
        """Parse test output to gather results

        Use the pattern specified when the class was instantiated to look
        through the results line-by-line and find lines that match it.
        Results are then stored in self.results.  If a fixupdict was supplied
        it is used to convert test result strings to a standard format.
        """
        filename = "testoutput.log"
        try:
            pat = re.compile(self.pattern)
        except Exception as strerror:
            raise RuntimeError(
                "SkemaSuiteParser - Invalid regular expression '%s' - %s" % (
                    self.pattern,strerror))

        with open(filename, 'r') as stream:
            for lineno, line in enumerate(stream, 1):
                match = pat.search(line)
                if not match:
                    continue
                data = match.groupdict()
                data["log_filename"] = filename
                data["log_lineno"] = lineno
                self.results['test_results'].append(data)
        if self.fixupdict:
            self.fixresults(self.fixupdict)
        if self.appendall:
            self.appendtoall(self.appendall)
        self.fixmeasurements()
        self.fixids()

    def append(self, testid, entry):
        """Appends a dict to the test_results entry for a specified testid

        This lets you add a dict to the entry for a specific testid
        entry should be a dict, updates it in place
        """
        index = self._find_testid(testid)
        self.results['test_results'][index].update(entry)

    def appendtoall(self, entry):
        """Append entry to each item in the test_results.

        entry - dict of key,value pairs to add to each item in the
        test_results
        """
        for t in self.results['test_results']:
            t.update(entry)

    def fixresults(self, fixupdict):
        """Convert results to a known, standard format

        pass it a dict of keys/values to replace
        For instance:
            {"TPASS":"pass", "TFAIL":"fail"}
        This is really only used for qualitative tests
        """
        for t in self.results['test_results']:
            if t.has_key("result"):
                t['result'] = fixupdict[t['result']]

    def fixmeasurements(self):
        """Measurements are often read as strings, but need to be float
        """
        for id in self.results['test_results']:
            if id.has_key('measurement'):
                id['measurement'] = float(id['measurement'])

    def fixids(self):
        """
        Convert spaces to _ in test_case_id and remove illegal characters
        """
        badchars = "[^a-zA-Z0-9\._-]"
        for id in self.results['test_results']:
            if id.has_key('test_case_id'):
                id['test_case_id'] = id['test_case_id'].replace(" ", "_")
                id['test_case_id'] = re.sub(badchars, "", id['test_case_id'])

