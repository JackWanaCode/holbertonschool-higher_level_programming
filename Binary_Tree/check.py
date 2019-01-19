#!/usr/bin/python3
Binary_Tree_Insert = __import__('binary_tree_insert').Binary_Tree_Insert

root = Binary_Tree_Insert()
node = root.insert(98)
root.insert_left(12, node)
root.insert_right(402, node)
root.insert_left(6, node.left_node)
root.insert_right(56, node.left_node)
root.insert_left(256, node.right_node)
root.insert_right(512, node.right_node)

# print(node.number)
# print(node.left_node.number)
# print(node.right_node.number)
# root.print_inorder(node)

# print(lis)
lis = root.print_heap(node)
# lis = root.queue_levelorder(node)
for el in lis:
    print(el)
# print(root.inorder_array(node))
