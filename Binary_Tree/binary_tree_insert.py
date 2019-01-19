#!/usr/bin/python3
Binary_Node = __import__('binary_tree_node').Binary_Node
Binary_Tree_Travel = __import__("binary_tree_travel").Binary_Tree_Travel

class Binary_Tree_Insert(Binary_Tree_Travel):
    """create Insert Node"""
    def __init__(self):
        super().__init__()

    def print_tree(self, node):
        if node is None:
            return
        else:
            print(node.number)
            self.print_tree(node.left_node)
            self.print_tree(node.right_node)

    def insert(self, value):
        """insert new node"""
        new_node = Binary_Node(value, None, None, None)
        if self.root is None:
            self.root = new_node
        else:
            self.parent_node = self.root
        return new_node

    def insert_left(self, value, node=None):
        """insert to the left"""
        new_node = Binary_Node(value, None, None, None)
        if node is None:
            raise ValueError("root must be exist")
        else:
            new_node.parent_node = node
            if node.left_node is None:
                node.left_node = new_node
            else:
                node.left_node.parent_node = new_node
                node.left_node = new_node
        return new_node

    def insert_right(self, value, node=None):
        """insert to the right"""
        new_node = Binary_Node(value, None, None, None)
        if node is None:
            raise ValueError("root must be exist")
        else:
            new_node.parent_node = node
            if node.right_node is None:
                node.right_node = new_node
            else:
                node.right_node.parent_node = new_node
                node.right_node = new_node
        return new_node
