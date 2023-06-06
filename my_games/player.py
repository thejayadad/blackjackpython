
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        num_aces = 0

        for card in self.hand:
            if card.rank.isdigit():
                value += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                num_aces += 1

        for _ in range(num_aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1

        return value
