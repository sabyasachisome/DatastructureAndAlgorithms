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
root= Node(4)
root.left=5
root.right=6
root.left.left=7