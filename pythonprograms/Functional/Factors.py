# Program to find the number of prime Factors
from math import *
def factors(n):
#While loop will run if the number is Even
    list =[]
    while n%2==0:
        list.append(2)
        print (2,end=" ")
        n=n/2
    x=int(sqrt(n))
#for loop will run if the Number is odd
    for i in range(3,x+1,2):
        while n%i==0:
            list.append(i)
            print (i,end=" ")
            n=n/i
#Here it will come if the number is prime number
    if  n>2:
        list.append(n)
        print(n)
    return list

n=int(input("Enter the Number"))
factors(n)