from random import shuffle
#Метод Shuffle из модуля random случайным образом перемешивает итерируемый обьект

class Card:
    suits = ("Пикей",
             "Червей",
             "Бубей",
             "Треф")
    
    values = (None, None, "2", "3", "4",
              "5", "6", "7",
              "8", "9", "10",
              "Валет", "Дама",
              "Король", "Туз")

    def __init__(self, v, s):
        #suit и value - целые числа
        self.value = v
        self.suit = s

    def __lt__(self, other): # метод для a < b
        if self.value < other.value:
            return True
        if self.value == other.value and self.suit < other.suit:
            return True
        return False

    def __gt__(self, other): # метод для a > b
        if self.value > other.value:
            return True
        if self.value == other.value and self.suit > other.suit:
            return True
        return False

    def __repr__(self):
        s = self.values[self.value] + " " + self.suits[self.suit]
        return s

class Deck: #колода карт
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return # return None
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("имя игрока 1: ")
        name2 = input("имя игрока 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print("{} Забирает карты {} {} {}".format(winner, len(self.deck.cards), self.p1.wins, self.p2.wins))

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} кладет {}, а {} кладет {}"
        print(d.format(p1n, p1c, p2n, p2c))

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            response = input("\nНажмите Х для выхода")
            if response == "X" or response == "Х":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("Игра окончена. {} Выиграл!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "Ничья!"
        
                

"""
c1 = Card(10, 2)
c2 = Card(11, 2)
print(c1 < c2)
deck = Deck()
for card in deck.cards:
    print(card)
"""
game = Game()
game.play_game()
