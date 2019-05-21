# Program to convert a decimal number to binary number

# function to convert decimal to binary
def decToBinary(n):
    # array to store a binary number
    binaryNum = [0] * n

    # counter for binary array
    i = 0;
    while (n > 0):
        # storing remainder in binary array
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1

    # printing binary array in reverse order
    for j in range(i - 1, -1, -1):
        print(binaryNum[j], end="")

n = int(input("Enter the Number\n"))

decToBinary(n)


