from Bridgelabz.pythonprograms.DataStructure.linklist import LinkedList,Node
class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, obj):
        self.queue.insert(Node(obj))

    def dequeuefront(self):
        return self.queue.deletebeg()

    def dequeuerear(self):
        return self.queue.deleteend()

    def size(self):
        return self.queue.Size()