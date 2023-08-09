#!/usr/bin/python3
"""
This is the console module for the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    This class defines the HBNB command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the command interpreter using Ctrl+D.
        """
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
