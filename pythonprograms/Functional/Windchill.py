# Program to calculate Wind Chill
t=float(input("Enter Temperature in Fahrenheit\n"))
# Temperature Should less then 50
while t>50:
    print("Temperature value should be less then or equal to 50\nRe-enter the value")
    t=float(input())
v=float(input("Enter Value of Wind Speed\n"))
# Wind speed Should greater then 3 and less then 120
while v<3 or v>120:
    print("Value should not be less then 3 or Greater then 120\nRe-enter the value")
    v=float(input())
# Formula For Calculating Wind Chill
w=35.74+0.6215*t+(0.4275*t-35.75)*pow(v,0.16)
print("Wind Chill="+str(w))