#!/usr/bin/python3
"""Defines the console."""

import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Does nothing when receiving an empty line."""
        pass

    def default(self, arg):
        """Default for command module when input is invalid."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arguments = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arguments[1])
            if match is not None:
                command = [arguments[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arguments[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new class instance and print the id."""
        arguments = parse(arg)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arguments[0])().id)
            FileStorage().save()

    def do_show(self, arg):
        """Displays the string representation of a class instance."""
        arguments = parse(arg)
        obj_dict = FileStorage().all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arguments[0], arguments[1])])

    def do_destroy(self, arg):
        """Deletes a class instance of a given id."""
        arguments = parse(arg)
        obj_dict = FileStorage().all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arguments[0], arguments[1])]
            FileStorage().save()

    def do_all(self, arg):
        """Displays string representations of all instances of a given class."""
        arguments = parse(arg)
        if len(arguments) > 0 and arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        storage_instance = FileStorage()
        objects = []
        for obj in storage_instance.all().values():
            if len(arguments) == 0 or arguments[0] == obj.__class__.__name__:
                objects.append(obj.__str__())
        print(objects)

    def do_count(self, arg):
        """Retrieves the number of instances of a given class."""
        arguments = parse(arg)
        count = 0
        for obj in FileStorage().all().values():
            if arguments[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates a class instance of a given id."""
        arguments = parse(arg)
        obj_dict = FileStorage().all()

        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arguments) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arguments[0], arguments[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arguments) == 2:
            print("** attribute name missing **")
            return False
        if len(arguments) == 3:
            try:
                type(eval(arguments[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arguments) == 4:
            obj = obj_dict["{}.{}".format(arguments[0], arguments[1])]
            if arguments[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arguments[2]])
                obj.__dict__[arguments[2]] = valtype(arguments[3])
            else:
                obj.__dict__[arguments[2]] = arguments[3]
        elif type(eval(arguments[2])) == dict:
            obj = obj_dict["{}.{}".format(arguments[0], arguments[1])]
            for k, v in eval(arguments[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        FileStorage().save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
