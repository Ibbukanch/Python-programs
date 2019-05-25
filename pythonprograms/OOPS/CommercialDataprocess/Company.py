import json
class Comcus:
    def __init__(self):
        # Creating empty list of customer and company
        self.customer_data = []
        self.company_data = []


        # Open json file and read json data from json file

        try:
            with open("companies.json") as data:
                self.company_data = json.load(data)
            with open("customer.json") as data:
                self.customer_data = json.load(data)
        except Exception:
            print("File not found.")

    def save(self,filename):

        # Save json data into particular json file

        try:
            with open(filename + ".json", 'w') as data:
                if filename == "companies": # checking in which json file we want to Dump data
                    json.dump(self.company_data, data, indent=2)
                else:
                    json.dump(self.customer_data, data, indent=2)
                    data.close()
        except Exception:
            print("You have not yet open any file. ")

    def addcompany(self):


            # Creating new company data and then add it into company list

            try:
                # Taking inputs from user

                companyname = input("Enter Company name : ").strip().upper()
                noofshare = input("Enter Number of share : ").strip()
                price = input("Enter Price : ").strip()
                balance = input("Enter Balance : ").strip()

                # Validating data

                if not companyname.isalpha() and not noofshare.isnumeric() and not price.isnumeric() and not balance.isnumeric():
                    raise ValueError
            except ValueError:
                print("You have to entered your data correctly.")
            else:
                # creating json file

                newcompany = {"data": {}}
                newcompany["Company Name"] = companyname
                newcompany["data"]["no.of share"] = noofshare
                newcompany["data"]["price"] = price
                newcompany["data"]["balance"] = balance

                flag = True
                for i in self.company_data:
                    if i["Company Name"] == companyname:
                        print("Duplicate data.")
                        flag = False
                        break
                if flag:
                    self.company_data.append(newcompany)
            print(self.company_data)
            self.save("companies")

    def addcustomer(self):
        # Creating new customer data and then add it into customer list
        try:

            # Taking inputs from user

            customername = input("Enter Customer name : ").strip().upper()
            noofshare = input("Enter Number of share : ").strip()
            price = input("Enter Price : ").strip()
            balance = input("Enter Balance : ").strip()

            # Validating data

            if not customername.isalpha() and not noofshare.isnumeric() and not price.isnumeric() and not balance.isnumeric():
                raise ValueError
        except ValueError:
            print("You have to entered your data correctly.")
        else:

            # creating customer json file

            newcustomer = {"data": {}}
            newcustomer["Customer Name"] = customername
            newcustomer["data"]["no.of share"] = noofshare
            newcustomer["data"]["price"] = price
            newcustomer["data"]["balance"] = balance

            flag = True
            for i in self.customer_data:
                if i["Customer Name"] == customername:
                    print("Duplicate data.")
                    flag = False
                    break
            if flag:
                self.customer_data.append(newcustomer)
        print(self.customer_data)
        self.save("customer")

    def removecompany(self):   # Will remove the company data from list and json file
        try:
            # Enter the company name which you want to remove

            companyname = input("Enter Company Name to remove:").strip().upper()

            if not companyname.isalpha():
                raise ValueError
        except ValueError:
            print("Invalid input")
            self.removecompany()
        else:
            for i in range(len(self.company_data)):
                if self.company_data[i]["Company Name"] == companyname:
                    self.company_data.remove(self.company_data[i])
                    print("Deleted..")
                    break
            self.save("companies")

    def removecustomer(self):   # Will remove the company data from list and json file
        try:

            # Enter the customer name which you want to remove

            customername = input("Enter Customer Name to remove:").strip().upper()
            if not customername.isalpha():
                raise ValueError
        except ValueError:
            print("Invalid input")
            self.removecompany()
        else:
            for i in range(len(self.customer_data)):
                if self.customer_data[i]["Customer Name"] == customername:
                    self.customer_data.remove(self.customer_data[i])
                    print("Deleted..")
                    break
            self.save("customer")



