""" A container for a command."""

from cmd.argparsing.cmd_manager import CmdManager

class CmdObject(object):
    """ A container for a command."""

    def __init__(self,
                 name=None,
                 message=None,
                 parser=None,
                 fun=None):
        self.name = name
        self.message = message
        self.parser = parser
        self.fun = fun

        CmdManager.add_command(self)



