import numpy
from Bridgelabz.pythonprograms.Algorithm.util import primenumber

class TwoDPrimeArray:
    def __init__(self):

        # Creating array for maintain and store data in array

        self.arr = numpy.zeros((10, 168))

    def prime2D(self,primearr):

        #print array of prime number
        k = j = 0
        block = 100
        for i in primearr:
            if i > block:
                k += 1
                j = 0
                block += 100
            self.arr[k][j] = i
            j += 1
        l = 0
        for x in range(10):
            print(str(l)+"-"+str(l+100)+":",end=" ")
            for y in range(30):
                if self.arr[x][y]==0:
                    continue
                print(int(self.arr[x][y]), end=" ")
            print()
            l = l+100



ll = TwoDPrimeArray()
primearr = primenumber()
ll.prime2D(primearr)