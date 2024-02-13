#!/usr/bin/python3

"""
File: base.py
Description: this module contains one class Base
"""
from json import dumps, loads
import csv
import turtle


class Base:
    """
    This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id == 0 or id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this method returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this method writes the JSON string representation of list_objs
        to a file
        """
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                l_objs = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(l_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        this method returns the list of the JSON string
        representation json_string
        """
        if json_string is None:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        this method returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                inst = cls(1)
            else:
                inst = cls(1, 2)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """
        this method returns a list of instances
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        this method opens a window and draws all the Rectangles and Squares
        """
        my_turtle = turtle.Turtle()
        my_turtle.screen.bgcolor("#000000")
        my_turtle.pensize(4)
        my_turtle.shape("turtle")

        my_turtle.color("#0000FF")
        for rec in list_rectangles:
            my_turtle.showturtle()
            my_turtle.up()
            my_turtle.goto(rec.x, rec.y)
            my_turtle.down()
            for i in range(2):
                my_turtle.forward(rec.width)
                my_turtle.left(90)
                my_turtle.forward(rec.height)
                my_turtle.left(90)
            my_turtle.hideturtle()

        my_turtle.color("FF0000")
        for sq in list_squares:
            my_turtle.showturtle()
            my_turtle.up()
            my_turtle.goto(sq.x, sq.y)
            my_turtle.down()
            for i in range(2):
                my_turtle.forward(sq.width)
                my_turtle.left(90)
                my_turtle.forward(sq.height)
                my_turtle.left(90)
            my_turtle.hideturtle()
