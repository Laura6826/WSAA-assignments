# Weekly Assignment 02. carddraw.py
# The aim of this program is to output use the Deck of Cards API to draw 5 cards from a shuffled deck and print the value and suit of each card.
# Author: Laura Lyons

# The original code works as expected, but it does not handle any exceptions that may occur during the API requests.
# The code below adds exception handling to the program to catch and display any errors that may occur during the requests.

import requests
import json

def deal_cards():
    try:
        # Step 1: Shuffle a new deck
        shuffle_url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        shuffle_response = requests.get(shuffle_url)
        shuffle_response.raise_for_status()  # Check for HTTP errors
        print("Response content:", shuffle_response.text)  # Inspect the response content
        deck = shuffle_response.json()
        deck_id = deck["deck_id"]

        # Step 2: Draw 5 cards from the shuffled deck
        draw_url = f"https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
        draw_response = requests.get(draw_url)
        draw_response.raise_for_status()  # Check for HTTP errors
        cards = draw_response.json()["cards"]

        # Step 3: Print the value and suit of each card
        print("Dealt Cards:")
        for card in cards:
            print(f"{card['value']} of {card['suit']}")

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
    except json.JSONDecodeError as errj:
        print("JSON Decode Error:", errj)
        print("Response content:", shuffle_response.text if shuffle_response else "No response")

if __name__ == "__main__":
    deal_cards()

# The code above adds exception handling to the program to catch and display any errors that may occur during the requests.
# The code below adds exception handling to the program to catch and display any errors that may occur during the requests. 
