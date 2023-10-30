import random
from jogador import Jogador


class Dealer:
    def __init__(self, identificacao):
        self.cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K', 'A']
        self.identificacao = identificacao

    def distribuir_carta(self):
        carta = random.choice(self.cartas)
        return carta

    def vencedor(self, jogadores):
        maior_pontuacao = -1
        nome_vencedor = None

        for jogador in jogadores:
            pontos = jogador.total_cartas()
            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                nome_vencedor = jogador.nome
            if pontos == 21:
                nome_vencedor = jogador.nome
        return nome_vencedor

    def perder(self, jogadores):
        nome_perdedor = None

        for jogador in jogadores:
            pontos = jogador.total_cartas()
            if pontos > 21:
                nome_perdedor = jogador.nome

        return nome_perdedor
