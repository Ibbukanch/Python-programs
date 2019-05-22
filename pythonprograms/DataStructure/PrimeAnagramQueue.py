from Bridgelabz.pythonprograms.DataStructure.prac import primeanagram2D
from Bridgelabz.pythonprograms.DataStructure.Queue import *
# Object of class Stack
queue = Queue()
# returns the 2D Anagram Array in which prime numbers
# which are Anagram or Non- Anagram are Stored
anagram = primeanagram2D()
anagram1D = []
# We want only those primeNumbers which are Anagram
for i in range(500):
    if anagram[0][i] == 0:
        continue
    anagram1D.append(anagram[0][i])
# Pushing Anagram Prime Numbers to Queue
for i in anagram1D:
    queue.enqueue(i)
# Popping Anagram Prime Numbers From Queue
for i in range(queue.size()):
    print(queue.dequeuefront(),end=" ")