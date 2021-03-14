class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def delete_node(self, value):
        # if value is 0th element
        if self.head.data== value:
            self.head= self.head.next
            return

        # check for value till end
        # if get value, then delete
        temp= self.head
        while(temp.next.data!=value):
            temp= temp.next
        previous_node= temp
        
        next_node= previous_node.next.next
        previous_node.next= next_node
        temp= None
        return

    def print_list(self) -> None:
        temp= self.head
        list_strn= "head=>"
        while(temp.next):
            list_strn+=str(temp.data)+"=>"
            temp= temp.next
        list_strn+=str(temp.data)
        print(list_strn)

linked_list= LinkedList()
node1= Node(1)
node2= Node(2)
node3= Node(3)
node4= Node(4)
node5= Node(5)
linked_list.head= node1
node1.next= node2
node2.next= node3
node3.next= node4
node4.next= node5

linked_list.print_list()
linked_list.delete_node(3)
linked_list.print_list()