# Program to find prime numbers which are Palindrome and Anagram
from array import *
import numpy
# Function which will reverse the number and return
def palindrome(palin):
    Reverse=0
    while (palin > 0):
        Reminder = palin % 10
        Reverse = (Reverse * 10) + Reminder
        palin = palin // 10
    return Reverse
arr = array('i',[])
# Displaying Prime Numbers
print("Prime numbers between 1 to 1000 are:")
for num in range(1, 1001):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           arr.append(num)      # Adding Prime Numbers to an Array
for i in range(len(arr)):
    print(arr[i],end=" ")
print("\nPalindrome Prime Numbers are:")
for i in range(len(arr)):
    result=palindrome(arr[i])

    #Checking if the number is palindrome or not
    if result==arr[i]:
        print(result,end=" ")

# Displaying Prime numbers which are Anagram
print("\nPrime Number which are Anagrams are:")
for i in range(len(arr)-1):
    str1=str(arr[i])
    string1=sorted(str1)
    for j in range(i+1,len(arr)):
        str2=str(arr[j])
        string2=sorted(str2)
        if string1 == string2:
            print(str1,str2)