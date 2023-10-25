from dealer import Dealer
from jogador import Jogador

dealer = Dealer("Croupier")
jogadores = []

qtd_jogadores = int(input("Quantos jogadores participarão?: "))

for i in range(qtd_jogadores):
    nome = (input(f"Digite o nome do Jogador {i + 1}: "))
    idade = (int(input(f"Digite a idade do Jogador {i + 1}: ")))
    jogador = Jogador(nome, idade)
    jogador.cartas = [dealer.distribuir_carta(), dealer.distribuir_carta()]
    jogadores.append(jogador)

dealer.cartas = [dealer.distribuir_carta(), dealer.distribuir_carta()]

for jogador in jogadores:
    print(f"{jogador.getNome()}'s cartas: {jogador.cartas}, Pontuação: {jogador.total_cartas()}")

print(f"Carta do dealer ({dealer.identificacao}): {dealer.cartas[0]}")

for jogador in jogadores:
    while jogador.total_cartas() < 21:
        acao = input(f"{jogador.nome}, deseja 'pedir' ou 'passar'? ").lower()
        if acao == 'pedir':
            carta = dealer.distribuir_carta()
            jogador.cartas.append(carta)
            print(f"{jogador.nome} recebeu a carta: {carta}")
            print(f"Nome: {jogador.nome}\nCartas:{jogador.cartas}, Pontuação: {jogador.total_cartas()}")
        elif acao == 'passar':
            break
        if jogador.total_cartas() == 21:
            print(f"Parabéns {jogador.nome}. Você Venceu!")
        if jogador.total_cartas() > 21:
            print(f"{jogador.nome}, infelizmente você perdeu!")

print(f"Cartas do dealer ({dealer.identificacao}): {dealer.cartas}")




