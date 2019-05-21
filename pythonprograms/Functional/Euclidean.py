# Program to calculate Euclidean Distance
# importing package sys for Command line arguments
import sys
from math import  *
x=float(sys.argv[1])
y=float(sys.argv[2])
# Calculating Distance
z=(x*x) + (y*y)
distance=sqrt(z)
print("Euclidean Distance="+str(distance))
