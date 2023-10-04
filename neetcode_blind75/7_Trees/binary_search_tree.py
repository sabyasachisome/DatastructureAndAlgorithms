class TreeNode:
    def __init__(self, data):
        self.left= None
        self.right= None
        self.data= data
    
    def insert_data(self, data):
        if data< self.data:
            if self.left is None:
                self.left= TreeNode(data)
            else:
                self.left.insert_data(data)
        else:
            if self.right is None:
                self.right= TreeNode(data)
            else:
                self.right.insert_data(data)
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()
