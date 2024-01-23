#!/usr/bin/python3
"""Classes for singly linked list"""


class Node:
    """a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Constructor

        Args:
            data: the data of the node
            next_node: the next node of the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """set the next node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """initalize a singly linked list"""

    def __init__(self):
        """Consturctor

        Args:
            head: the first node of the list
        """
        self.__head = None

        def sorted_insert(self, value):
            """Insert a new node to the list

            Args:
                value: the new node to insert:
            """
            new = Node(value)
            if self.__head is None:
                new.next_node = None
                self.__head == new
            elif self.__data > value:
                new.next_node = self.__head
                self.__head = new
            else:
                tmp = self.__head
                while (tmp.next_node is not None and
                        tmp.next_node.data < value):
                    tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

    def __str__(self):
        """ defind the print() representation of a singly linked list"""
        values = []
        tmp = self.__head

        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        
        return ("\n".join(values))
