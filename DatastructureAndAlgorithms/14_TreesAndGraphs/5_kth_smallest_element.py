"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def create_bt(self, arr, root, arr_len, i):
        if i<arr_len:
            temp= TreeNode(arr[i])
            root= temp
            root.left= self.create_bst(arr, root.left, arr_len, 2*i+1)
            root.right = self.create_bst(arr, root.right, arr_len, 2*i+2)
        return root

    def create_bst(self, arr):
        if not arr:
            return None
        mid= len(arr)//2
        root= TreeNode(arr[mid])
        root.left= self.create_bst(arr[:mid])
        root.right = self.create_bst(arr[mid+1:])
        return root


    def bst_insert_node(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if root is None:
            root= node
            return
        if root.val < node.val:
            if root.right is None:
                root.right= node
            else:
                self.bst_insert_node(root.right, node)
        else:
            if root.left is None:
                root.left= node
            else:
                self.bst_insert_node(root.left, node)


    def preorder(self, root):
        if root is not None:
            print(root.val,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        pass

sol= Solution()
arr=[3,1,4,None,2]
arr=[4,2,5,1,6]
# root_bst= TreeNode(arr[0])
# for i in range(1, len(arr)):
#     sol.bst_insert_node(root_bst, TreeNode(arr[i]))
# sol.preorder(root_bst)
arr.sort()
root= sol.create_bst(arr)
sol.preorder(root)