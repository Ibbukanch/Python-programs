#Program to find whether 2 strings are anagram or not
from Bridgelabz.pythonprograms.Algorithm.util import Anagram

if __name__ == "__main__":
    # take 2 strings from user

    str1=input("Enter the First string\n")
    str2=input("Enter the Second string\n")
    if Anagram(str1,str2):
        print("Strings are Anagram")
    else:
        print("Strings sre not Anagram")

