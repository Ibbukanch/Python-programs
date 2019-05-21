# Program for three integers adds to zero


from array import *
arr=array('i',[])
n=int(input("Enter the length of array\n"))
print("Enter the elements\n")
for i in range(n):    #Taking the array input from user
    x=int(input())
    arr.append(x)
sum=0
for i in range(len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for f in range(j + 1, len(arr)):
            if(arr[i]+arr[j]+arr[f]==0):
                print(arr[i], arr[j], arr[f])  #Printing the triplets
                sum = sum + 1                  # Counting the no of triplets

print("Number of Triplets=" + str(sum))

