from math import trunc
from Bridgelabz.pythonprograms.Algorithm.util import leapyear
class Calendar:
    def __init__(self):

        self.arr = []
        self.week = ["S", "M", "T", "W", "Th", "F", "S"]
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def display(self, arr, month, year):

        print("------------", month, year, "---------------")
        for i in self.week:
            print(i, end="    ")
        for i in range(len(arr)):
            if i % 7 == 0:
                print()
            if arr[i] == 0:
                print(end="     ")
            elif arr[i] < 10:
                print(arr[i], end="    ")
            else:
                print(arr[i], end="   ")

    def initial(self, m, y):

        day_of_year = (y * 365 + trunc((y - 1) / 4) - trunc((y - 1) / 100) +
                       trunc((y - 1) / 400)) % 7
        month = self.month_days[m - 1]
        for i in range(m - 1):
            day_of_year += self.month_days[i]
        if leapyear(y):
            if m == 2:
                month += 1
            day_of_year += 1
        day_of_year = (day_of_year % 7)
        temp = 1
        for i in range(42):
            if day_of_year > 0:
                self.arr.append(0)
                day_of_year -= 1
                continue
            if temp <= month:
                self.arr.append(temp)
                temp += 1
                continue
            self.arr.append(0)
        return self.arr


if __name__ == "__main__":

#Creating object of Calender class

    c = Calendar()

    month = int(input("Enter a month : "))
    year = int(input("Enter a year : "))
    arr = c.initial(month, year)
    c.display(arr, month, year)