# Program to calculate Harmonic Number
# Import sys package for command line argument
import sys
n=int(input("Enter the number\n"))
sum=1
# While loop will run if number is negative
while n<=0:
    print("Enter positive value,Re-enter the value\n")
    n=int(input())
# Calculating Series
for i in range(1,n):
    sum=sum+(1/i)
print(sum)
