""" Contains the CmdManager class definition."""

import argparse
from cmd.argparsing.arg_formatter import ArgFormatter

__version__ = 0

class CmdManager(object):
    """  
    .. class:: CmdManager

    This class is intended to store commands, their associated functions and
    their arguments (that will be exposed through argparse).

    """

    parser = argparse.ArgumentParser(
        formatter_class=ArgFormatter,
        description=""" gtftoolkit is intended to ease manipulation of gtf """
                    """files.\n See available commands in the 'Available 
                    commands' section. WARNING: properly finding transcript 
                    and gene coordinates is error prone if IDs are ambiguous. 
                    Use Ensembl GTF for instance.""",
        epilog="Usage example:\n 'gtftoolkit command_name -h' for more " \
                "information.\n",
        version='%(prog)s {0}'.format(__version__)
    )
    parser = argparse.ArgumentParser(prog='PROG')

    sub_parsers = parser.add_subparsers(
        title='Available commands',
        dest='command',
        metavar='')

    # This attributes store the instance of CmdObject
    _cmd_obj_list = dict()

    def __init__(self):
        pass

    @classmethod
    def add_command(cls, cmd):
        """ Add new argument parser for a command  'self.cmd_name'. Note that
        verbose and keep-temp arguments are added by default."""

        # verbose is a default argument of any command
        cmd.parser.add_argument("--verbose",
                         "-v",
                         choices=range(4),
                         help="Display processing and warning messages.",
                         required=False)

        # keep-temp-file is a default argument of any command
        cmd.parser.add_argument("--keep-temp-file",
                         "-k",
                         action='store_true',
                         help="Keep all temporary files.",
                         required=False)

        # Add the command to the list of known commands

        cls._cmd_obj_list[cmd.name] = cmd

        # Update the global argument parser

        cls.sub_parsers.add_parser(
            cmd.name,
            formatter_class=ArgFormatter,
            parents=[cmd.parser],
            help=cmd.message)

    @classmethod
    def fun_by_cmd_name(cls, cmd_name):
        return cls._cmd_obj_list[cmd_name].fun

    @classmethod
    def parse_cmd_args(cls):
        """ Parse arguments of all declared commands."""
        args = cls.parser.parse_args(None)
        return args

