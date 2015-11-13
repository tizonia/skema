# Copyright (C) 2011-2015 Aratelia Limited - Juan A. Rubio
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
Skema's suite-related utility functions
"""

import os
import sys
from ctypes import *
from xml.etree.ElementTree import ElementTree as et
from optparse import make_option

import skema.command
from skema.omxil12 import get_string_from_il_enum
from skema.utils import log_line
from skema.utils import log_result
from skema.tagutils import get_tag
from skema.config import get_config


def run_suite(scriptpath):

    tree = et()
    tree.parse(scriptpath)
    titer = tree.iter()

    config = get_config()

    suites = []
    cases = []
    errors = dict()
    last_tag = dict()
    case = ""
    for elem in titer:

        if elem.tag == "Suite":
            continue

        if elem.tag == "Case":
            case  = elem.get('name')
            log_line ("Use Case : '%s'"  % case)
            cases.append(case)
            errors[case] = 0
            result = 0
            continue

        if result == 0:
            tag_func = get_tag(elem.tag)
            if not tag_func:
                log_line ("Tag '%s' not found. Exiting."  % elem.tag)
                sys.exit(1)

            result = tag_func.run(elem, config)
            if result != 0:
                log_result (elem.tag, get_string_from_il_enum(result, "OMX_Error"))
                errors[case] = result
            last_tag[case] = elem.tag

    if result != 0:
        config.base_profile_mgr.stop()

    log_line()
    log_line()
    log_line("-------------------------------------------------------------------")
    msg = "SUITE EXECUTION SUMMARY : " + str(len(cases)) + " test cases executed"
    log_result (msg, get_string_from_il_enum(result, "OMX_Error"))
    last_error = 0
    for case in cases:
        msg = "CASE : " + case + " (last tag was '" + last_tag[case] + "')"
        log_result (msg, get_string_from_il_enum(errors[case], "OMX_Error"))
        if errors[case] != 0:
            last_error = errors[case]
    log_line()
    log_line("-------------------------------------------------------------------")
    log_line()

    return last_error

def suiteloader(suitename):
    """
    Load the suites, which can be either an individual
    file, or a directory with an __init__.py
    """
    importpath = "skema.suites.%s" % suitename
    try:
        mod = __import__(importpath)
    except ImportError:
        print "unknown suite '%s'" % suitename
        sys.exit(1)
    for i in importpath.split('.')[1:]:
        mod = getattr(mod,i)
    try:
        base = mod.testdir.suiteobj
    except AttributeError:
        base = mod.suiteobj

    return base

