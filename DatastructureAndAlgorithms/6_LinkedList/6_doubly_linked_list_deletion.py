from typing import List
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        self.previous= None

class LinkedList:
    def __init__(self):
        self.head= None

    def create_list(self, arr: List)-> Node:
        arr_len: int= len(arr)
        ctr: int=0
        while(ctr<arr_len):
            new_node= Node(arr[ctr])
            if ctr==0:
                start= new_node
                temp= start
            else:
                temp.next= new_node
                new_node.previous= temp
                temp= temp.next
            ctr+=1
        self.head= start
        return self.head

    def delete_node(self, value)-> None:
        # delete at 0th position
        if self.head.data==value:
            self.head= self.head.next
            return

        # delete at any other position
        temp= self.head
        while(temp.next.data!=value):
            temp= temp.next
        previous_node= temp
        next_node= previous_node.next.next
        previous_node.next= next_node
        next_node.previous= previous_node

    def print_list(self)-> None:
        temp: Node= self.head
        list_strn: str= "head=>"
        while(temp.next):
            list_strn+= str(temp.data)+"<=>"
            temp= temp.next
        list_strn += str(temp.data)
        print(list_strn)

linked_list= LinkedList()
arr=[1,2,3,4,5]
linked_list.create_list(arr)
linked_list.print_list()
linked_list.delete_node(3)
linked_list.print_list()