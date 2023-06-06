

from .deck import Deck
from .player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_starting_cards(self):
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())


    def play_game(self):
        self.deal_starting_cards()
        print("Player's hand:", ", ".join(str(card) for card in self.player.hand))
        print("Dealer's hand:", str(self.dealer.hand[0]), "<hidden card>")

        player_turn = True

        while player_turn:
            choice = input("Do you want a hit or stay? (h/s): ")

            if choice == 'h':
                self.player.add_card(self.deck.deal_card())
                print("Player's hand:", ", ".join(str(card) for card in self.player.hand))

                if self.player.get_hand_value() > 21:
                    print("BUSTTTT!!!! YOU LOOSE!!")
                    player_turn = False
            elif choice == 's':
                player_turn = False
        
        if self.player.get_hand_value() <= 21:
            while self.dealer.get_hand_value() < 17:
                self.dealer.add_card(self.deck.deal_card())

            print("Dealer's hand:", ", ".join(str(card) for card in self.dealer.hand))


            player_value = self.player.get_hand_value()
            dealer_value = self.dealer.get_hand_value()

            if dealer_value > 21:
                print("Dealer busts! You win.")
            elif dealer_value > player_value:
                print("Dealer wins.")
            elif dealer_value < player_value:
                print("You win.")
            else:
                print("It's a tie.")


