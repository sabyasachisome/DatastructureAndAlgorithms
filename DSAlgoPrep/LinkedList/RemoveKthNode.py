class ListNode:
    def __init__(self, data):
        self.data= data
        self.next= None

class Solution:
    def delete_nth_from_last(self, head: ListNode, n: int) -> ListNode:
        ans= ListNode(0)
        ans.next= head

        first= ans
        second= ans

        for i in range(1, n+2):
            first= first.next

        while(first is not None):
            first= first.next
            second= second.next

        second.next= second.next.next
        return ans.next

    def print_list(self, head: ListNode) -> None:
        while (head):
            print(head.data)
            head = head.next

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

s.print_list(ll_1)
new_head= s.delete_nth_from_last(ll_1,2)
print()
s.print_list(new_head)