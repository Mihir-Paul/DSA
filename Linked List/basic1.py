class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head 
            while curr.next is not None:
                curr = curr.next 
            curr.next = new_node 

    def traversal(self):
        if self.head is None:
            print("Single Linked List is Empty")

        else:
            curr = self.head 
            while curr is not None:
                print(curr.data,end =' ')
                curr = curr.next 
            print()

    def insert(self,index,data):
        new_node = Node(data)
        if index==0:
            new_node.next = self.head 
            self.head = new_node
        else:
            curr = self.head 
            prev_node = None
            count = 0
            while curr is not None and count < index:
                prev_node = curr
                curr = curr.next
                count+=1
            prev_node.next = new_node
            new_node.next = curr

    def delete(self,data):
        temp = self.head 
        if temp.next is not None:
            if temp.data == data:
                self.head = temp.next 
                return 
            else:
                found = False 
                prev =  None 
                while temp is not None:
                    if temp.data == data:
                        found = True 
                        break 
                    prev = temp 
                    temp = temp.next 

                if found:
                    prev.next = temp.next 
                    return 
                else:
                    print("Not Found")




ll = LinkedList()
ll.append(40)
ll.append(50)
ll.append(80)
ll.append(70)
ll.append(60)
ll.insert(3,90)
ll.delete(70)
ll.traversal()

        
