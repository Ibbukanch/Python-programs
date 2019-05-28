# Coupon Number Program
import random
from array import *
arr=array('i',[])
def getcoupon(n):                     # Function to calculate Random Number
    return int(random.random() * n)

def collect(n):                       # Function to Collect the distinct Coupons
    count=0
    for i in range(n):
        arr.append(0)

    distinct=0
    while(distinct<n):
        value=getcoupon(n)
        print(value,end=" ")    # Printing the value of random number
        count=count+1
        if arr[value]==0:
            distinct=distinct+1
            arr[value]=1         # Adding the value in Array if random number is distinct
    return count

if __name__ == "__main__":
    x = int(input("Enter distinct coupon Number\n"))
    count = collect(x)
    # printing the count of random numbers generated
    print("\nRandom coupons generated="+str(count))
