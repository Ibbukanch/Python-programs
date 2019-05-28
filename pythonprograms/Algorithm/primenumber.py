# Program to print Prime Numbers From 1 to 1000
from Bridgelabz.pythonprograms.Algorithm.util import primenumber
if __name__ == "__main__":
    print("Prime Numbers from 1 to 1000 are:")
    # Calling the function prime Number which will return the prime Number Array

    primearr = primenumber()
    # Display the Array
    for i in range(len(primearr)):
        print(primearr[i],end=" ")

