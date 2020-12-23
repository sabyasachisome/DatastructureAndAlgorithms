"""
Linked List
"""
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def printList(self):
        temp= self.head
        linked_list="head=> "
        while(temp.next):
            linked_list+= str(temp.data)+" => "
            temp= temp.next
        linked_list+= str(temp.data)+""
        print(linked_list)

    def getPrevious(self, pos):
        temp= self.head
        counter=1
        while(counter<pos):
            temp= temp.next
            counter+=1
        return temp

    def insertNode(self, value, pos):
        target= Node(value)
        if (pos==0):
            target.next= self.head
            self.head= target
        else:
            previous= self.getPrevious(pos)
            nextNode= previous.next

            previous.next= target
            target.next= nextNode

# create the linkedList
linked_list= LinkedList()

# create nodes
node1= Node(5)
node2= Node(6)
node3= Node(7)
node4= Node(8)

# link them
linked_list.head= node1
node1.next=node2
node2.next=node3
node3.next=node4

# print data
linked_list.printList()

linked_list.insertNode(10,0)
linked_list.printList()

linked_list.insertNode(11,2)
linked_list.printList()

linked_list.insertNode(12,1)
linked_list.printList()