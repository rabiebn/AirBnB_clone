#!/usr/bin/python3
"""
Console Module has:
    HBNBCommand Class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Class, entry point of the command interpreter.

    Public instance methods:
        do_quit
        do_EOF
    """

    def do_EOF(self, arg):
        """
        Exits the program (command: Ctrl+D)
        """
        return True

    def do_quit(self, arg):
        """
        Exits the program (command: quit)
        """
        return True
    

if __name__ =='__main__':
    HBNBCommand().cmdloop()
