from collections import defaultdict
from typing import List

class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

def insert_node(root: Node, node: Node):
    if root is None:
        root= node
        return
    if root.data<node.data:
        if root.right is None:
            root.right= node
        else:
            insert_node(root.right, node)
    else:
        if root.left is None:
            root.left= node
        else:
            insert_node(root.left, node)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

tree= Node(5)
insert_node(tree, Node(6))
insert_node(tree, Node(20))
insert_node(tree, Node(1))
preorder(tree)