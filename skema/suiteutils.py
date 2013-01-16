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
Skema's suite-related utility functions
"""

import os
import sys
from ctypes import *
from xml.etree.ElementTree import ElementTree as et
from optparse import make_option

import skema.command
from skema.utils import log_line
from skema.tagutils import get_tag
from skema.config import get_config


def run_suite(scriptpath):

    tree = et()
    tree.parse(scriptpath)
    titer = tree.iter()

    config = get_config()

    for elem in titer:

        if elem.tag == "Suite":
            continue

        if elem.tag == "Case":
            log_line ("Use Case : %s"  % elem.get('name'))
            continue

        tag_func = get_tag(elem.tag)

        if not tag_func:
            print "run_suite : tag [%s] not found" % elem.tag
            return 1

        tag_func.run(elem, config)


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

