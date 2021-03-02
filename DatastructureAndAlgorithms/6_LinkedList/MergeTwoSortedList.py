"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""""

import numpy as np
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head= None

    def create_list(self, arr):
        start= self.head
        arr_len= len(arr)
        temp= start
        arr_ptr= 0
        while(arr_ptr<arr_len):
            new_node= ListNode(arr[arr_ptr])
            if arr_ptr==0:
                start= new_node
                temp= start
            else:
                temp.next= new_node
                temp= temp.next
            arr_ptr+=1
        self.head= start
        return self.head

    def __str__(self):
        temp= self.head
        linked_list= "head=>"
        while(temp.next):
            linked_list+=str(temp.val)+"=>"
            temp= temp.next
        linked_list += str(temp.val)
        return linked_list

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        soln = cur
        while (l1 and l2):
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while (l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while (l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return soln.next

arr1= np.array([1,2,4,7,8,100])
ll1= LinkedList()
l1_1= ll1.create_list(arr1)

arr2= np.array([1,3,4])
ll2= LinkedList()
l2_1= ll1.create_list(arr2)


s= Solution()
merged_list= s.mergeTwoLists(l1_1,l2_1)

def print_list(merged_list):
    list_strn= ""
    while(merged_list.next):
        list_strn+= str(merged_list.val)+"=>"
        merged_list= merged_list.next
    list_strn += str(merged_list.val)
    print(list_strn)
print_list(merged_list)