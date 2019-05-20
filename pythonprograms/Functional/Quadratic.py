# Program to calculate the root of Quadratic Equation
from math import *
print("Enter a,b & c value of quadratic equation")
a=float(input())
b=float(input())
c=float(input())
delta=(b*b)-(4*a*c)
# Calculating the Root
x1=(-b+sqrt(delta))/(2*a)
x2=(-b-sqrt(delta))/(2*a)
print("Root 1="+str(x1))
print("Root 2="+str(x2))
