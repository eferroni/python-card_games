import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# GAME SETUP
player_one = Player('One')
player_two = Player('Two')
new_deck = Deck()
new_deck.shuffle()
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

additional_cards = 3

# game on
round_num = 0
while game_on:
    round_num += 1
    if round_num % 100 == 0:
        print('Shuffle')
        player_one.shuffle()
        player_two.shuffle()

    print(f'Round {round_num}, {len(player_one.all_cards)} - {len(player_two.all_cards)}')
    if len(player_one.all_cards) == 0:
        print('Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player One wins!')
        game_on = False
        break

    # NEW ROUND
    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    war_on = True
    while war_on:
        # print('{} x {}'.format(player_one_cards[-1].value, player_two_cards[-1].value))

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war_on = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war_on = False
        else:
            print('WAR!!!')
            for x in range(additional_cards+1):
                if len(player_one.all_cards) == 0:
                    print('Player Two wins at War!')
                    game_on = False
                    war_on = False
                    break

                if len(player_two.all_cards) == 0:
                    print('Player One wins at War!')
                    game_on = False
                    war_on = False
                    break

                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
