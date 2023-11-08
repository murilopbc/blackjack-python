import random


# CRIAÇÃO DA CLASSE DEALER - CARTAS DO JOGO

class Dealer:
    def __init__(self, id):
        self.cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K']
        self.id = ""

# FUNÇÃO DE COMPRAR UMA CARTA ALEATÓRIA

    def sortearCarta(self):
        carta = random.choice(self.cartas)
        return carta

# FUNÇÃO DO DEALER DE DISTRIBUIR 2 CARTAS PARA CADA JOGADOR NO INÍCIO DO JOGO

    def distribuirCarta(self):
        carta = self.sortearCarta()
        return carta

# FUNÇÃO DO JOGADOR VENCEDOR

    def vencedor(self, jogadores, apostas):
        vencedor = None
        maiorPontuacao = -1

        for jogador in jogadores:
            pontos = jogador.totalCartas()
            if maiorPontuacao < pontos <= 21:
                maiorPontuacao = pontos
                vencedor = jogador

        vencedor.saldo = sum(apostas)


# SE O VENCEDOR APOSTOU, ELE GANHA A APOSTA

        if vencedor.apostou:
            return f"\nVencedor: {vencedor.getNome()}\nPontos: {maiorPontuacao}\nSaldo final: R${vencedor.saldo}"
        else:
            return f"\nVencedor: {vencedor.getNome()}\nPontos: {maiorPontuacao}"

# FUNÇÃO SE TODOS OS JOGADORES PARARAM DE JOGAR(PASSARAM A VEZ)

    def pararam(self, jogadores):
        for jogador in jogadores:
            if not jogador.parou:
                return False
        return True
