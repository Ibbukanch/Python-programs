# Program for Printing username with string
username=input("Enter the Username\n")
# If length is less then 2
while len(username)<=2:
    print("Username should contain minimum 3 characters")
    username=input("Enter the Username\n")
# Printing the username
print("Hello "+username+",How are you?")



