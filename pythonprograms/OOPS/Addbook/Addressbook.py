from Bridgelabz.pythonprograms.OOPS.Addbook.Service import Service

"""
Overview : To maintain an address book.
purpose : Show the menu list to user
class name : AddressBook
date : 24/05/2019
"""
class AddressBook:
    def __init__(self):

        # Creating object of Class Service

        self.addbook = Service()

    def addressbook(self):
        # Try block for handling Exceptions
        try:
            while True:
                print()
                # Enter the choice what Function you want to perform
                print("1.Create\n2.Open\n3.Save\n4.Save As\n5.Add Person\n6.Delete Person\n7:Exit")
                entered = int(input("Enter choice : "))
                if entered == 7:
                    self.addbook.save()
                    print("Exited")
                    return
                elif entered > 7:
                    print("You have selected wrong choice.")
                    continue
                choice = {1: "create", 2: "open", 3: "save", 4: "save_as",
                          5: "add_person", 6:"delete_person"}
                fun = getattr(self.addbook, choice[entered])
                fun()
        except Exception as e:
            print("You have enter wrong input.")
            self.addressbook()




# Main method

if __name__ == "__main__":

    # Creating object of class AddressBook
    obj = AddressBook()
    # Calling class Methods
    obj.addressbook()