class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def add_two_numbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        ans = ListNode(None)
        pointer: ListNode = ans
        carry = 0
        summ = 0

        while(l1 is not None or l2 is not None):
            summ = carry
            if (l1 is not None):
                summ+=l1.val
                l1 = l1.next
            if (l2 is not None):
                summ+=l2.val
                l2 = l2.next
            carry = int(summ/10)
            pointer.next = ListNode(summ%10)
            pointer = pointer.next
        if (carry>0):
            pointer.next = ListNode(carry)

        return ans.next


l1_1= ListNode(9)
l1_2= ListNode(4)
l1_3= ListNode(8)
l1_1.next= l1_2
l1_2.next= l1_3
# l1= 9->4->8
# actual no= 849

l2_1= ListNode(5)
l2_2= ListNode(6)
l2_3= ListNode(4)
l2_1.next= l2_2
l2_2.next= l2_3
# l2= 5->6->4
# actual no= 465

sol= Solution()
sum= sol.add_two_numbers(l1_1,l2_1)

while(sum is not None):
    print(sum.val)
    sum= sum.next