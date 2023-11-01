from dealer import Dealer
from jogador import Jogador

dealer = Dealer("Croupier")

jogadores = []

while True:
    qtd_jogadores = int(input("Quantos jogadores participarão?: ")),
    if qtd_jogadores > 1:
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
            print(f"\nJogador: {jogador.getNome()}")
            print(f"Cartas: {jogador.cartas}")
            print(f"Pontuação: {jogador.totalCartas()}")

    else:
        print("Valor invalido!!!")
        break

    for i in range(qtd_jogadores):
        while True:

            if dealer.pararam(jogadores):
                break

            acao = int(input(f"\n{jogadores[i].getNome()}, digite '1' para pedir a carta ou '2' para passar sua vez: "))
            if acao == 1:
                carta = dealer.distribuirCarta(Jogador)
                jogadores[i].cartas.append(carta)
                print(f"\nJogador: {jogadores[i].getNome()}")
                print(f"Cartas: {jogadores[i].cartas}")
                print(f"Pontuação: {jogadores[i].totalCartas()}")

                if jogadores[i].totalCartas() == 21:
                    print(f"Jogador(a) {jogadores[i].getNome()} venceu o jogo!")
                    exit()

                elif jogadores[i].totalCartas() > 21:
                    print(f"Jogador: {jogadores[i].getNome()}")
                    print(f"Pontuação: {jogadores[i].totalCartas()}")
                    print("Você perdeu, pois seus pontos ultrapassaram 21!\n")
                    break

            if acao == 2:
                jogadores[i].jogou(True)
                break

    print(dealer.vencedor(jogadores))
    break
