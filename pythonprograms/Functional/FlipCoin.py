# Program of Flip Coin
import random
def flipcoin(a):
    i = 0
    head = 0
    tails = 0
    # If random Generated is greater then 0.5 then increment head otherwise tails
    for i in range(a):
        if random.random() > 0.5:
            head = head + 1
        else:
            tails = tails + 1
    n = (float(head) / float(tails)) * 100
    # Printing the Percentage of Heads vs Tails
    print("Percentage of Heads vs Tails= " + str(n))

if __name__ == "__main__":
    a = int(input("The number of times to Flip Coin\n"))
    # If User enters the negative number
    while a < 0:
        print("It should be a positive number")
        a = int(input("Re-enter the number\n"))
    flipcoin(a)


