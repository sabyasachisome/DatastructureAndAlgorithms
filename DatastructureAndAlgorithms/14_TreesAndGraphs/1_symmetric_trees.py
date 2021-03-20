# class Node:
# #     def __init__(self, data):
# #         self.data= data
# #         self.left= None
# #         self.right= None
# #
# # class Solution:
# #     def is_mirror(self, node1, node2):
# #         if node1 is None and node2 is None:
# #             return True
# #         if node1 is None or node2 is None:
# #             return False
# #         return (node1.data==node2.data) and self.is_mirror(node1.left, node1.right) and self.is_mirror(node1.right, node1.left)
# #
# #     def is_symmetric(self, root: Node)-> bool:
# #         return self.is_mirror(root, root)
# #
# #
# # sol= Solution
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        stk= [root.left,root.right]
        while(stk):
            left= stk.pop()
            right = stk.pop()
            if left is None and right is None:
                pass
            elif left is None or right is None or left.val!= right.val:
                return False
            else:
                stk.append(left.left)
                stk.append(right.right)
                stk.append(right.left)
                stk.append(left.right)
        return True
"""
        1
       /  \
      2    2
     / \   / \
    3   4 4   3
"""
[1,2,2,3,4,4,3]
sol = Solution()
node1= TreeNode(1)
node2= TreeNode(2)
node3= TreeNode(2)
node4= TreeNode(3)
node5= TreeNode(4)
node6= TreeNode(4)
node7= TreeNode(3)
node1.left= node2
node1.right= node3
node2.left= node4
node2.right= node5
node3.left= node6
node3.right= node7
print(sol.isSymmetric(node1))