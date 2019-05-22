# Function to print day
def dayofweek(date,month,year):
    y=year - (14 - month) // 12
    x=y + y//4 - y//100 + y//400
    m=month + 12 * ((14 - month)//12)-2
    d=(date + x + (31 * m)//12) % 7
    print(d)
# x-----------------------------------x---------------------------------------------------------------x

# This Function will convert celsius to Fahrenheit or Fahrenheit to Celsius

def tempconversion(temp,n):
    if n == 1:
        F = (temp * 9/5) + 32
        print("Temp in Fahrenheit ="+str(F))
    else:
        C = (temp - 32) * (5/9)
        print("Temp in Celsius="+str(C))
# x---------------------------x------------------------------------------------------------------------x
# Function to calculate the Monthly Payment

def monthlyPayment(Principal,Year,Rate):
    n = 12 * Year
    r = Rate/(12 * 100)
    a = pow((1+r),-n)
    pay = (Principal * r)/(1-a)
    print("Payment="+str(pay))
# x-------------------------------------x---------------------------------------------------------------x
def insertionsortinteger(arr):
# Traverse through 1 to len(arr)
    for i in range(0, len(arr) - 1):
        key = arr[i + 1]
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
        j = i
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return  arr
# x--------------------------------------x---------------------------------------------------------------x

def Anagram(str1,str2):
    # Convert both the strings to Uppercase
    str1 = str1.upper()
    str2 = str2.upper()
    # Sort both the strings
    str1 = sorted(str1)
    str2 = sorted(str2)
    # Check if strings are equal or not
    if str1 == str2:
        return True
    else:
        return False

#----------------------------------------------------x--------------------------------------------x

def primenumber():
    primearr = []
    for num in range(1, 1001):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primearr.append(num)
    return primearr
#---------------------x------------------------------------------------------------------#

#Function to check whether a year is a leap year or not

def leapyear(year):
    # The if statement checks if the year is a multiple of 4 but isn’t a multiple of 100
    # or if it is a multiple of 400 (not every year that is a multiple of 4 is a leap year)
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
#----------------------x-----------------------------------------------#

#Function to find factorial of a number

def factorial(n):
    fact = 1
    for c in range(1,n+1):
        fact = fact * c
    return fact


