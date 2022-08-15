import random
from graphics import *

class playCard():

    def __init__(self, rank, suit):
        # rank: int from 1 to 13 (ranks ace-king)
        # suit: 'd', 'c', 'h', 's' (diamonds, clubs, hearts, spades)
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        # returns the Blackjack value of a card
        # ace counts as 1, face cards count as 10
        if self.rank >= 10:
            return 10
        return self.rank

    def draw(self, win, center):
        # https://code.google.com/archive/p/vector-playing-cards/downloads
        imgDir = "cardsImg/" + "_".join(self.__str__().lower().split(" ")) + '.png'
        numtoletter = {
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'ten': '10'
        }
        for k in numtoletter.keys():
            imgDir = imgDir.replace(k, numtoletter[k])

        myImg = Image(center, imgDir)
        myImg.draw(win)

    def __str__(self):
        rankNames = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        rankName = rankNames[self.rank-1]

        names = {
            'd': 'Diamonds',
            'c': 'Clubs',
            'h': 'Hearts',
            's': 'Spades'
            }

        suitName = names[self.suit]

        return '{} of {}'.format(rankName, suitName)

def main():
    print("Let's play Blackjack !")
    n = int(input('How many cards do you want to draw? (int): '))
    win = GraphWin("BlackJack", 800, 600)

    for i in range(n):
        card = playCard(random.randint(1,13), random.choice(['d','c','h','s']))
        center = Point((2*i+1)*800/(2*n), 300)
        card.draw(win, center)
        print('Card: {}; value = {}'.format(card, card.value()))

    win.getMouse()

if __name__ == '__main__':
    main()
        