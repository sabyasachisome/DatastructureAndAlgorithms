class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def print_list(self):
        temp= self.head
        strn="head=>"
        while(temp.next):
            strn+=str(temp.data)+"=>"
            temp= temp.next
        strn+=str(temp.data)
        print(strn)

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