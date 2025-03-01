# Weekly Assignment 02. carddraw.py
# The aim of this program is to output use the Deck of Cards API to draw 5 cards from a shuffled deck and print the value and suit of each card.
# Author: Laura Lyons

import requests 
import json

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

if __name__ == "__main__":
    deal_cards()
