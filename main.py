#System Modeling abd Simulation Assignment 1 Moez Souidi
# Date: 10/10/2019
import random
import time


#Nice Touch 619 
random.seed(619)
#ToDo add timeer to the simulation

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)
    
# ●	Define a Deck class that initializes a list of cards by iterating over ranks and suits and creating a Card object for each combination of rank and suit. The class also has shuffle and draw methods

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack","Queen","King"]:
                self.cards.append(Card(suit, rank))
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop(0)
    def __str__(self):
        return str([str(card) for card in self.cards])


class Game:
    def __init__(self,game_name):
        self.game_name = game_name
    def play(self,deck):
        pass
    def rank_to_value(self,rank):
        if rank == "Ace":
            return 1
        elif rank == "Jack":
            return 11
        elif rank == "Queen":
            return 12
        elif rank == "King":
            return 13
        else:
            return int(rank)
        
class SaharaAce(Game):
    def __init__(self):
        Game.__init__(self,"Sahara Ace")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card = deck.draw()
        if card.rank == "Ace":
            return [True,10]
        else:
            return [False,0]

class TunisianTwins(Game):
    def __init__(self):
        Game.__init__(self,"Tunisian Twins")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        if card1.rank == card2.rank and card1.suit == card2.suit:
            return [True,50]
        else:
            return [False,0]
        
class MedinaBiggie(Game):
    def __init__(self):
        Game.__init__(self,"Medina Biggie")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        if self.rank_to_value(card2.rank) > self.rank_to_value(card1.rank):
            return [True,2]
        else:
            return [False,0]
        
class DesertHearts(Game):
    def __init__(self):
        Game.__init__(self,"Desert Hearts")
    def play(self):
        nb = 0
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        card3 = deck.draw()
        for card in [card1,card2,card3]:
            if card.suit == "Hearts":
                nb = nb + 1
        if nb>0:
            return [True,nb]
        else:
            return [False,0]

class OasisRunny(Game):
    def __init__(self):
        Game.__init__(self,"Oasis Runny")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        card3 = deck.draw()
        card4 = deck.draw()
        card5 = deck.draw()
        list = [card1,card2,card3,card4,card5]
        list.sort(key=lambda x: self.rank_to_value(x.rank))
        #Check for subset of 3 or more cards with consecutive ranks
        for i in range(0,len(list)-2):
            if self.rank_to_value(list[i+2].rank) - self.rank_to_value(list[i].rank) == 2:
                return [True,5]
        return [False,0]
    
class StudentGame(Game):
    def __init__(self):
        Game.__init__(self,"Student Game")
    def play(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.draw()
        card2 = deck.draw()
        #My game is to draw two cards and check if they have the same suit
        if card1.suit == card2.suit:
            return [True,10]
        else:
            return [False,0]
        

class MonteCarlo:
    def __init__(self,game,iterations):
        self.game = game
        self.iterations = iterations
    def run(self):
        start = time.time()
        excepected_winings_per_play = 0
        wins = 0
        for i in range(0,self.iterations):
            result = self.game.play()
            excepected_winings_per_play = excepected_winings_per_play + result[1]
            if result[0] == True:
                wins = wins + 1
        end = time.time()
        print("Simulation took " + str(end - start) + " seconds")
        return [round(wins/self.iterations*100,2),round(excepected_winings_per_play/self.iterations,2)]
    
if __name__ == "__main__":
    #Run the simulation for each game
    num_iterations = 0
    while num_iterations <= 0:
        num_iterations = int(input("Please enter the number of iterations: "))

    print("")

    print("Running simulation for Sahara Ace")
    winProb , winings = MonteCarlo(SaharaAce(),num_iterations).run()
    print("Win probability: " + str(winProb) + "%")
    print("Expected winings per play: " + str(winings) + " Dinars per play")
    print("")
    print("Running simulation for Tunisian Twins")
    winProb , winings = MonteCarlo(TunisianTwins(),num_iterations).run()
    print("Win probability: " + str(winProb) + "%")
    print("Expected winings per play: " + str(winings) + " Dinars per play")
    print("")
    print("Running simulation for Medina Biggie")
    winProb , winings = MonteCarlo(MedinaBiggie(),num_iterations).run()
    print("Win probability: " + str(winProb) + "%")
    print("Expected winings per play: " + str(winings) + " Dinars per play")
    print("")
    print("Running simulation for Desert Hearts")
    winProb , winings = MonteCarlo(DesertHearts(),num_iterations).run()
    print("Win probability: " + str(winProb) + "%")
    print("Expected winings per play: " + str(winings) + " Dinars per play")
    print("")
    print("Running simulation for Oasis Runny")
    winProb , winings = MonteCarlo(OasisRunny(),num_iterations).run()
    print("Win probability: " + str(winProb) + "%")
    print("Expected winings per play: " + str(winings) + " Dinars per play")
    print("")
    print("Running simulation for Student Game")
    winProb , winings = MonteCarlo(StudentGame(),num_iterations).run()
    print("Win probability: " + str(winProb) + "%")
    print("Expected winings per play: " + str(winings) + " Dinars per play")
