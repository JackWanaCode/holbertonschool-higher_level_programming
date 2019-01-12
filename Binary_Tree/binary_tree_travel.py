#!/usr/bin/python3
Binary_Node = __import__("binary_tree_node").Binary_Node

class Binary_Tree_Travel:
    """create a nice looking printing when travelling"""
    def __init__(self):
        self.root = None

    def inorder_array(self, node, lis=[]):
        if node.left_node is not None:
            self.inorder_array(node.left_node, lis)
        lis.append(node.number)
        if node.right_node is not None:
            self.inorder_array(node.right_node, lis)
        return lis

    def queue_levelorder(self, node, lis1=[], lis2=[]):
        if node.parent_node is None:
            lis1 += list([node])
        if lis1 != []:
            lis2 += list([(lis1.pop(0)).number])
        if node.left_node is not None:
            lis1 += list([node.left_node])
        if node.right_node is not None:
            lis1 += list([node.right_node])
        if lis1 != []:
            self.queue_levelorder(lis1[0], lis1, lis2)
        return (lis2)

    def print_heap(self, node):
        lis = self.queue_levelorder(node)
        i = 0; row = 1; col = 1; idx = 0; ct = 0
        temp_max = 1; check = 1; max = lis[0]; min = lis[0]
        max_digit = 1; count = 0; j = 0
        for el in lis:
            if max < el:
                max = el
            if min > el:
                min = el
        # compare max with min
        if max <= (min * -1):
            max = (min * -1) * 10;
            count += 1
        # find the count of digit and max_digit will be printing
        while max_digit < max:
            max_digit *= 10
            count += 1
        max_digit /= 10
        # calculate row and co that it will be printing
        i = 0
        while i < len(lis):
            row += 1
            i = (i * 2) + 1
        row -= 1
        i = (i - 1) / 2
        col = i * 2 + 1
        #print the dash / number depending on position
        # print("COUNT IS {}", format(count))
        while row > 0:
            check = 1
            ct = 1; j = 0
            while ct <= col and idx < len(lis):
                if ct % (i + 1) == 0 and check == 1:
                    print("[{}".format(lis[idx]), end='')
                    temp_max = max_digit
                    j = count
                    while int(temp_max / (lis[idx] + 1)) != 0:
                        temp_max /= 10
                        j -= 1
                    if lis[idx] < 0:
                        j += 1
                    while j < count:
                        print(" ", end='')
                        j += 1
                    print("]", end='')
                    idx += 1
                    check = 0
                elif ct % (i + 1) == 0 and check == 0:
                    j = 0
                    while j < count:
                        print("-", end='')
                        j += 1
                    check = 1
                else:
                    j = 0
                    while j < count + 1:
                        print("-", end='')
                        j += 1
                ct += 1
            print("")
            row -= 1
            i = (i - 1) / 2
        return lis

    def print_preorder(self, node):
        """print the tree follow pre_order method"""
        if node is None:
            return
        else:
            print(node.number)
            self.print_preorder(node.left_node)
            self.print_preorder(node.right_node)

    def print_inorder(self, node):
        """print the tree follow in_order method"""
        if node is None:
            return
        else:
            self.print_inorder(node.left_node)
            print(node.number)
            self.print_inorder(node.right_node)

    def print_postorder(self, node):
        """print the tree follow pre_order method"""
        if node is None:
            return
        else:
            self.print_postorder(node.left_node)
            self.print_postorder(node.self_node)
            print(node.number)
