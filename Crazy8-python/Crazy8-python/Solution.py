# Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def matches(self, other):
        return self.suit == other.suit or self.rank == other.rank or self.rank == '8'
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck Class (without using random.shuffle)
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.manual_shuffle()

    def manual_shuffle(self):
        """Manually shuffle the deck without using random"""
        shuffled = []
        step = 3  # Shuffle with a step pattern
        while self.cards:
            shuffled.append(self.cards.pop(0))
            if len(self.cards) > step:
                shuffled.append(self.cards.pop(step))
        self.cards = shuffled

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None
    
    def is_empty(self):
        return len(self.cards) == 0

# Hand Class
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def play_card(self, top_card):
        for card in self.cards:
            if card.matches(top_card):
                self.cards.remove(card)
                return card
        return None
    
    def has_cards(self):
        return len(self.cards) > 0

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

# Player Class
class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.hand = Hand()
        self.is_human = is_human

    def draw_card(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.add_card(card)

    def play_turn(self, top_card, deck):
        played_card = self.hand.play_card(top_card)
        if played_card:
            print(f"{self.name} played: {played_card}")
            return played_card
        else:
            print(f"{self.name} had to draw a card.")
            self.draw_card(deck)
            return None
        
    def has_won(self):
        return not self.hand.has_cards()

    def __str__(self):
        return f"{self.name}: {self.hand}"

# Game Class
class Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.top_card = self.deck.draw_card()
        self.current_player_index = 0
    
    def start_game(self):
        for player in self.players:
            for _ in range(5):
                player.draw_card(self.deck)
        print(f"Starting Card: {self.top_card}")
    
    def play_game(self):
        self.start_game()
        while True:
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s Turn. Top Card: {self.top_card}")
            played_card = current_player.play_turn(self.top_card, self.deck)
            if played_card:
                self.top_card = played_card
            if current_player.has_won():
                print(f"\n{current_player.name} wins the game!")
                break
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

if __name__ == "__main__":
    game = Game(2)
    game.play_game()
