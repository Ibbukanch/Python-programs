# OOPS Program to Replace the Paragraph Content with Proper Name,Fullname and Mobile No.

import re
import datetime

# Assigning a Paragraph to the String

string = "Hello <<name>>, We have your full name as <<full name>> in our system. " \
         "your contact number is 91-xxxxxxxxxx. " \
         "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016"

# Accept Name,Fullname and Mobile no from user
count = 1
while count > 0:
    try:
        Name = input("Enter the Name:")
        FullName = input("Enter the FullName:")
        MobileNo = input("Enter the Mobile Number:")
        if not Name.isalpha() or not FullName.isalpha() or not MobileNo.isnumeric():
            raise ValueError
    except:
        print("You have entered wrong data.")
    else:
        break
 # Accepting date using inbuild Function

date = datetime.datetime.now()
dateformat = date.strftime("%d/%m/%y")
string = re.sub("<<name>>", Name, string)  # Replacing the string <<name>> with proper Name
string = re.sub("<<full name>>", FullName, string)  # Replacing the string <<full name>> with FullName
string = re.sub("xxxxxxxxxx", MobileNo, string)  # Replacing the string <<xxxxx>> with Mobile No
string = re.sub("01/01/2016", dateformat, string)  # Replacing the string 01/01/2016 with Today's Date
# Display the Replace String

print(string)



