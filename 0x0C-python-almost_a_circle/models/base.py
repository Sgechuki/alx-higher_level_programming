#!/usr/bin/python3
"""This module holds the Base class"""
import json
import os
import csv


class Base:
    """will be the “base” of all other classes
    in this project
    Args
        id (int, optional): public instance attribute
    Class attr
        __nb_objects (int): private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance with attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of list_objs to a file"""
        string = []
        if list_objs is None:
            pass
        else:
            for item in list_objs:
                string.append(item.to_dictionary())
        json = Base().to_json_string(string)
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return list()
        else:
            obj = json.loads(json_string)
            return obj

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes
        already set"""
        if cls.__name__ == "Rectangle":
            inst = cls(1, 2)
        elif cls.__name__ == "Square":
            inst = cls(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        l_inst = []
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                obj = cls.from_json_string(f.read())
                for i in obj:
                    inst = cls.create(**i)
                    l_inst.append(inst)
        return l_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize to csv"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            header = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            header = ['id', 'size', 'x', 'y']
        with open(filename, "w", newline="") as f:
            csv_writer = csv.DictWriter(f, fieldnames=header)
            csv_writer.writeheader()
            for obj in list_objs:
                csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv"""
        l_inst = []
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                rows = [row for row in reader]
                rows = [{ky: int(val)for ky, val in row.items()}
                        for row in rows]
                for dic in rows:
                    l_inst.append(cls.create(**dic))
        return l_inst
