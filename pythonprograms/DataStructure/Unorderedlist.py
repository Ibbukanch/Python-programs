from Bridgelabz.pythonprograms.DataStructure.linklist import LinkedList,Node

if __name__ == "__main__":
    # Creating the object of LinkedList
    linkedList = LinkedList()
    # Read the file
    with open('/home/user/Desktop/data') as f:
        lists = f.read().split()
    # Insert element to linkedlist
    for i in range(len(lists)):
        linkedList.insert(Node(lists[i]))
    # Display the Linkedlist
    linkedList.printList()
    # take the word from user for searching
    word = input("\nEnter the word you want to search\n")
    # Delete the word if found,otherwise insert it into linkedlist
    check = linkedList.deleteelement(word)
    if check == 0:
        linkedList.insert(Node(word))
        lists.append(word)
    else:
        lists.remove(word)
    # Display the list
    linkedList.printList()
    # Update the file
    with open('/home/user/Desktop/data', 'w') as f:
        for item in lists:
            f.write("%s " % item)