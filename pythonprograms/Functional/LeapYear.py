#Program of Leap year
from Bridgelabz.pythonprograms.Algorithm.util import leapyear


# User must first enter the year to be checked
year=int(input("Enter year to be checked:"))
if leapyear(year):
    print(str(year)+" is a Leap Year")