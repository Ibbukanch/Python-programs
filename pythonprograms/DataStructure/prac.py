from Bridgelabz.pythonprograms.Algorithm.util import Anagram,primenumber
import numpy
# Function will return the 2D array of Prime Number which are anagram and prime number which are not anagram
def primeanagram2D():
    primearr = primenumber()
    anagramarr = numpy.full((2, 500), 0)
    b_value = True
    cnt = 0
    for i in range(len(primearr)):
        for j in range(len(primearr)):
            if i == j:
                continue
            b_value = True
            if Anagram(str(primearr[i]), str(primearr[j])):   #First row contains prime number which are anagram
                anagramarr[0][cnt] = primearr[i]              #Second row contains prime number which are not anagram
                cnt += 1
                b_value = False
                break
        if b_value:
            anagramarr[1][i] = primearr[i]
    return anagramarr




