# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node= None
        while(head != null ):
            next= head.next
            head.next= node
            node= head
            head= next
        return node

s= Solution()
ll_1= ListNode(1)
ll_2= ListNode(2)
ll_3= ListNode(3)
ll_4= ListNode(4)
ll_5= ListNode(5)
ll_1.next= ll_2
ll_2.next= ll_3
ll_3.next= ll_4
ll_4.next= ll_5
reversed_head= s.reverseList(ll_1)

# print the reversed list
reversed_list= ""
while(reversed_head.next):
    reversed_list+=str(reversed_head.val)+"=>"
    reversed_head=reversed_head.next
reversed_list+=str(reversed_head.val)
print(reversed_list)