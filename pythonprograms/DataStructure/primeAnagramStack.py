from Bridgelabz.pythonprograms.DataStructure.prac import primeanagram2D
from Bridgelabz.pythonprograms.DataStructure.Stack import *
if __name__ == "__main__":
    # Object of class Stack
    stack = Stack()
    # returns the 2D Anagram Array in which prime number
    # which are Anagram or Non- Anagram are Store
    anagram = primeanagram2D()
    anagram1D = []
    # We want only those primeNumbers which are Anagram
    for i in range(500):
        if anagram[0][i] == 0:
            continue
        anagram1D.append(anagram[0][i])
    # Pushing Anagram Prime Numbers to Stack
    for i in anagram1D:
        stack.push(i)
    # Popping Anagram Prime Numbers From Stack
    for i in range(stack.size()):
        print(stack.pop(), end=" ")