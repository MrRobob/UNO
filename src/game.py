from src.player import Player, Bot  
from src.card import Card
from src.utils import create_deck, is_valid_card
from src.handlers import choose_color, handle_plus2, handle_plus4, handle_mische_alle_karten, aussetzen

class Game:  
    def __init__(self):  
        self.deck = create_deck()  
        self.players = [Player('Player'), Bot('Bot')]  
        self.current_player_index = 0 
        self.current_card = None

    def start_game(self):  
        for player in self.players:  
            for _ in range(7):  
                player.draw_card(self.deck)

        while True:
            self.current_card = self.deck.pop()
            if self.current_card.color != "Schwarz" and self.current_card.value != "Aussetzen":
                break
            else:
                self.deck.insert(0, self.current_card)
        print("Die Startkarte ist:", self.current_card)
  
    def choose_card_from_hand(self, hand):
        valid_cards = [card for card in hand if is_valid_card(self, card)]
        if not valid_cards:
            print("Keine gültigen Karten zum Spielen. Ziehe eine Karte.")
            return None

        print("\nWähle eine Karte zum Spielen:")
        for idx, card in enumerate(valid_cards):
            print(f"{idx + 1}: {card}")

        while True:
            choice = input("Gib die Nummer der Karte ein, die du spielen möchtest: ")
            if choice.isdigit() and 1 <= int(choice) <= len(valid_cards):
                chosen_card = valid_cards[int(choice) - 1]
                hand.remove(chosen_card)
                return chosen_card
            else:
                print("Ungültige Eingabe. Bitte versuche es erneut.")

    def play_turn(self):  
        player = self.players[self.current_player_index]  
        if isinstance(player, Bot):
            print(f"{player}'s Zug:")
        else:
            print(f"{player}'s Zug:")
            print(f"Deine Karten: {', '.join(str(card) for card in player.hand)}")
        
        if isinstance(player, Bot):  
            played_card = player.play(self.current_card, self.deck)  
        else:  
            played_card = self.choose_card_from_hand(player.hand)  
        
        if played_card:  
            self.current_card = played_card  
            print(f"{player} spielt {self.current_card}")

            same_cards = [card for card in player.hand if card.color == played_card.color and card.value == played_card.value]

            if played_card.color != "Schwarz" and played_card.value != "+2" and same_cards:
                print(f"{player} hat weitere {len(same_cards)} {played_card.color} {played_card.value} Karten und spielt diese ebenfalls.")
                for card in same_cards:
                    player.hand.remove(card)
        
            if played_card.value == "Aussetzen": 
                aussetzen(self) 
            elif played_card.value == "+2": 
                handle_plus2(self) 
            elif played_card.value == "Farbwechsel": 
                self.current_card.color = choose_color(self, player) 
            elif played_card.value == "+4": 
                if not handle_plus4(self, player): 
                    player.hand.append(played_card)  
                    self.current_player_index = (self.current_player_index - 1) % len(self.players) 
            elif played_card.value == "Mische alle Karten":
                handle_mische_alle_karten(self)        
        
        else:
            print(f"{player} zieht 1 Karte")
            player.draw_card(self.deck)
            drawn_card = player.hand[-1]
            if is_valid_card(self, drawn_card):
                print(f"{player} spielt die gezogene Karte: {drawn_card}")
                player.hand.remove(drawn_card)
                self.current_card = drawn_card
                if drawn_card.value == "Aussetzen":
                    aussetzen(self)
                elif drawn_card.value == "+2":
                    handle_plus2(self)
                elif drawn_card.value == "Farbwechsel":
                    self.current_card.color = choose_color(self, player)
                elif drawn_card.value == "+4":
                    if not handle_plus4(self, player):
                        player.hand.append(drawn_card)
                        self.current_player_index = (self.current_player_index - 1) % len(self.players)
                elif drawn_card.value == "Mische alle Karten":
                    handle_mische_alle_karten(self)
            else:
                pass

        self.current_player_index = (self.current_player_index + 1) % len(self.players)