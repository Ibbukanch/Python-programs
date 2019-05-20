#Program of Leap year
# User must first enter the year to be checked
year=int(input("Enter year to be checked:"))
# The if statement checks if the year is a multiple of 4 but isn’t a multiple of 100
# or if it is a multiple of 400 (not every year that is a multiple of 4 is a leap year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")