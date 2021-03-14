class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        self.previous= None

class LinkedList:
    def __init__(self):
        self.head= None

    # creating linked list from an array
    def create_list(self, arr):
        arr_len= len(arr)
        ctr=0
        while(ctr<arr_len):
            new_node = Node(arr[ctr])
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

    def get_previous(self, pos):
        temp= self.head
        counter=1
        while(counter<=pos-1):
            temp= temp.next
            counter+=1
        return temp

    def get_length(self):
        temp= self.head
        counter=0
        while(temp):
            temp= temp.next
            counter+=1
        return counter

    def print_list(self):
        temp= self.head
        list_strn= "head=>"
        while(temp.next):
            list_strn+=str(temp.data)+"<=>"
            temp= temp.next
        list_strn += str(temp.data)
        print(list_strn)

linked_list= LinkedList()
arr=[1,2,3,4,5]

linked_list.create_list(arr)
linked_list.print_list()