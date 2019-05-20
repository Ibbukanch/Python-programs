# Program Of Power of 2
# importing sys package for Command line argument
import sys
n=int(sys.argv[1])
# Printing power of 2 value till n
for i in range(n+1):
    a=pow(2,i)
    print(a)