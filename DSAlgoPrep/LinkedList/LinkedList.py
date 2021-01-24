class Node:
    def __init__(self, data):
        self.data=data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head= None
        
    def insert_node(self, val, pos):
        target= Node(val)
        if pos==0:
            target.next= self.head
            self.head= target
            return
        else:
            previous_node= self.get_value(pos-1)
            target.next= previous_node.next
            previous_node.next= target
            
    def delete_node(self, key):
        temp= self.head
        if(temp is None):
            return
        if (temp.data==key):
            self.head= temp.next
            temp= None
            return
        
        while(temp.next.data!= key):
            temp= temp.next
        
        target_node= temp.next
        temp.next= target_node.next
        target_node.next= None
        
    
    def get_value(self, pos):
        counter=0 #head starts=0, counter= 1 if head starts=1
        temp= self.head
        while(counter<pos):
            temp= temp.next
            counter+=1
        return temp
    
    def print_list(self):
        temp= self.head
        list_str= "head=>"
        while(temp.next):
            list_str+= str(temp.data)+"=>"
            temp= temp.next
        list_str+= str(temp.data)
        print(list_str)

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

# print list
linked_list.print_list()

# get value at position
# linked_list.get_value(3)

#insert node
linked_list.insert_node(10,2)
linked_list.insert_node(20,2)
linked_list.print_list()

# delete node
linked_list.delete_node(10)
linked_list.print_list()