class Node:
    def __init__(self, data):
        self.data= data
        self.previous= None
        self.next= None
    
class DoublyLinkedList:
    def __init__(self):
        self.head= None
        
    def create_list(self, arr):
        start= self.head
        n= len(arr)
        
        temp= start
        i=0
        while(i<n):
            new_node= Node(arr[i])
            if (i==0):
                start= new_node
                temp= start
            else:
                temp.next= new_node
                new_node.prev= temp
                temp= temp.next
            i+=1
        self.head= start
        return start
    
    def count_elements(self):
        temp= self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count
    
    def insert_node(self, value, pos):
        temp= self.head
        count_of_elem= self.count_elements()
        
        #index is 6, count is 5, valid 
        #index is 7, count is 5,
        if (count_of_elem+1<pos):
            return temp
        
        new_node= Node(value)
        
        if (pos==1):
            new_node.next= temp
            temp.previous= new_node
            self.head= new_node
            return self.head
        
        if (pos==count_of_elem+1):
            while(temp.next):
                temp= temp.next
            
            temp.next= new_node
            new_node.previous= temp
            return self.head
        
        i=1
        while(i<pos):
            temp= temp.next
            i+=1
        
        node_at_target= temp.next
        node_at_target.previous= new_node
        new_node.next= node_at_target
        
        temp.next= new_node
        new_node.previous= temp
        
        return self.head
    
    def delete_node(self, pos):
        temp= self.head
        
        count_of_elem= self.count_elements()
        if (count_of_elem<pos):
            return 'delete position {} is greater than list size {}'.format(pos, count_of_elem)
        
        if (pos==1):
            temp= temp.next
            self.head=temp
            return self.head
        
        if(pos==count_of_elem):
            while(temp.next and temp.next.next):
                temp=temp.next
            temp.next= None
            return self.head
        
        i=1
        while(i<pos-1):
            temp= temp.next
            i+=1
        prev_node= temp
        target_node= temp.next
        next_node= target_node.next
        
        next_node.previous= prev_node
        prev_node.next= next_node
        return self.head
    
    def print_list(self):
        temp= self.head
        linked_list= "head=>"
        while(temp.next):
            linked_list+= str(temp.data)+"<=>"
            temp= temp.next
        linked_list+= str(temp.data)
        print(linked_list)

arr= [1,2,3,4,5]
dll= DoublyLinkedList()
dll.create_list(arr)
dll.print_list()
dll.count_elements()

dll.insert_node(6,3)
dll.print_list()
dll.count_elements()

dll.delete_node(2)
dll.print_list()