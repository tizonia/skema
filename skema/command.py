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
Skema command-related base classes
"""

from optparse import OptionParser
import os
import sys


class _SkemaOptionParser(OptionParser):
    """
    This is just to override the epilog formatter to allow newlines
    """
    def format_epilog(self, formatter):
        return self.epilog


class SkemaCmd(object):
    """ Base class for commands that can be passed to Skema.

    Commands added to skema should inherit from SkemaCmd.  To allow for
    autodiscovery, the name of the class should begin with cmd_.

    Arguments allowed by the command can be specified in the 'arglist'.
    These arguments will automatically be listed in the help for that
    command.  Required arguments should begin with a '*'.  For example:
        arglist = ['*requiredarg', 'optionalarg']

    Options may also be specified by using the 'options' list.  To add
    arguments, you must use the make_option() function from optparse.
    For example:
        options = [make_option("-b", "--bar", dest="bar")]

    Commands also support subcommands.  A subcommand is similar to a
    command in skema, and it should also inherit from SkemaCmd.  However,
    a subcommand class should not begin with cmd_.  Instead, it should
    be tied to the command that uses it, using the 'subcmds' dict.
    For example:
        class subcmd_bar(SkemaCmd):
            pass
        class cmd_foo(SkemaCmd):
            subcmds = {'bar':subcmd_bar()}
            pass
    """
    options = []
    arglist = []

    def __init__(self, name_prefix=''):
        self._name_prefix = name_prefix
        self.parser = _SkemaOptionParser(usage=self._usage(),
                                         epilog=self._desc())
        for opt in self.options:
            self.parser.add_option(opt)

    def main(self, argv):
        (self.opts, self.args) = self.parser.parse_args(argv)
        return self.run()

    def name(self):
        return self._name_prefix + _convert_command_name(self.__class__.__name__)

    def run(self):
        raise NotImplementedError("%s: command defined but not implemented!" %
                                  self.name())

    def _usage(self):
        usagestr = "Usage: skema %s" % self.name()
        for arg in self.arglist:
            if arg[0] == '*':
                usagestr += " %s" % arg[1:].upper()
            else:
                usagestr += " [%s]" % arg.upper()
        return usagestr

    def _desc(self):
        from inspect import getdoc
        docstr = getdoc(self)
        if not docstr:
            return ""
        description = "\nDescription:\n"
        description += docstr + "\n"
        return description

    def help(self):
        #For some reason, format_help includes an extra \n
        return self.parser.format_help()[:-1]

    def get_subcommand(self, name):
        return None


class SkemaCmdWithSubcommands(SkemaCmd):

    arglist = ['subcommand']

    def main(self, argv):
        if not argv:
            print "Missing sub-command." + self._list_subcmds()
        else:
            subcmd = self.get_subcommand(argv[0])
            if subcmd is None:
                # This line might print the help and raise SystemExit if
                # --help is passed or if an invalid option was passed.
                opts, args = self.parser.parse_args(argv)
                # If it didn't, complain.
                print "'%s' not found as a sub-command of '%s'" % (
                    args[0], self.name()) + self._list_subcmds()
            else:
                return subcmd.main(argv[1:])

    def get_subcommand(self, name):
        subcmd_cls = getattr(self, 'cmd_' + name.replace('_', '-'), None)
        if subcmd_cls is None:
            return None
        return subcmd_cls(self.name() + ' ')

    def _usage(self):
        usagestr = SkemaCmd._usage(self)
        usagestr += self._list_subcmds()
        return usagestr

    def _list_subcmds(self):
        subcmds = []
        for attrname in self.__class__.__dict__.keys():
            if attrname.startswith('cmd_'):
                subcmds.append(_convert_command_name(attrname))
        if not subcmds:
            return ''
        return "\n\nAvailable sub-commands:\n  " + "\n  ".join(subcmds)


def _convert_command_name(cmd):
    return cmd[4:].replace('_','_')


def _find_commands(mod):
    cmds = {}
    for name, func in mod.__dict__.iteritems():
        if name.startswith("cmd_"):
            real_name = _convert_command_name(name)
            cmds[real_name] = func()
    return cmds


def get_all_cmds():
    from skema import builtins
    cmds = _find_commands(builtins)
    return cmds


def get_command(cmd_name):
    cmds = get_all_cmds()
    return cmds.get(cmd_name)
