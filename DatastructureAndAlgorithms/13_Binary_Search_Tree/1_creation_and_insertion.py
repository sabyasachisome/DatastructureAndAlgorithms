class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

def insert(root: Node, node: Node) -> None:
    if root is None:
        root= node
        return
    if root.data<node.data:
        if root.right is None:
            root.right= node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left= node
        else:
            insert(root.left, node)

def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

tree= Node(5)
insert(tree, Node(6))
insert(tree, Node(20))
insert(tree, Node(1))
preorder(tree)