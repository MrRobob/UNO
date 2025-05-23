from src.player import Player, Bot
from src.card import Card
import random

def choose_color(game, player):
    if isinstance(player, Bot):
        chosen_color = player.choose_most_needed_color()
        print(f"{player} wählt {chosen_color}")
        return chosen_color
    else:
        farben = ["Rot", "Gelb", "Grün", "Blau"]
        print("Wähle eine Farbe:")
        for index, farbe in enumerate(farben):
            print(f"{index + 1}: {farbe}")
        chosen_color = farben[int(input("Gib die Nummer der gewünschten Farbe ein: ")) - 1]
        return chosen_color

def handle_plus2(game): 
    next_player_index = (game.current_player_index + 1) % len(game.players) 
    cards_to_draw = 2
    while True: 
        next_player = game.players[next_player_index] 
        plus2_cards = [card for card in next_player.hand if card.value == "+2"]
        
        if plus2_cards:
            card_to_play = plus2_cards[0]
            next_player.hand.remove(card_to_play)
            game.current_card = card_to_play
            print(f"{next_player} spielt {game.current_card}")
            cards_to_draw += 2
            if cards_to_draw > 4:
                cards_to_draw = 4
            next_player_index = (next_player_index + 1) % len(game.players)
        else:
            print(f"{next_player} zieht {cards_to_draw} Karten") 
            for _ in range(cards_to_draw):
                next_player.draw_card(game.deck)
            break
    game.current_player_index = next_player_index

def handle_plus4(game, player):
    if all(card.color == "Schwarz" or (card.color != game.current_card.color and card.value != game.current_card.value) for card in player.hand):
        game.current_card.color = choose_color(game, player)
        next_player_index = (game.current_player_index + 1) % len(game.players)
        next_player = game.players[next_player_index]
        
        print(f"{next_player} zieht 4 Karten.")
        for _ in range(4):
            next_player.draw_card(game.deck)
    else:
        if not isinstance(player, Bot):
            print("Du kannst die +4 Karte nur spielen, wenn du keine andere Option hast.")
        return False
    return True

def handle_mische_alle_karten(game): 
    game.current_card.color = choose_color(game, game.players[game.current_player_index])
    alle_karten = [] 
    for player in game.players: 
        alle_karten.extend(player.hand) 
        player.hand.clear() 
    random.shuffle(alle_karten) 

    spieler_index = game.current_player_index 
    while alle_karten: 
        game.players[spieler_index].hand.append(alle_karten.pop()) 
        spieler_index = (spieler_index + 1) % len(game.players)

def aussetzen(game):  
    game.current_player_index = (game.current_player_index + 1) % len(game.players)