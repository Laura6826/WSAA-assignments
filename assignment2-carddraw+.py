# Weekly Assignment 02. carddraw+.py
# # The aim of this program is to output use the Deck of Cards API to draw 5 cards from a shuffled deck and print the value and suit of each card, and to identify the drawn cards.
# Author: Laura Lyons

import requests
import json

def check_hand(cards):
    # Extract values and suits from the drawn cards
    values = [card['value'] for card in cards]
    suits = [card['suit'] for card in cards]
    
    # Convert face cards to numbers for easy comparison
    value_conversion = {'ACE': 1, 'JACK': 11, 'QUEEN': 12, 'KING': 13}
    numeric_values = [value_conversion.get(value, value) for value in values]
    numeric_values = list(map(int, numeric_values))
    
    # Check for pairs and triples
    value_counts = {value: numeric_values.count(value) for value in numeric_values}
    pair = any(count == 2 for count in value_counts.values())
    triple = any(count == 3 for count in value_counts.values())
    
    # Check for a straight
    numeric_values.sort()
    straight = all(numeric_values[i] == numeric_values[i-1] + 1 for i in range(1, len(numeric_values)))
    
    # Check for a flush (all cards of the same suit)
    flush = len(set(suits)) == 1

    # Print congratulatory messages
    if pair:
        print("Congratulations! You've drawn a pair.")
    if triple:
        print("Congratulations! You've drawn a triple.")
    if straight:
        print("Congratulations! You've drawn a straight.")
    if flush:
        print("Congratulations! All cards are of the same suit.")

def deal_cards():
    # Step 1: Shuffle a new deck
    shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    shuffle_response = requests.get(shuffle_url)
    deck = shuffle_response.json()
    deck_id = deck["deck_id"]

    # Step 2: Draw 5 cards from the shuffled deck
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
    draw_response = requests.get(draw_url)
    cards = draw_response.json()["cards"]

    # Step 3: Print the value and suit of each card
    print("Dealt Cards:")
    for card in cards:
        print(f"{card['value']} of {card['suit']}")

    # Check the hand for pairs, triples, straights, and flushes
    check_hand(cards)

if __name__ == "__main__":
    deal_cards()
