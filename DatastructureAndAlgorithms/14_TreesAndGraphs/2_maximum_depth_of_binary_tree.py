"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class Node:
    def __init__(self, data):
        self.left=self.right= None
        self.data= data

class BinaryTree:
    def insert_node(self, arr, root, i, n):
        if i<n:
            temp= Node(arr[i])
            root= temp

            root.left= self.insert_node(arr, root.left, 2*i+1, n)
            root.right= self.insert_node(arr, root.right, 2*i+2, n)
        return root

    def maximum_depth(self, node):
        if node is None:
            return 0
        else:
            left_height= self.maximum_depth(node.left)
            right_height = self.maximum_depth(node.right)
            if left_height>right_height:
                return left_height+1
            else:
                return right_height+1

    def preorder(self, root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


arr= [1,2,2,3,4,4,3]
"""
        1
       /  \
      2    2
     / \   / \
    3   4 4   3
"""
bt= BinaryTree()
root= bt.insert_node(arr, None, 0, len(arr))
# bt.preorder(root)
print(bt.maximum_depth(root))