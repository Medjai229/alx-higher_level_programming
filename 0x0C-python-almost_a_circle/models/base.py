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
        if list_dictionaries is None:
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
        """
        this method serializes into a csv file
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Sqaure":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]

                csv_write = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    csv_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This method returns a list of classes instantiated from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                        dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts
                        ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw all the Rectangles and Squares using Turtle graphics.

        Args:
        -   list_rectangles (list): A list of Rectangle instances.
        -   list_squares (list): A list of Square instances.
        """
        # Create a turtle screen
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Create a turtle object
        painter = turtle.Turtle()
        painter.speed(1)
        painter.pensize(2)
        # draw the squares
        for sq in list_squares:
            print(sq)
            painter.color("red")
            painter.penup()
            painter.goto(sq.x, sq.y)
            painter.pendown()
            for _ in range(4):
                painter.forward(sq.size)
                painter.left(90)

        # draw the rectangles
        for rect in list_rectangles:
            print(rect)
            painter.penup()
            painter.goto(rect.x, rect.y)
            painter.pendown()
            for _ in range(2):
                painter.color("indigo")
                painter.forward(rect.width)
                painter.left(90)
                painter.forward(rect.height)
                painter.left(90)

        screen.exitonclick()
