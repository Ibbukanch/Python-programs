# Program of bubble sort
from array import *
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    # Creating the Array
    arr = array('i',[])
    # Taking input from user
    n=int(input("Enter the no.of elements\n"))
    print("Enter the elements\n")
    for i in range(n):
        arr.append(int(input()))  # Appending elements into the array
    bubbleSort(arr)               # Calling the function

    print("Sorted array is:")
    # display the sorted Array
    for i in range(len(arr)):
        print("%d" % arr[i]),
