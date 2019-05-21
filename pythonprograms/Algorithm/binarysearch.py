# Program of binary Search
#Create binarySearch Function

def binarysearch(lists,word):

    # Sort the list
    lists.sort()
    lb=0
    ub=len(lists)-1
    while lb <= ub:
        middle = (lb+ub) // 2
        if lists[middle].casefold() == word.casefold():
            return 1
        elif word.casefold() > lists[middle].casefold():
            lb=middle+1
        else:
            ub=middle-1
    return 0

#Open the file

with open('/home/user/Desktop/data') as f:
   lists = f.read().split()

# Taking input from user to search word in list

word=input("Enter the word you want to search\n")
z=binarysearch(lists,word)
if z==1:
    print("WORD FOUND")
else:
    print("WORD NOT FOUND")
