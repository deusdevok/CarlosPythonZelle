import random

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

    for _ in range(n):


        card = playCard(random.randint(1,13), random.choice(['d','c','h','s']))
        print('Card: {}; value = {}'.format(card, card.value()))

if __name__ == '__main__':
    main()
        