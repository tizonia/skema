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
Built-in Skema commands
"""

import os
import sys
from optparse import make_option

import skema.command
import skema.suite
from skema.config import get_config

class cmd_version(skema.command.SkemaCmd):
    """
    Show the version of skema
    """
    def run(self):
        import skema
        print skema.__version__


class cmd_help(skema.command.SkemaCmd):
    """ Get help on skema commands

    If the command name is ommited, calling the help command will return a
    list of valid commands.
    """
    arglist = ['command', 'subcommand']
    def run(self):
        if len(self.args) < 1:
            print ""
            print '\033[93m' + "Available commands:" + '\033[0m'
            print ""
            for cmd in skema.command.get_all_cmds():
                print '\033[91m' + "  %s" % cmd
            print
            print '\033[93m' + "To access extended help on " \
                "a command use 'skema help " \
                "[command]'" + '\033[0m'
            print ""
            return
        command_name = self.args.pop(0)
        cmd = skema.command.get_command(command_name)
        if not cmd:
            print "No command found for '%s'" % command_name
            return
        while self.args:
            subcommand_name = self.args.pop(0)
            cmd = cmd.get_subcommand(subcommand_name)
            if not cmd:
                print "No sub-command of '%s' found for '%s'" % (
                    command_name, subcommand_name)
                return
            command_name += ' ' + subcommand_name
        print cmd.help()


class cmd_install_suite(skema.command.SkemaCmd):
    """
    Install a suite
    """
    arglist = ['*suitename']

    def run(self):
        from skema.suiteutils import suiteloader

        if len(self.args) != 1:
            print "please specify the name of the suite to install"
            sys.exit(1)
        suite = suiteloader(self.args[0])
        try:
            suite.install()
        except RuntimeError as strerror:
            print "Suite installation error: %s" % strerror
            sys.exit(1)


class cmd_run_suite(skema.command.SkemaCmd):
    """
    Run suites
    """
    arglist = ['*suitename']
    options = [make_option('-q', '--quiet', action='store_true',
                           default=False, dest='quiet'),
               make_option('-o', '--output',  action='store',
                           default=None, metavar="DIR",
                           help="Store processed suite output to DIR")
               ]

    def run(self):
        from skema.suiteutils import suiteloader

        if len(self.args) != 1:
            print "please specify the name of the suite to run"
            sys.exit(1)
        suite = suiteloader(self.args[0])
        try:
            return suite.run(quiet=self.opts.quiet, output=self.opts.output)

        except Exception as strerror:
            print "Suite execution error: %s" % strerror
            sys.exit(1)

class cmd_uninstall_suite(skema.command.SkemaCmd):
    """
    Uninstall a suite
    """
    arglist = ['*suitename']

    def run(self):
        from skema.suiteutils import suiteloader

        if len(self.args) != 1:
            print "please specify the name of the suite to uninstall"
            sys.exit(1)
        suite = suiteloader(self.args[0])
        try:
            suite.uninstall()
        except Exception as strerror:
            print "Suite uninstall error: %s" % strerror
            sys.exit(1)


class cmd_list_installed_suites(skema.command.SkemaCmd):
    """
    List suites that are currently installed
    """
    def run(self):
        config = get_config()
        try:
            for dir in os.listdir(config.suitesdir):
                print dir
        except OSError:
            print "No suites installed"


class cmd_install_tag(skema.command.SkemaCmd):
    """
    Install a tag
    """
    arglist = ['*tagname']

    def run(self):
        from skema.tagutils import tagloader

        if len(self.args) != 1:
            print "please specify the name of the tag to install"
            sys.exit(1)
        tag = tagloader(self.args[0])
        try:
            tag.install()
        except RuntimeError as strerror:
            print "Tag installation error: %s" % strerror
            sys.exit(1)


class cmd_uninstall_tag(skema.command.SkemaCmd):
    """
    Uninstall a tag
    """
    arglist = ['*tagname']

    def run(self):
        from skema.tagutils import tagloader

        if len(self.args) != 1:
            print "please specify the name of the tag to uninstall"
            sys.exit(1)
        tag = tagloader(self.args[0])
        try:
            tag.uninstall()
        except Exception as strerror:
            print "Tag uninstall error: %s" % strerror
            sys.exit(1)


class cmd_list_installed_tags(skema.command.SkemaCmd):
    """
    List tags that are currently installed
    """
    def run(self):
        config = get_config()
        try:
            for dir in os.listdir(config.tagsdir):
                print dir
        except OSError:
            print "No tags installed"




class cmd_list_suites(skema.command.SkemaCmd):
    """
    List all known suites
    """
    def run(self):
        from skema import suites
        from pkgutil import walk_packages
        for importer, mod, ispkg in walk_packages(suites.__path__):
            print mod

class cmd_list_tags(skema.command.SkemaCmd):
    """
    List all known tags
    """
    def run(self):
        from skema import tags
        from pkgutil import walk_packages
        for importer, mod, ispkg in walk_packages(tags.__path__):
            print mod

