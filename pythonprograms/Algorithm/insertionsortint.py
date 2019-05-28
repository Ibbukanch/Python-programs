# Program for insertion Sort integer
from array import *
from Bridgelabz.pythonprograms.Algorithm.util import insertionsortinteger

if __name__ == "__main__":

    # Take input from user
    n=int(input("Enter the no.of Elements\n"))
    # Creating the integer Array
    arr = array('i',[])
    print("Enter the no of elements")
    for i in range(n):
        arr.append(int(input()))   # Appending elements to the List
    arr = insertionsortinteger(arr)
    # display the Sorted Array

    for i in range(len(arr)):
        print(arr[i],end=" ")
