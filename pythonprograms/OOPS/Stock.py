"""
Overview : Stock Management of Companies
purpose: Json Concept,reading json data and print
class name : Stock
date : 23/05/2019
"""
import json
class Stock:
    def __init__(self):
        self.list = []


    def readingstocks(self):

        # This method will read the json file and will append data to list

        with open("Jsonfiles/stock.json") as my:
            data = json.load(my)

        for i in data:
            self.list.append(i)



    def newdata(self):

        #This method will take the New data from User
        new = {
            "name":"",
            "no.of share":"",
            "price":""
        }
        name = input("Enter Company Name:")
        noofshare = input("Enter no.of shares of Company:")
        price = input("Enter the price:")

        new["name"] = name
        new["no.of share"] = noofshare
        new["price"] = price
        return new

    def update(self):

        # This Method will update the json file
        new = self.newdata()
        self.list.append(new)
        with open("Jsonfiles/stock.json",'w') as my:
            json.dump(self.list,my)

    def display(self):

        #Display the file

        print("Company Name\t\tNo of shares\t\tPer Share Price")
        for i in self.list:
            print(i["name"],"\t\t\t\t",i["no.of share"],"\t\t\t\t",i["price"])

        totals = 0
        for i in self.list:
            total = 0
            totals += int(i["price"])
            total += int(i["price"])
            print(i["name"],":",total)
        print("Total Price Value of the Stocks:",totals)

# MAIN METHOD

if __name__ == "__main__":

    #  Creating the object of class stock

    stock = Stock()

    # Calling the class methods

    stock.readingstocks()
    stock.display()
    stock.update()
    stock.display()