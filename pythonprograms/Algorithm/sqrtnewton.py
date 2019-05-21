# program to find the sqrt of number using newton method
# Take input from user
n=float(input("Enter the Number"))
t = n
# calculates the sqrt of a Number
while abs(t- n/t) > 1e-15 * t:
    t = (n/t + t) / 2
# Print the sqrt of a number
print(round(t,2))
