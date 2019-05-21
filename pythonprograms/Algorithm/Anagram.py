#Program to find whether 2 strings are anagram or not
from com.Bridgelabz.Algorithm.util import Anagram

# take 2 strings from user
str1=input("Enter the First string\n")
str2=input("Enter the Second string\n")
if Anagram(str1,str2):
    print("Strings are Anagram")
else:
    print("Strings sre not Anagram")

