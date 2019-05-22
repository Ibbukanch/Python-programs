from Bridgelabz.pythonprograms.DataStructure.Queue import *
class PalindromeChecker:
    def __init__(self):
        self.queue = Queue()

    def palindromeChecker(self, string):
        for i in range(len(string)):
            self.queue.enqueue(string[i])
        while self.queue.size() > 1:
            if self.queue.dequeuefront() != self.queue.dequeuerear():
                return False
        return True

if __name__ == '__main__':
    pal = PalindromeChecker()
    String=input("Enter the String\n")
    x = pal.palindromeChecker(String.upper())
    if x:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

