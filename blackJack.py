import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 0}

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
    def __init__(self, name, money = 0):
        self.name = name
        self.all_cards = []
        self.money = money
        self.aces = 0
        self.values = []

    def add_cards(self, new_card):
        self.all_cards.append(new_card)
        if new_card.value == 0:
            self.aces += 1
        self.count_cards()

    def count_cards(self):
        self.values = []
        value = sum(item.value for item in self.all_cards)
        if self.aces > 0:
            for i in range(self.aces+1):
                self.values.append((value+(10*i)+self.aces))
        else:
            self.values.append(value)

    def reset(self):
        self.all_cards = []
        self.aces = 0
        self.values = []

    def __str__(self):
        return f'Player {self.name} has {money} dolars.'

player_one = Player('You', 100)
dealer = Player('Dealer')
new_deck = Deck()
new_deck.shuffle()

game_on = True
# game on
while game_on:
    # reset the hands
    player_one.reset()
    dealer.reset()

    # ask for bet
    bet = 0
    while bet > player_one.money or bet == 0:
        try:
            bet = int(input('Whats your bet? 0 to stop playing: '))
            if bet == 0:
                print('OK, bye! You leave with {} dolars'.format(player_one.money))
                game_on = False
                break

            elif bet > player_one.money:
                print('Choose a bet between 1 and {}'.format(player_one.money))
        except:
            print('Inform a value!')
    else:
        print(f'{bet} dolar!! OK, lets go!')

    if not game_on:
        break

    round_on = True
    while round_on:
        dealer.add_cards(new_deck.deal_one())
        dealer.add_cards(new_deck.deal_one())
        print('Dealer has: {} - *'.format(dealer.all_cards[0].rank))

        player_one.add_cards(new_deck.deal_one())
        player_one.add_cards(new_deck.deal_one())
        print('You have: {} {}'.format(" - ".join([str(x.rank) for x in player_one.all_cards]), player_one.values))

        action = 'Y'
        while action == 'Y':
            action = input('Do you want to Hit another card (Y for yes)?')
            if action == 'Y':
                player_one.add_cards(new_deck.deal_one())
                print('You have: {} {}'.format(" - ".join([str(x.rank) for x in player_one.all_cards]), player_one.values))
                if all(x > 21 for x in player_one.values):
                    print('Sorry you lose!')
                    player_one.money -= bet
                    round_on = False
                    break
        if round_on:
            print('Dealer has: {} {}'.format(" - ".join([str(x.rank) for x in dealer.all_cards]), dealer.values))
            while all(x < 17 for x in dealer.values):
                dealer.add_cards(new_deck.deal_one())
                print('Dealer have: {} {}'.format(" - ".join([str(x.rank) for x in dealer.all_cards]), dealer.values))
                if all(x > 21 for x in dealer.values):
                    print('You Win!')
                    player_one.money += bet
                    round_on = False
                    break

        if round_on:
            if max(p for p in player_one.values if p <= 21) > max(d for d in dealer.values if d <= 21):
                print('Great, you won!')
                player_one.money += bet
            elif max(p for p in player_one.values if p <= 21) < max(d for d in dealer.values if d <= 21):
                print('Sorry you lose!')
                player_one.money -= bet
            else:
                print('We have a tie!')

            round_on = False
            
        print(f'Now you have {player_one.money} dolars')

        if player_one.money == 0:
            print('You dont have more money, goodbye!')
            game_on = False
            break
