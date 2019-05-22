from Bridgelabz.pythonprograms.Algorithm.util import factorial
class Binarysearchtree:
    def No_of_bst(self,nodes):
        catalan = factorial(2 * nodes) // (factorial(nodes + 1) * factorial(nodes))
        print("Number of Distinct Binary search tree= "+str(catalan))

nodes=int(input("Enter the Number of Nodes:"))
bst = Binarysearchtree()
bst.No_of_bst(nodes)
