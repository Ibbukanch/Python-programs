# Program to calculate Euclidean Distance
# importing package sys for Command line arguments
import sys
from math import  *

# Calculating Distance
def euclidean(x,y):
    z=(x*x) + (y*y)
    distance=sqrt(z)

if __name__ == "__main__":
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    distance = euclidean(x,y)
    print("Euclidean Distance=" + str(distance))
