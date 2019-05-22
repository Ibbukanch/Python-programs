from Bridgelabz.pythonprograms.DataStructure.linklist import LinkedList,Node


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, obj):
        self.stack.insert(Node(obj))

    def pop(self):
        return self.stack.deleteend()

    def stacktop(self):
        return self.stack.stacktos()

    def size(self):
        return self.stack.Size()

