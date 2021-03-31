"""
Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def create_bt(self, arr, root, i, arr_len):
        if i<arr_len:
            root= TreeNode(arr[i])
            root.left= self.create_bt(arr, root.left, 2*+i+1, arr_len)
            root.right = self.create_bt(arr, root.left, 2*+i+2, arr_len)
        return root

    def preorder(self, root):
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.serialize_strn= self.inorder_serialize(root)
        return self.serialize_strn

    def inorder_serialize(self, root):
        if root is None or root.val is None:
            return 'X#'
        left_serialized_strn= self.inorder_serialize(root.left)
        right_serialized_strn= self.inorder_serialize(root.right)
        return str(root.val)+'#'+left_serialized_strn+right_serialized_strn

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pass

arr= [1,2,3,None,None,4,5]

# Your Codec object will be instantiated and called as such:
ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# ser.serialize()
root= ser.create_bt(arr, None, 0, len(arr))
ser.preorder(root)
strn =ser.serialize(root)
print(strn)