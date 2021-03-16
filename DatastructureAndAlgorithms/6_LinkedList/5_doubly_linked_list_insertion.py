class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        self.previous= None

class LinkedList:
    def __init__(self):
        self.head= None

    def insert(self, pos, val):
        # node exceeds size of list
        if pos>self.get_length():
            raise ValueError('Position exceeds list size')

        # node is 0th position
        new_node= Node(val)
        temp= self.head
        if pos==0:
            new_node.next= self.head
            self.head.previous= new_node
            self.head= new_node
            return

        # node is after the end position
        if pos==self.get_length():
            while temp.next:
                temp= temp.next
            # print(temp.data)
            temp.next= new_node
            new_node.previous= temp
            return

        # node is anywhere in between
        if 0<pos<self.get_length():
            counter=0
            while(counter<pos):
                temp= temp.next
                counter+=1
            previous_node=temp.previous

            previous_node.next= new_node
            new_node.previous= previous_node
            new_node.next=temp
            temp.previous=new_node
            return

    def get_length(self):
        counter=0
        temp= self.head
        while(temp):
            counter+=1
            temp= temp.next
        return counter

    def print_list(self) -> None:
        list_strn= "head=>"
        temp= self.head
        while(temp.next):
            list_strn+=str(temp.data)+"<=>"
            temp= temp.next
        list_strn += str(temp.data)
        print(list_strn)

linked_list= LinkedList()
node1= Node(1)
node2= Node(2)
node3= Node(3)
node4= Node(4)
node5= Node(5)
linked_list.head= node1
node1.next= node2
node2.previous= node1
node2.next= node3
node3.previous= node2
node3.next= node4
node4.previous= node3
node4.next= node5
node5.previous= node4
linked_list.print_list()

print(linked_list.get_length())
linked_list.insert(0,100)
linked_list.print_list()
print(linked_list.get_length())
linked_list.insert(6,100)
linked_list.print_list()
linked_list.insert(5,1000)
linked_list.print_list()
# linked_list.insert(76,1000)