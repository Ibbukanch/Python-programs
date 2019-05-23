"""
Overview : JSON Inventory Data Management of Rice, Pulses and Wheats.
purpose: Json Concept,reading json data and print
class name : Inventory
date : 22/05/2019
"""
import json
with open("Jsonfiles/Inventory.json") as json_file:
    data = json.load(json_file)   # Reading the json File
for i in data:
    price1 = weight1 = 0
    print("***********", i, "*************")
    for j in data[i]:
        price1 += int(j["price"])
        weight1 += int(j["weight"])  # Adding up the price and Weight of Particular data
    print("Price : ", price1)
    print("Weight : ", weight1)