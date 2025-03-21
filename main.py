'''
Deck mit 108 Karten
- 4 Farben (rot, gelb, grün, blau, schwarz) 
- 2x 0-9
- 2x Aussetzen
- 2x +2
- 4x Farbwahl (schwarz)
- 4x Farbwahl +4 (schwarz)
- 2x Karten mischen (schwarz)

Funktionen für die einzelnen Aktionen:
- Deck mischen (einmalig)
- Karten austeilen (7 Karten pro Spieler)
- Spielerkarten anzeigen
- Botkarten verdeckt anzeigen
- erste Karte aufdecken
- Minigame um festzulegen wer beninnt
    - Schere, Stein, Papier
- Karte spielen
- Bot spielt Karte
- Karte ziehen
- Bot zieht Karte
- 2 Karten ziehen
- Bot zieht 2 Karten
- 4 Karten ziehen
- Bot zieht 4 Karten
- Farbe wählen
- Bot wählt Farbe
- Aussetzen
- Bot setzt aus
- Karten mischen
- Bot mischt Karten
- UNO
- Bot sagt UNO
- Gewonnen
- Bot gewinnt
- Spiel beenden
- Bot beendet Spiel
- Spielstand anzeigen
- Bot Spielstand anzeigen
'''

from src.game import Game

def main():
    game = Game()
    game.start_game()

    while True:
        game.play_turn()
        if len(game.players[0].hand) == 0:
            print(f"{game.players[0]} hat gewonnen!")
            break
        elif len(game.players[1].hand) == 0:
            print(f"{game.players[1]} hat gewonnen!")
            break
        input("Weiter mit Enter...")

if __name__ == "__main__":
    main()