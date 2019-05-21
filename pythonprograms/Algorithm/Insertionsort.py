from array import *
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(0, len(arr)-1):

        key = arr[i+1]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

list=[]
n=int(input("Enter the no of strings\n"))
print("Enter the Strings")
for i in range(n):
    list.append(input())
insertionSort(list)
print("Sorted array is:")
for i in range(len(list)):
    print(list[i])
