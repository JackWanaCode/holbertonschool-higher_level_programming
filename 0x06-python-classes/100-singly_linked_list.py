#!/usr/bin/python3
class Node:
    """create Node class"""
    def __init__(self, data, next_node=None):
        """initiallize data and next_node atribute"""
        self.data = data
        self.next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        string = []
        printval = self.head
        while printval is not None:
            string += [str(printval.data)]
            printval = printval.next_node
        return "\n".join(string)

    def sorted_insert(self, value):
        new_node = Node(value, None)
        curr_node = self.head
        pre_node = self.head
        if self.head is None:
            self.head = new_node
        else:
            while curr_node is not None:
                if curr_node.data >= value:
                    new_node.next_node = curr_node
                    if curr_node != pre_node:
                        pre_node.next_node = new_node
                    if curr_node == pre_node:
                        self.head = new_node
                    break
                elif curr_node.next_node is None:
                    curr_node.next_node = new_node
                    break
                pre_node = curr_node
                curr_node = curr_node.next_node
