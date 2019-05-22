# Program to print Prime Numbers From 1 to 1000
from Bridgelabz.pythonprograms.Algorithm.util import primenumber
print("Prime Numbers from 1 to 1000 are:")
primearr = primenumber()
for i in range(len(primearr)):
    print(primearr[i],end=" ")

