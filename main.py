import random

cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
baralho = cartas * 4

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

    def calcular_pontuacao(self):
        pontuacao = 0
        as_contagem = 0
        for carta in self.cartas:
            if carta == 'A':
                as_contagem += 1
            pontuacao += cartas.index(carta) + 2

        while as_contagem > 0 and pontuacao > 21:
            pontuacao -= 10
            as_contagem -= 1

        return pontuacao

class Dealer:
    def __init__(self, identificacao):
        self.cartas = []
        self.identificacao = identificacao

    def distribuir_carta(self, baralho):
        carta = random.choice(baralho)
        baralho.remove(carta)
        return carta

    @staticmethod
    def embaralhar(baralho):
        random.shuffle(baralho)

def criar_baralho():
    baralho = cartas * 4
    Dealer.embaralhar(baralho)
    return baralho

def jogar_blackjack(num_jogadores):
    baralho = criar_baralho()
    dealer = Dealer("Croupier")
    jogadores = []

    for i in range(num_jogadores):
        jogador = Jogador(input(f"Digite o nome do Jogador {i + 1}: "))
        jogador.cartas = [dealer.distribuir_carta(baralho), dealer.distribuir_carta(baralho)]
        jogadores.append(jogador)

    dealer.cartas = [dealer.distribuir_carta(baralho), dealer.distribuir_carta(baralho)]

    for jogador in jogadores:
        print(f"{jogador.nome}'s cartas: {jogador.cartas}, Pontuação: {jogador.calcular_pontuacao()}")

    print(f"Carta do dealer ({dealer.identificacao}): {dealer.cartas[0]}")

    for jogador in jogadores:
        while jogador.calcular_pontuacao() < 21:
            acao = input(f"{jogador.nome}, deseja 'pedir' ou 'passar'? ").lower()
            if acao == 'pedir':
                carta = dealer.distribuir_carta(baralho)
                jogador.cartas.append(carta)
                print(f"{jogador.nome} recebeu a carta: {carta}")
                print(f"{jogador.nome}'s cartas: {jogador.cartas}, Pontuação: {jogador.calcular_pontuacao()}")
            elif acao == 'passar':
                break

    while sum(cartas.index(carta) + 2 for carta in dealer.cartas) < 17:
        carta = dealer.distribuir_carta(baralho)
        dealer.cartas.append(carta)

    print(f"Cartas do dealer ({dealer.identificacao}): {dealer.cartas}")

    for jogador in jogadores:
        if jogador.calcular_pontuacao() > 21:
            print(f"{jogador.nome} estourou! {jogador.nome} perdeu.")
        elif sum(cartas.index(carta) + 2 for carta in dealer.cartas) > 21:
            print(f"Dealer ({dealer.identificacao}) estourou! {jogador.nome} vence.")
        elif jogador.calcular_pontuacao() > sum(cartas.index(carta) + 2 for carta in dealer.cartas):
            print(f"{jogador.nome} vence!")
        elif jogador.calcular_pontuacao() < sum(cartas.index(carta) + 2 for carta in dealer.cartas):
            print(f"Dealer ({dealer.identificacao}) vence {jogador.nome}.")
        else:
            print(f"{jogador.nome} empatou!")

if __name__ == "__main__":
    num_jogadores = int(input("Quantos jogadores participarão? "))
    jogar_blackjack(num_jogadores)

