#Program of Leap year
from Bridgelabz.pythonprograms.Algorithm.util import leapyear

if __name__ == "__main__":
    # User must first enter the year to be checked
    year = int(input("Enter year to be checked:"))
    if leapyear(year):
        print(str(year) + " is a Leap Year")
    else:
        print(str(year) + " is not a Leap Year")