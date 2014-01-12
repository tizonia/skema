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

import readline
import skema.command

def completer(text, state):
    commands = ["example", None] #skema.command.get_all_cmds()
    print commands
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def main(argv):
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    argv = argv[1:]
    if not argv:
        argv = ['help']
    cmd = argv.pop(0)
    cmd_func = skema.command.get_command(cmd)
    if not cmd_func:
        print "command '%s' not found" % cmd
        return 1
    return cmd_func.main(argv)

if __name__ == '__main__':
    import os
    import sys
    exit_code = main(sys.argv)
    sys.exit(exit_code)
