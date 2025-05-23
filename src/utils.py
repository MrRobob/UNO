import random
from src.card import Card

def create_deck():  
    colors_and_values = {  
        "Rot": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "Aussetzen"],
        "Gelb": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "Aussetzen"],
        "Grün": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "Aussetzen"],
        "Blau": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "Aussetzen"],
        "Schwarz": ["+4", "Farbwechsel", "Mische alle Karten"]
    }
    deck = []  
    for color, values in colors_and_values.items():  
        for value in values:  
            deck.append(Card(color, value))  
            if value != "0":  
                deck.append(Card(color, value))  
            if color == "Schwarz" and (value == "+4" or value == "Farbwechsel" or value == "Mische alle Karten"): 
                deck.append(Card(color, value))  
                deck.append(Card(color, value))  
    random.shuffle(deck)  
    return deck

def is_valid_card(game, card):
    if card.color == "Schwarz" and card.value == "+4":
        return all(c.color == "Schwarz" or (c.color != game.current_card.color and c.value != game.current_card.value) for c in game.players[game.current_player_index].hand)
    return card.color == game.current_card.color or card.value == game.current_card.value or card.color == "Schwarz"