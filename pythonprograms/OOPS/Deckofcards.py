# Program Of Deck Of Cards
import random
class Deckofcards:
    def __init__(self):
        # Creating Dictionaries and Tuples

        self.card = {"Clubs":[],"Diamonds":[],"Hearts":[],"Spades":[]}
        self.suit = ("Clubs","Diamonds","Hearts","Spades")
        self.rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        self.player1 = {"Clubs":[],"Diamonds":[],"Hearts":[],"Spades":[]}
        self.player2 = {"Clubs":[],"Diamonds":[],"Hearts":[],"Spades":[]}
        self.player3 = {"Clubs":[],"Diamonds":[],"Hearts":[],"Spades":[]}
        self.player4 = {"Clubs":[],"Diamonds":[],"Hearts":[],"Spades":[]}
        self.player = (self.player1,self.player2,self.player3,self.player4)

    def randoms(self):

        # This method will generate the random rank and will append it into the particular card List

        counter = 36
        while counter > 0:
            suit = self.suit[random.randrange(0,4,1)]
            rank = self.rank[random.randrange(0,13,1)]
            temp = self.card[suit]
            flag = True
            for i in range(len(temp)):
                if temp[i] == rank: # checking if already Present or not
                    flag = False    # If present then dont append
                    break
            if flag:                # If not present then append
                self.card[suit].append(rank)
                counter = counter - 1

    def assign(self):

        # Assining Deck cards to each player

        count = 0
        for i in self.suit:
            temp = self.card[i]
            for j in range(len(temp)):
                if count >= 4:
                    count = 0
                self.player[count][i].append(temp[j])
                count = count + 1

    # Display Function, which will display all the cards of each player

    def display(self):
        for i in range(len(self.player)):
            print("\n----Player ", i + 1, "-----")
            print("Clubs : ", self.player[i]["Clubs"])
            print("Diamonds : ", self.player[i]["Diamonds"])
            print("Hearts : ", self.player[i]["Hearts"])
            print("Spades : ", self.player[i]["Spades"])

# MAIN METHOD
if __name__ == "__main__":
    deck = Deckofcards()  # Creating object of class Deckofcards

    # Calling the class methods

    deck.randoms()
    deck.assign()
    deck.display()



