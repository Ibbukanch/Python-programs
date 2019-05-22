from Bridgelabz.pythonprograms.DataStructure.Stack import Stack
class BalancedParentheses:
    def __init__(self):
    # Creating object of class stack
        self.stack = Stack()

    def balancedParentheses(self, string):
        for i in string:
            if i is '(':
                self.stack.push(i)
            elif i is ')' and self.stack.stacktop() is '(':
                self.stack.pop()

        if self.stack.size() is 0:
            return True
        else:
            return False


if __name__ == "__main__":

    obj = BalancedParentheses()
    string = input("Enter expression : ")

    result = obj.balancedParentheses(string)
    print(result)
    if result:
        print("Arithmetic Expression is Balanced")
    else:
        print("Arithmetic Expression is Not Balanced")