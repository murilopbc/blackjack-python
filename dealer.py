import random


class Dealer:
    def __init__(self, identificacao: str):
        self.cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K']
        self.identificacao = identificacao

    def comprarCarta(self):
        carta = random.choice(self.cartas)
        return carta

    def distribuirCarta(self, jogador):
        carta = self.comprarCarta()
        return carta

    def vencedor(self, jogadores):
        vencedor = None
        maiorPontuacao = -1

        for jogador in jogadores:
            pontos = jogador.totalCartas()
            if maiorPontuacao < pontos <= 21:
                maiorPontuacao = pontos
                vencedor = jogador.getNome()

        return f"\nJogador Vencedor: {vencedor}\nPontos: {maiorPontuacao}"

    def pararam(self, jogadores):
        for jogador in jogadores:
            if not jogador.parou:
                return False
        return True
