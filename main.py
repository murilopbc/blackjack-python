from dealer import Dealer
from jogador import Jogador

dealer = Dealer("Croupier")
jogadores = []

qtd_jogadores = int(input("Quantos jogadores participarão?: "))

if qtd_jogadores <= 1:
    print("Valor Inválido. No mínimo 2 jogadores.")
else:
    for i in range(qtd_jogadores):
        nome = input(f"\nDigite o nome do Jogador {i + 1}: ")
        idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
        if idade < 18:
            print("Você é de menor! Não é permitido jogar")
            exit()
        else:
            jogador = Jogador(nome, idade)
            jogador.cartas = [dealer.distribuirCarta(jogador), dealer.distribuirCarta(jogador)]
            jogadores.append(jogador)

    for jogador in jogadores:
        print(
            f"\nJogador: {jogador.getNome()}\nCartas: {jogador.cartas}\nPontuação: {jogador.total_cartas()}\n---------------")

for i in range(qtd_jogadores):
    while True:
        acao = input(f"\n{jogadores[i].getNome()}, deseja 'pedir' ou 'passar'? ").lower()
        if acao == 'pedir':
            carta = dealer.distribuirCarta(Jogador)
            jogadores[i].cartas.append(carta)
            print(
                f"Jogador: {jogadores[i].getNome()}\nCartas: {jogadores[i].cartas}\nPontuação: {jogadores[i].total_cartas()}")
        elif acao == 'passar':
            break

