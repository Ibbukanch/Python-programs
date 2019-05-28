import json
from re import search


class Service:
    def __init__(self):
        # Creating empty list
        
        self.person_data = []
        self.file_name = None

    def create(self):

        # Creating new json file

        try:
            file_name = input("Enter file name for creating new json file : ").strip()
            if search("[a-zA-Z]", file_name) is not None:
                f = open(file_name + ".json", 'w+')
                f.close()
            else:
                raise ValueError
        except ValueError:
            print("File name should be alphabet only")

    def open(self):

        # Open json file and read json data from json file

        file_name = input("Enter file name :  ").strip()
        try:
            with open(file_name + ".json") as data:
                self.person_data = json.load(data)
                self.file_name = file_name
        except Exception:
            print("File not found.")

    def save(self):

        # Save json data into json file


        try:

            with open(self.file_name + ".json", 'w') as data:
                json.dump(self.person_data, data,indent=2)
                data.close()
        except Exception:
            print("You have not yet open any file. ")

    def save_as(self):

        # save as the json data into json file or text file

        file_name = input("Enter file name with extension json or txt : ").strip()
        json_patt = search("\.json", file_name)
        txt_patt = search("\.txt", file_name)
        if json_patt is not None and json_patt.group() == ".json":
            select = 1
        elif txt_patt is not None and txt_patt.group() == ".txt":
            select = 2
        else:
            print("You enter wrong file extension.")
            return

        with open(file_name, 'w+') as data:
            if select == 1:
                json.dump(self.person_data, data)
            elif select == 2:
                data.write(str(self.person_data))

    def add_person(self):

        # Creating new person data and then add person list

        try:
            first_name = input("Enter first name : ").strip().upper()
            last_name = input("Enter last name : ").strip().upper()
            address = input("Enter address : ").strip().upper()
            city = input("Enter city : ").strip().upper()
            state = input("Enter state : ").strip().upper()
            zip_code = input("Enter zip code : ").strip()
            phone_number = input("Enter phone number : ").strip()
            if not first_name.isalpha() and not last_name.isalpha() and not city.isalpha() and not state.isalpha() and not phone_number.isalpha() \
                    and not zip_code.isalpha() and not phone_number.isnumeric():
                raise ValueError
        except ValueError:
            print("You have to entered your data correctly.")
        else:

            new_person = {"data": {}}

            new_person["data"]["address"] = address
            new_person["data"]["city"] = city
            new_person["data"]["state"] = state
            new_person["data"]["zip_code"] = zip_code
            new_person["data"]["phone_number"] = phone_number
            new_person["first_name"] = first_name
            new_person["last_name"] = last_name
            flag = True
            for i in self.person_data:
                if i["first_name"] == first_name and i["last_name"] == last_name:
                    print("Duplicate data.")
                    flag = False
                    break
            if flag:
                self.person_data.append(new_person)
        print(self.person_data)

    def delete_person(self):

        #Deletes the Peron from the List
        try:
            first_name = input("Enter the First Name you want to delete:").strip().upper()
            last_name = input("Enter the Last Name you want to delete:").strip().upper()
            if not first_name.isalpha() or not last_name.isalpha():
                raise ValueError
        except ValueError:
            print("Name should contain only alphabets")
            self.delete_person()

        for i in range(len(self.person_data)):
            if self.person_data[i]["first_name"] == first_name and self.person_data[i]["last_name"] == last_name:
                self.person_data.remove(self.person_data[i])
                print("Data Deleted Successfully")
                return True
                break



if __name__ == "__main__":
    s= Service()