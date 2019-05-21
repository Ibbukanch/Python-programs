# Program for insertion Sort integer
from array import *
from com.Bridgelabz.Algorithm.util import insertionsortinteger
# Take input from user
n=int(input("Enter the no.of Elements\n"))
arr = array('i',[])
print("Enter the no of elements")
for i in range(n):
    arr.append(int(input()))
arr = insertionsortinteger(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
