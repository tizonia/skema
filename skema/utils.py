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

from __future__ import print_function

import os
import shutil
import subprocess
import sys
import urllib2
import urlparse
import logging

from skema.config import get_config

class Tee(file):
    """ A file-like object that optionally mimics tee functionality.

    By default, output will go to both stdout and the file specified.
    Optionally, quiet=True can be used to mute the output to stdout.
    """
    def __init__(self, *args, **kwargs):
        try:
            self.quiet = kwargs.pop('quiet')
        except KeyError:
            self.quiet = False
        super(Tee, self).__init__(*args, **kwargs)

    def write(self, data):
        super(Tee, self).write(data)
        if self.quiet is False:
            sys.stdout.write(data)


class bcolors:
    BOLD = '\033[1m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def printit(line):
    config = get_config ()
    config.fd.writelines (line + '\n')
    if (config.quiet == False):
        print (line)


def log_param(param, val, tabs=0):
    l = ('\t' * tabs) + "[" + param + " -> '" + val + "']"
    lansi = "[skema] " + bcolors.WARNING + l + bcolors.ENDC
    logging.info(l)
    printit (lansi)


def log_line(line="", tabs=0):
    if (line == ""):
        lansi = "[skema] "
        l = ""
    else:
        l = ('\t' * tabs) + "[" + line + "]"
        lansi = "[skema] " + bcolors.WARNING + l + bcolors.ENDC
    logging.info(l)
    printit (lansi)


def log_api(line):
    log_line ()
    logging.info("")
    log_line ()
    logging.info("")
    l = "[" + line  +"]"
    logging.info(l)
    lansi = "[skema] " + bcolors.BOLD + l + bcolors.ENDC
    printit (lansi)


def log_result(tag, err):
    log_line ()
    if (err == "OMX_ErrorNone"):
        l = "[" + tag + " -> '" + err + "']"
        lansi = "[skema] " + bcolors.OKGREEN + l + bcolors.ENDC
        logging.info(l)
    else:
        l = "[" + tag + " -> '" + err + "']"
        lansi = "[skema] " + bcolors.FAIL + l + bcolors.ENDC
        logging.error(l)

    printit (lansi)


def geturl(url, path=""):
    urlpath = urlparse.urlsplit(url).path
    filename = os.path.basename(urlpath)
    if path:
        filename = os.path.join(path, filename)
    fd = open(filename, "w")
    try:
        response = urllib2.urlopen(urllib2.quote(url, safe=":/"))
        fd = open(filename, 'wb')
        shutil.copyfileobj(response, fd, 0x10000)
        fd.close()
        response.close()
    except:
        raise RuntimeError("Could not retrieve %s" % url)
    return filename


def write_file(data, path):
    with open(path, "w") as fd:
        fd.write(data)

def read_file(path):
    global _fake_files
    global _fake_paths
    if _fake_files is not None:
        if path in _fake_files:
            return _fake_files[path]
    if _fake_paths is not None:
        if path in _fake_paths:
            path = _fake_paths[path]
    with open(path) as fd:
        data = fd.read()
    return data


def run_and_log(cmd, fd, quiet=False):
    """
    Run a command and log the output to fd
    """
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, shell=True)
    while proc.returncode == None:
        proc.poll()
        data = proc.stdout.readline()
        fd.write(data)
        if quiet is False:
            sys.stdout.write(data)
    return proc.returncode
