class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None

# insert the node at the end
    def insert(self,newNode):

        if self.head is None:
            self.head = newNode
        else:
            q=self.head
            while q.next is not None:
                q=q.next
            q.next=newNode

 # insert the node at the beginning
    def inserbeg(self,newNode):
        newNode.next = self.head
        self.head = newNode

 # insert the node at appropriate position
    def insertappropriate(self,newNode):
        if self.head is None:
            self.head = newNode
            return
        q = self.head
        if q.data >= newNode.data:
            newNode.next = q
            self.head = newNode
            return

        while q.next is not None:
            if q.next.data >= newNode.data:
                newNode.next = q.next
                q.next = newNode
                return
            else:
                q = q.next
        q.next = newNode

# Prints the LinkedLIst
    def printList(self):
        if self.isempty():
            print("Linked List empty")
        else:
            q=self.head
            while q is not None:
                print(q.data,end=" ")
                q=q.next

# Deletesthe element if Found otherwise adds element to Linked List
    def deleteelement(self,ele):

        if self.isempty():
            return 0
        if self.head.data == ele:
             self.head = self.head.next
             return
        q = self.head
        while q.next is not None:
            if q.next.data == ele:
                break
            else:
                q = q.next
        if q.next is None:
            print("ele not found and added in to the list")
            return 0
        else:
            q.next = q.next.next

# Deletes the element in the beginning
    def deletebeg(self):
        if self.isempty():
            print("Linked List Empty")
        p = self.head
        self.head = self.head.next
        return p.data

# Deletes the element at the end
    def deleteend(self):
        if self.isempty():
            print("Linked List Empty")
        if self.head.next is None:
            p = self.head
            self.head = None
        else:
            q = self.head
            while q.next.next is not None:
                q = q.next
            p = q.next
            q.next = None
        return p.data

# Sorts the LinkedList
    def sort(self):
        i = self.head
        while i.next is not None:
            j = self.head

            while j.next is not None:
                if j.data > j.next.data:
                    j.data,j.next.data = j.next.data,j.data
                j= j.next
            i = i.next
# Returns the size of LinkedList
    
    def Size(self):
        countnodes = self.head
        count = 0
        while countnodes is not None:
            count = count + 1
            countnodes = countnodes.next
        return count

# ----------------Checks whether the Linked List is Empty or Not--------------------------#

    def isempty(self):
        if self.head is None:
            return 1
        else:
            return 0

#----------Function to return the stacktop--------#

    def stacktos(self):
        stacktos = self.head
        if stacktos is None:
            return -1
        while stacktos.next is not None:
            stacktos = stacktos.next
        return stacktos.data














