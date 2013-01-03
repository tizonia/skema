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

import os
import sys

from skema.tags import *

def _convert_tag_name(tag):
    return tag[4:].replace('_','_')

def _find_tags(mod):
    tags = {}
    for name, func in mod.__dict__.iteritems():
        if name.startswith("tag_"):
            real_name = _convert_tag_name(name)
            tags[real_name] = func(real_name)
    return tags

def get_all_tags():
    from skema import tags
    the_tags = {}
    for mod in tags.__all__:
        if (mod !=  "__init__"):
            the_tags.update(_find_tags(getattr(tags, mod)))
    return the_tags


def get_tag(tag_name):
    tags = get_all_tags()
    return tags.get(tag_name)

def tagloader(tag_name):
    """
    Load the tag definition, which can be either an individual file, or a
    directory with an __init__.py
    """
    importpath = "skema.tags.%s" % tag_name
    try:
        mod = __import__(importpath)
    except ImportError:
        print "unknown tag '%s'" % tag_name
        sys.exit(1)
    for i in importpath.split('.')[1:]:
        mod = getattr(mod,i)
    try:
        base = mod.testdir.tagobj
    except AttributeError:
        base = mod.tagobj

    return base
