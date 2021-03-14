class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def insert_node(self, val: int, pos: int) -> None:
        # check if pos exceeds linked list length
        if pos> self.get_length()+1:
            raise ValueError('Position exceeds list size')

        # insert at 0
        new_node= Node(val)
        if pos==0:
            new_node.next= self.head
            self.head= new_node
            return

        # insert a new node after the end
        if pos==self.get_length():
            previous_node= self.get_previous_node(pos)
            target_node= previous_node.next
            target_node.next= new_node
            return

        # insert at any position
        if 0<pos<self.get_length()+1:
            previous_node= self.get_previous_node(pos)
            target_node= previous_node.next

            new_node.next= target_node
            previous_node.next= new_node
            return

    # if linked_list= 1=>2=>3=>4=>5, get_length= 5
    def get_length(self) -> int:
        temp = self.head
        counter = 0
        while (temp):
            counter += 1
            temp = temp.next
        return counter

    # prints the previous node
    def get_previous_node(self, pos: int) -> Node:
        temp= self.head
        counter=1
        while(counter<pos-1):
            counter+=1
            temp= temp.next
        return temp

    # prints the list
    def print_list(self)-> str:
        temp= self.head
        list_strn="head=>"
        while(temp.next):
            list_strn+=str(temp.data)+"=>"
            temp= temp.next
        list_strn += str(temp.data)
        print(list_strn)

"""
note:
here, indexing and length of linked_list is implemented similar to list
"""
linked_list= LinkedList()
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
linked_list.head= node1
node1.next= node2
node2.next= node3
node3.next= node4
node4.next= node5

linked_list.print_list()
linked_list.insert_node(7,0)
linked_list.print_list()
linked_list.insert_node(100,6)
linked_list.print_list()
linked_list.insert_node(1000,1)
linked_list.print_list()