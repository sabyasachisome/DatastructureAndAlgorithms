"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

ref: https://leetcode.com/problems/linked-list-cycle/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        turtle= head
        hare= head
        while(turtle and hare and hare.next):
            turtle= turtle.next
            hare= hare.next.next
            if (turtle==hare):
                return True
        return False

ll_1= ListNode(3)
ll_2= ListNode(2)
ll_3= ListNode(0)
ll_4= ListNode(-4)

ll_1.next= ll_2
ll_2.next= ll_3
ll_3.next= ll_4
ll_4.next= ll_1

sol= Solution()
print(sol.hasCycle(ll_1))