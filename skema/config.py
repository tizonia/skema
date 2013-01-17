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
import threading

from skema.omxil12 import OMX_CALLBACKTYPE


class SkemaConfig(object):
    def __init__(self):
        home       = os.environ.get('HOME', '/')
        baseconfig = os.environ.get('XDG_CONFIG_HOME',
                                    os.path.join(home, '.config'))
        basedata   = os.environ.get('XDG_DATA_HOME',
                                  os.path.join(home, '.local', 'share'))

        self.configdir  = os.path.join(baseconfig, 'skema')
        self.suitesdir  = os.path.join(basedata, 'skema', 'installed-suites')
        self.tagsdir    = os.path.join(basedata, 'skema', 'installed-tags')
        self.resultsdir = os.path.join(basedata, 'skema', 'results')
        self.fd         = file(os.devnull)
        self.quiet      = True

        self.ilevent = threading.Event()
        self.cbacks  = OMX_CALLBACKTYPE()

        # Global Dictionaries
        self.aliases                 = dict() # comp name -> comp alias
        self.cnames                  = dict() # comp alias -> comp name
        self.cnames2                 = dict() # comp handle -> comp name
        self.handles                 = dict() # comp alias -> comp handle
        self.cmdevents               = dict() # comp comp handle -> cmd event
        self.eosevents               = dict() # comp comp handle -> eos event
        self.settings_changed_events = dict() # comp comp handle -> eos event
        self.params                  = dict() # OMX_IndexParam... -> OMX_ param struct
        self.configs                 = dict() # OMX_IndexConfig... -> OMX_ config struct
        self.result                  = dict() # Test result

_config = None

def get_config():
    global _config
    if _config is not None:
        return _config
    _config = SkemaConfig()
    return _config

def set_config(config):
    global _config
    _config = config

