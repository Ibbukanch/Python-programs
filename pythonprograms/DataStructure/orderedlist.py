from Bridgelabz.pythonprograms.DataStructure.linklist import LinkedList,Node
from array import *
# Creating the object of LinkedList
orderedlist = LinkedList()
arr = array('i',[])
# Reading the file
with open('/home/user/Desktop/elements') as f:
   Numlists = f.read().split()
for i in range(len(Numlists)):
    arr.append(int(Numlists[i]))
# Inserting elements from file to linkedList
for i in range(len(arr)):
    orderedlist.insert(Node(arr[i]))
# Checking whether the Linked List is empty or Not,if not then we sort the list
if orderedlist.isempty() == 0:
    orderedlist.sort()
    print("\nSorted Linked List:")
    orderedlist.printList()
# Takes the element from user for Searching
element=int(input("\nEnter the element you want to search:"))
# If element found then delete it or insert it at an appropriate position
check = orderedlist.deleteelement(element)
if check == 0:
    orderedlist.insertappropriate(Node(element))
    arr.append(element)
else:
    arr.remove(element)
# Display the list
orderedlist.printList()
# Updatethe file
with open('/home/user/Desktop/elements', 'w') as f:
    for item in arr:
        f.write("%d " % item)