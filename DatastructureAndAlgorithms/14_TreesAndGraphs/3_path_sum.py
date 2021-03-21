"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def create_binary_tree(self, root, arr, arr_len, ctr):
        if ctr<arr_len:
            root= TreeNode(arr[ctr])
            root.left= self.create_binary_tree(root.left, arr, arr_len, 2*ctr+1)
            root.right = self.create_binary_tree(root.right, arr, arr_len, 2*ctr+2)
        return root

    def has_sum(self, root,targetSum, cur):
        if root is None:
            return False
        else:
            cur+=root.val
            if cur==targetSum and root.left is None and root.right is None:
                return True
            return (self.has_sum(root.left, targetSum, cur) or self.has_sum(root.right, targetSum, cur))

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.has_sum(root,targetSum, 0)

    def preorder(self,root):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

# arr=[5,4,8,11,None,13,4,7,2,None,None,None,1]
arr= [1,2,2,3,4,4,3]
sol= Solution()
root=sol.create_binary_tree(None, arr, len(arr), 0)
sol.preorder(root)
print(sol.hasPathSum(root, 10))