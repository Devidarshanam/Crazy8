from Solution import Card, Deck, Hand, Player, Game

# Main method for testing
def main():
    print("===== TESTING CRAZY 8 GAME =====")

    # Testing Card Class
    print("\n>>> Testing Card Class...")
    c1 = Card("Hearts", "8")
    c2 = Card("Diamonds", "8")
    c3 = Card("Hearts", "10")
    c4 = Card("Spades", "K")

    print(f"Card 1: {c1}")
    print(f"Card 2: {c2}")
    print(f"Card 3: {c3}")
    print(f"Card 4: {c4}")

    if c1.matches(c2):
        print("c1 matches c2 (Same Rank)")
    else:
        print("c1 does not match c2")

    if c1.matches(c3):
        print("c1 matches c3 (Same Suit)")
    else:
        print("c1 does not match c3")

    if c1.matches(c4):
        print("c1 matches c4 (Should be False)")
    else:
        print("c1 does not match c4")

    # Testing Deck Class
    print("\n>>> Testing Deck Class...")
    deck = Deck()
    print(f"Deck initialized with {len(deck.cards)} cards.")

    print("Drawing 3 cards manually...")
    for _ in range(3):
        print(f"Drawn Card: {deck.draw_card()}")

    print(f"Remaining cards in deck: {len(deck.cards)}")

    # Testing Hand Class
    print("\n>>> Testing Hand Class...")
    hand = Hand()
    hand.add_card(Card("Spades", "A"))
    hand.add_card(Card("Clubs", "5"))
    hand.add_card(Card("Diamonds", "8"))

    print(f"Hand contents: {hand}")
    top_card = Card("Diamonds", "3")
    print(f"Top Card: {top_card}")

    played_card = hand.play_card(top_card)
    if played_card:
        print(f"Playable Card Found: {played_card}")
    else:
        print("No Playable Card. Need to draw.")

    print(f"Hand size after playing: {len(hand.cards)}")

    # Testing Player Class
    print("\n>>> Testing Player Class...")
    player = Player("Alice")
    player.draw_card(deck)
    print(f"{player.name} has {len(player.hand.cards)} cards.")

    print("Attempting to play a turn...")
    played = player.play_turn(top_card, deck)
    if played:
        print(f"Played Card: {played}")
    else:
        print("No valid card found. Drew from deck.")

    print(f"Cards after playing: {len(player.hand.cards)}")

    # Testing Game Logic
    print("\n>>> Testing Game Class...")
    game = Game(2)
    game.play_game()

# Run the main method
main()
