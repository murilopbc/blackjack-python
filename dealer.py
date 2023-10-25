import random


class Dealer:
    def __init__(self, identificacao):
        self.cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K', 'A']
        self.identificacao = identificacao

    def distribuir_carta(self):
        carta = random.choice(self.cartas)
        return carta
