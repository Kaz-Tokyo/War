class Card:
    values = [None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suits = ["spades", "hearts", "diamonds", "clubs"]
    def __init__(self, v, s):
        self.value = v
        self.suit = s
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False

def __gt__(self, c2):
    if self.value > c2.value:
        return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
    else:
        return False

def __repr__(self):
    v = "{} of {}".format(self.values[self.value], self.suits[self.suit])
    return v

import random
class Deck:
    def __init__(self):
        self.deck_cards = []
        for i in range(2, 15):
            for j in range(4):
                self.deck_cards.append(Card(i, j))
        random.shuffle(self.deck_cards)
    def draw_card(self):
        if len(self.deck_cards) >= 1:
            return self.deck_cards.pop()
        else:
            return
deck = Deck()

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1 = input("p1 name")
        name2 = input("p2 name")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()
    def drawn_card(self, p1c, p2c, p1n, p2n):
        d = "{} drew {}, {} drew {}".format(p1n, p1c, p2n, p2c)
        print(d)
    def wins(self, winner):
        w = "{} wins this round".format(winner)
        print(w)
    
    def play_game(self):
        cards = self.deck.deck_cards
        print("beginning war!")
        while len(cards) >= 2:
            response = input("q to quit. Any key to play:")
            if response == "q":
                break
            else:
                p1c = self.deck.draw_card()
                p2c = self.deck.draw_card()
                p1n = self.p1.name
                p2n = self.p2.name
                self.drawn_card(p1c, p2c, p1n, p2n)
                if p1c > p2c:
                    self.p1.wins +=1
                    self.wins(self.p1.name)
                else:
                    self.p2.wins +=1
                    self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2)
    print("War is over. {} won the game.".format(win))

def winner(self, p1, p2):
    if p1.wins > p2.wins:
        return p1.name
        elif p1.wins == p2.wins:
            return "It was a tie!"
    else:
        return p2.name

game = Game()
game.play_game()
