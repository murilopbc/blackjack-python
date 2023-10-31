import random


class Dealer:
    def __init__(self, identificacao: str):
        self.cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K']
        self.identificacao = identificacao

    def distribuirCarta(self, jogador):
        jogadorCarta = []

        for i in range(2):
            carta = random.choice(self.cartas)
            jogadorCarta.append(carta)
            self.cartas.remove(carta)
        jogador.setCartas(jogadorCarta)
    def comprarCarta(self):
        carta = random.choice(self.cartas)
        return carta

    def vencedor(self, jogadores):
        vencedor = None
        maiorPontuacao = -1

        for jogador in jogadores:
            pontos = jogador.total_cartas()
            if pontos > maiorPontuacao and pontos <= 21:
                maiorPontuacao = pontos
                vencedor = jogador.nome

        return f"Jogador Vencedor: {vencedor}\nPontos: {maiorPontuacao}"
    def parar(self, jogadores):
        for jogador in jogadores:
            if jogador.getJogou() == False:
                return False
        return True

