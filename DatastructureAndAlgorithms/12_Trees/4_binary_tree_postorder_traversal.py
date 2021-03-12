class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

"""
                4
            /       \
           5         6
         /   \      /  \
        7    None  None None
       / \
    None  None    
"""


def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

root= Node(4)
root.left=Node(5)
root.right=Node(6)
root.left.left=Node(7)

postorder(root)