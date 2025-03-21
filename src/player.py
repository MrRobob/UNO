class Player:  
    def __init__(self, name):  
        self.name = name  
        self.hand = []  

    def draw_card(self, deck):  
        if deck:  
            self.hand.append(deck.pop())  

    def play_card(self, card):  
        self.hand.remove(card)  
        return card  

    def __str__(self):  
        return self.name  

class Bot(Player):
    def choose_most_needed_color(self):
        color_count = {"Rot": 0, "Gelb": 0, "Grün": 0, "Blau": 0}
        for card in self.hand:
            if card.color in color_count:
                color_count[card.color] += 1
        return max(color_count, key=color_count.get)

    def play(self, current_card, deck):  
        for card in self.hand:  
            if card.color == current_card.color or card.value == current_card.value:  
                return self.play_card(card)  
            elif card.color == "Schwarz":
                chosen_color = self.choose_most_needed_color()
                card.color = chosen_color 
                return self.play_card(card) 
        self.draw_card(deck)
        print(f"{self} zieht 1 Karte")
        drawn_card = self.hand[-1]
        if drawn_card.color == current_card.color or drawn_card.value == current_card.value or drawn_card.color == "Schwarz":
            return self.play_card(drawn_card)
        else:
            return None