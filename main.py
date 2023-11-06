from dealer import Dealer
from jogador import Jogador
# criação do dealer
dealer = Dealer("Croupier")
# criação da lista jogadores
jogadores = []
# criação do while true > enquanto (loop)
while True:
    # input do usuário sobre a quantidade de jogadores
    qtd_jogadores = int(input("Quantos jogadores participarão?: "))
    # condição se a quantidade de jogadores for = ou > que 2
    if qtd_jogadores >= 2:
        for i in range(qtd_jogadores):
            # input de nome e idade
            nome = input(f"\nDigite o nome do Jogador {i + 1}: ")
            idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
            if idade < 18:
                # se o jogador for de menor ele não poderá jogar
                print("Você é de menor! Não é permitido jogar")
                exit()
            else:
                # senão o dealer vai distribuir as 2 cartas inicias para cada jogador
                jogador = Jogador(nome, idade)
                jogador.cartas = [dealer.distribuirCarta(jogador), dealer.distribuirCarta(jogador)]
                jogadores.append(jogador)
        # exibir o nome, as cartas, e a pontuação de cada jogador
        for jogador in jogadores:
            print(f"\nJogador: {jogador.getNome()}")
            print(f"Cartas: {jogador.cartas}")
            print(f"Pontuação: {jogador.totalCartas()}")

    else:
        # condição se o usuário digitar um valor menor que 2 : não tem como jogar o jogo com 1 jogador!
        print("Valor inválido!!!")
        break

    for i in range(qtd_jogadores):
        while True:

            if dealer.pararam(jogadores):
                break
            # jogador tem duas opções: pedir ou passar. Se ele pedir ele vai acumulando os pontos
            acao = int(input(f"\n{jogadores[i].getNome()}, digite '1' para pedir a carta ou '2' para passar sua vez: "))
            if acao == 1:
                carta = dealer.distribuirCarta(Jogador)
                jogadores[i].cartas.append(carta)
                print(f"\nJogador: {jogadores[i].getNome()}")
                print(f"Cartas: {jogadores[i].cartas}")
                print(f"Pontuação: {jogadores[i].totalCartas()}")
                # se o jogador alcançar 21 ele ganha
                if jogadores[i].totalCartas() == 21:
                    print(f"Jogador(a) {jogadores[i].getNome()} venceu o jogo!")
                    exit()
                # se estiver jogando entre 2 jogadores, quando um jogador perder o outro jogador automaticamente ganhará
                elif qtd_jogadores == 2 and jogadores[i].totalCartas() > 21:
                    print("Você perdeu!\n\n")
                    print(dealer.vencedor(jogadores))
                    exit()
                # se um jogador ultrapassar mais que 21 pontos ele perde
                elif jogadores[i].totalCartas() > 21:
                    print(f"\n{jogadores[i].getNome()}, você perdeu, pois seus pontos ultrapassaram 21!\n")
                    break
            # jogador escolheu parar. Ele não terá mais chance de jogar novamente
            if acao == 2:
                jogadores[i].jogou(True)
                break
    # função do jogador vencedor
    print(dealer.vencedor(jogadores))
    break
