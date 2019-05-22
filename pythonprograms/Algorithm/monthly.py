from Bridgelabz.pythonprograms.Algorithm.util import monthlyPayment
# Takes input from user
Principal=float(input("Enter Principal loan Amount\n"))
Years=float(input("For How Many years\n"))
Rate=float(input("At what Rate of Interest\n"))
# Calculates the monthly Payment
monthlyPayment(Principal,Years,Rate)
