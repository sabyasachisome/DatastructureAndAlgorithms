class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

def insert_node(root: Node, node: Node) -> None:
        if root is None:
            root= node
            return
        if root.data<node.data:
            if root.right is None:
                root.right=node
            else:
                insert_node(root.right, node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert_node(root.left, node)

def minimum_value(node):
    while node.left is not None:
        node= node.left
    return node

def delete_node(root: Node, key)-> None:
    if root is None:
        return root
    if key< root.data:
        return delete_node(root.left, key)
    elif key>root.data:
        return delete_node(root.right, key)
    else:
        if root.left is None:
            temp=root.right
            root= None
            return temp
        elif root.right is None:
            temp= root.left
            root= None
            return temp
        temp= minimum_value(root.right)
        root.data= temp.data
        root.right= delete_node(root.right, temp.data)

def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

"""
        5
      /   \
    3       7
   / \      / \
  2   4    6    8
"""

root_node= Node(5)
insert_node(root_node, Node(3))
insert_node(root_node, Node(2))
insert_node(root_node, Node(4))
insert_node(root_node, Node(7))
insert_node(root_node, Node(6))
insert_node(root_node, Node(8))
preorder(root_node)
print('After delete')
delete_node(root_node, 7)
preorder(root_node)