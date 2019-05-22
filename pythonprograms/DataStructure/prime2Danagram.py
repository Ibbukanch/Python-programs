from Bridgelabz.pythonprograms.DataStructure.prac import primeanagram2D
anagramarr = primeanagram2D()  # returns the 2D Anagram Array in which prime number
for x in range(2):             # which are Anagram or Non- Anagram are Store
    if x == 0:
        print("Prime Numbers which are Anagram:")
    else:
        print("Prime Numbers which are not Anagram:")
    for y in range(500):
        if anagramarr[x][y] == 0:
            continue
        print(int(anagramarr[x][y]), end=" ")
    print()