# Program to Convert temperature to Celsius or Fahrenheit
from Bridgelabz.pythonprograms.Algorithm.util import tempconversion
# take temperature value from user
print("Press 1 to Enter Temperature in Celsius:")
print("Press 2 to Enter Temperature in Fahrenheit:")
n=int(input())
while n!=1 and n!=2:
    print("Invalid Input\nPress 1 to Enter Temperature in Celsius:\nPress 2 to Enter Temperature in Fahrenheit:")
    n=int(input())
if n == 1:
    C=float(input("Enter Temperature in Celsius\n"))
    tempconversion(C,n)
else:
    F=float(input("Enter Temperature in Fahrenheit\n"))
    tempconversion(F,n)
