from Bridgelabz.pythonprograms.Algorithm.util import factorial
class Binarysearchtree:
    def No_of_bst(self,nodes):

        # Calculating how much no.of BST can be constructed using formula

        catalan = factorial(2 * nodes) // (factorial(nodes + 1) * factorial(nodes))
        # Display the number of distinct BST
        print("Number of Distinct Binary search tree= "+str(catalan))

if __name__ == "__main__":
    # Taking input from user
    nodes=int(input("Enter the Number of Nodes:"))
    # Creating the object of Binarysearchtree
    bst = Binarysearchtree()
    # Calling the method of class BST
    bst.No_of_bst(nodes)
