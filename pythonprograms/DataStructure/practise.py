"""
Program to Read the Paragraph and if Vowels Encounter then push it into the stack
and in stack2 update the counter of each vowels encounters
"""

class Stacks:
    def __init__(self):
        self.list = []

    def push(self,ele):
        self.list.append(ele)

    def pop(self):
        return self.list.pop()

    def display(self):
        for i in self.list:
            print(i,end=" ")


def update(x):
    list1 = []
    list2 = []
    for i in range(5):
        n1 = stack1.pop()
        list1.append(n1)
        n2 = stack2.pop()
        list2.append(n2)
    n = list1.index(x)
    list2[n] += 1

    for i in range(5):
        stack1.push(list1[i])
        stack2.push(list2[i])

if __name__ == "__main__":

    # This is the Main method
    #Creating objects of Class Stack

    stack1 = Stacks()
    stack2 = Stacks()

    # Reading the paragraph

    paragraph = 'My name is Ibrahim'


    vowels = 'aeiou'  # Reading Vowels
    # Pushing vowels into stack1
    for i in vowels:
        stack1.push(i)
    #  Initially Pushing 0 to stack2
    for i in range(5):
        stack2.push(0)

    for i in paragraph.lower():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            update(i)    # If vowel encounter then update the counter into stack2
            print()
            stack1.display()
            print()
            stack2.display()

        else:
            continue

# Display both Stacks

    print()
    stack1.display()
    print()
    stack2.display()


