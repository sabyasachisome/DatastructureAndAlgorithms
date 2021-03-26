"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binary_tree(self, arr: List[int], root:TreeNode, arr_len: int, i: int)-> TreeNode:
        if i<arr_len:
            root= TreeNode(arr[i])
            root.left= self.binary_tree(arr, root.left, arr_len, 2*i+1)
            root.right = self.binary_tree(arr, root.right, arr_len, 2*i+2)
        return root

    def preorder(self, root: TreeNode):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root is None):
            return None
        if (root.val == p.val or root.val == q.val):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left is None and right is None):
            return None
        if (left is not None and right is not None):
            return root
        if (left is None):
            return right
        return left

sol= Solution()
# arr= [3,5,1,6,2,0,8,None,None,7,4]
# arr=[1,2,3,4,5,6]
arr=[1,2,3,4,5,6,7]
root= sol.binary_tree(arr, None, len(arr), 0)
sol.preorder(root)
print(sol.lowestCommonAncestor(TreeNode(2),TreeNode(4),TreeNode(5)))