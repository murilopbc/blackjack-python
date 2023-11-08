from dealer import Dealer
from jogador import Jogador

# CRIAÇÃO DO DEALER

dealer = Dealer("Croupier")

# CRIAÇÃO DA LISTA DE JOGADORES E DE APOSTAS

jogadores = []
apostas = []

# INÍCIO DO JOGO - INPUT DE NOME E IDADE

while True:
    print("\nWELCOME TO BLACKJACK!!!\n")
    qtd_jogadores = int(input("Digite a quantidade de jogadores: "))
    if qtd_jogadores >= 2:
        for i in range(qtd_jogadores):
            nome = input(f"\nDigite o nome do Jogador {i + 1}: ")
            idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
            if idade < 18:
                print("Você é de menor! Não é permitido jogar")
                exit()
            else:
                jogador = Jogador(nome, idade)
                jogador.cartas = [dealer.distribuirCarta(), dealer.distribuirCarta()]
                jogadores.append(jogador)
# APOSTA
                while True:
                    opcao = input("Você deseja apostar?: ")
                    if opcao == 'sim':
                        jogadores[i].apostou = True
                        print(f"Você tem {jogadores[i].saldo} reais de saldo!")
                        valor = float(input("Insira o valor da aposta: "))
                        if valor <= jogadores[i].saldo:
                            jogadores[i].saldo -= valor
                            apostas.append(valor)
                            print(f"{jogadores[i].getNome()}, você apostou {valor} reais")
                            break
                        else:
                            print("Saldo Insuficiente!")
                    elif opcao == 'não':
                        print("Ok, sem problemas!")
                        break
                    else:
                        print("Valor Inválido! Digite 'sim' ou 'não' para continuar! ")

# EXIBIR O NOME, AS CARTAS E A PONTUAÇÃO INICIAL DE CADA JOGADOR

        for jogador in jogadores:
            print(f"\nJogador: {jogador.getNome()}")
            print(f"Cartas: {jogador.cartas}")
            print(f"Pontuação: {jogador.totalCartas()}")

# NÃO É POSSIVEL JOGAR SOZINHO

    else:
        print("Valor inválido!!!")
        break

# INPUT DE 'PEDIR' OU 'PASSAR' A CARTA
# JOGADOR ACUMULA SEUS PONTOS

    for i in range(qtd_jogadores):
        while True:
            if dealer.pararam(jogadores):
                break
            acao = int(input(f"\n{jogadores[i].getNome()}, digite '1' para pedir a carta ou '2' para passar sua vez: "))
            if acao == 1:
                carta = dealer.distribuirCarta()
                jogadores[i].cartas.append(carta)
                print(f"\nJogador: {jogadores[i].getNome()}")
                print(f"Cartas: {jogadores[i].cartas}")
                print(f"Pontuação: {jogadores[i].totalCartas()}")

# SE O JOGADOR FAZER 21 PONTOS, ELE GANHA O JOGO

                if jogadores[i].totalCartas() == 21:
                    print(dealer.vencedor(jogadores, apostas))
                    print(f"Jogador(a) {jogadores[i].getNome()} venceu o jogo!")
                    print(f"Saldo final: {jogadores[i].saldo}")
                    exit()

# CONDIÇÃO VÁLIDA QUANDO ESTIVER JOGANDO APENAS 2 JOGADORES: QUANDO UM GANHA O OUTRO PERDE AUTOMATICAMENTE

                elif qtd_jogadores == 2 and jogadores[i].totalCartas() > 21:
                    print("Você perdeu!\n")
                    print(dealer.vencedor(jogadores, apostas))
                    exit()

# SE O JOGADOR ULTRAPASSAR 21 PONTOS, ELE PERDE

                elif jogadores[i].totalCartas() > 21:
                    print(f"\n{jogadores[i].getNome()}, você perdeu, pois seus pontos ultrapassaram 21!\n")
                    break

# JOGADOR ESCOLHEU 'PASSAR' A VEZ

            if acao == 2:
                break

# FUNÇÃO DO JOGADOR VENCEDOR
# EXIBE O NOME, A PONTUAÇÃO FINAL E O SALDO DA APOSTA

    print(dealer.vencedor(jogadores, apostas))
    break
