from Bridgelabz.pythonprograms.DataStructure.linklist import LinkedList,Node
from array import *
def takenumber():
    # Takes the number from user for searching
    n = int(input("Enter number : "))
    check = list[n % 11].deleteelement(n)
    if check == 0:
        list[n % 11].insertappropriate(Node(n))
        arr.append(n)
    else:
        arr.remove(n)
def display_hash():
    #Display data from linked list on console
    for i in range(11):
        if list[i].isempty():
            print(i,":")
            continue
        print(i, ":", end="")
        list[i].printList()
        print()

# Declaring an Empty list
list = []
arr = array('i',[])
# Creating 11 Linked list objects and storing into list
for i in range(11):
    list.append(LinkedList())
# Reads the File
with open('/home/user/Desktop/elements') as f:
   number = f.read().split()
for i in range(len(number)):
    arr.append(int(number[i]))
# Inserting number to linked list
for i in arr:
    rem = i % 11
    list[rem].insert(Node(i))
    list[rem].sort()
display_hash()
takenumber()
display_hash()
# Updating the list
with open('/home/user/Desktop/elements', 'w') as f:
    for item in arr:
        f.write("%d " % item)