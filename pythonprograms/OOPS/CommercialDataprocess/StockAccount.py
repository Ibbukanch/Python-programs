from Bridgelabz.pythonprograms.OOPS.CommercialDataprocess.Company import Comcus
class StockAccount:
    def __init__(self):

        # Creating object of class comcus

        self.operation = Comcus()
        self.filename = None

    def stockaccount(self):
        while True:

            # Enter the choice what Function you want to perform

            print("1:Add customer\n2:Add company\n3:Remove Customer\n4:Remove Company\n5:Buy\n6:Sell\n7:Save\n8:Exit")
            choice =int((input("Enter the choice:")))
            try:   # Handling Exceptions

                if 8 <= choice <= 0:
                    raise ValueError
            except Exception or ValueError:
                    print("Invalid input")
                    continue

            if choice ==5 or choice == 6:
                try:
                    customerid = input("Enter Customer ID:")
                    customername = input("Enter Customer Name")
                    if choice == 5:
                        for i in self.customer.companydata:
                            print("Company Name:",i["name"],"No.of Share:",i["data"]["no.of share"],"share price:",i["data"]
                                    ["price"])
                    else:
                        for i in self.customer.customerdata:
                            if i["id"] == str(customerid) and i["name"] == customername:
                                print(i["data"])

                    # Taking inputs from user

                    companyname = input("Enter Company Name:")
                    noofshare =   input("Enter No of Share:")

                    # Validating data

                    if not companyname.isalpha() or not noofshare.isnumeric():
                        raise  ValueError
                except ValueError:
                    print("Invalid Input")
                    continue

            choiceselected = {1:"addcustomer",2:"addcompany",3:"removecustomer",4:"removecompany",5:"buy",6:"sell",
                              7:"save"}
            if choice == 8:

                # If user exits then first save the files

                self.operation.save("companies")
                self.operation.save("customer")
                return
            if 1 <= choice <= 5 or choice == 8:
                check = getattr(self.operation,choiceselected[choice])
            else:
                check = getattr(self.operation,choiceselected[choice])

            if choice == 5 or choice == 6:
                check(customerid,companyname,customername,noofshare)

            else:
                check()

# Main Method

if __name__ == "__main__":

    # Create the object of class StockAccount

    stock = StockAccount()

    # call the class methods

    stock.stockaccount()



