#!/usr/bin/python3
"""
Console Module defines:
    HBNBCommand Class;
    parse Function.
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from shlex import split


def parse(arg):
    """
    Parses 'arg' into tokens.
    """
    arguments = []
    for i in split(arg):
        if i[0] == '"' and i[-1] == '"':
            arguments.append(i[1:-1])
        else:
            arguments.append(i)
    
    return arguments

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Class, entry point of the command interpreter.

    Public instance methods:
        do_quit
        do_EOF
    """

    prompt = '(hbnb) '
    __classes = ['BaseModel']

    def do_EOF(self, arg):
        """
        Exits the program (command: Ctrl+D)
        """
        print("")
        return True

    def do_quit(self, arg):
        """
        Exits the program (command: quit)
        """
        return True
    
    def do_create(self, arg):
        """
        Creates a new instance, saves it to the JSON file and prints 'id'.
        """
        if arg:
            if arg == 'BaseModel':
                obj = BaseModel()
                storage.new(obj)
                storage.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints th string representation of an instance,
        based on the class name and the 'id'.
        """
        arguments = parse(arg)
        obj_dict = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            print("[{}] ({}) {}".format(
                arguments[0], arguments[1], obj_dict["{}.{}".format(
                arguments[0], arguments[1])]))
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and 'id',
        and saves changes to JSON file.
        """
        arguments = parse(arg)
        obj_dict = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arguments[0], arguments[1])]
            storage.save()
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = parse(arg)
        obj_list = []
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(args) == 0 or args[0] in obj.__str__():
                    obj_list.append("[{}] ({}) {}".format(
                        obj["__class__"], obj["id"], obj))
            print(obj_list)
    
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        and saves the change into the JSON file.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arguments = parse(arg)
        obj_dict = storage.all()

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in obj_dict.keys():
            print("** no instance found **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        elif len(arguments) == 4:
            obj = obj_dict["{}.{}".format(arguments[0], arguments[1])]
            obj[arguments[2]] = arguments[3]
            storage.save()













if __name__ == '__main__':
    HBNBCommand().cmdloop()
