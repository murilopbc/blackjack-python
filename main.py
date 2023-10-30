from dealer import Dealer
from jogador import Jogador

dealer = Dealer("Croupier")
jogadores = []

qtd_jogadores = int(input("Quantos jogadores participarão?: "))

if qtd_jogadores <= 1:
    print("Valor Inválido")
else:
    for i in range(qtd_jogadores):
        nome = (input(f"Digite o nome do Jogador {i + 1}: "))
        idade = (int(input(f"Digite a idade do Jogador {i + 1}: ")))
        if idade < 18:
            print("Você é de menor! Não é permitido jogar")
            exit()
        else:
            jogador = Jogador(nome, idade)
            jogador.cartas = [dealer.distribuir_carta(), dealer.distribuir_carta()]
            jogadores.append(jogador)

    dealer.cartas = [dealer.distribuir_carta(), dealer.distribuir_carta()]

    for jogador in jogadores:
        print(f"{jogador.getNome()}'s cartas: {jogador.cartas}, Pontuação: {jogador.total_cartas()}")

    for jogador in jogadores:
        while jogador.total_cartas() < 21:
            acao = input(f"{jogador.nome}, deseja 'pedir' ou 'passar'? ").lower()
            if acao == 'pedir':
                carta = dealer.distribuir_carta()
                jogador.cartas.append(carta)
                print(f"{jogador.nome} recebeu a carta: {carta}")
                print(f"{jogador.getNome()}`s cartas:{jogador.cartas}, Pontuação: {jogador.total_cartas()}")
            elif acao == 'passar':
                break
    print(f"{dealer.vencedor(jogadores)}, você venceu!")
    print(f"{dealer.perder(jogadores)}, infelizmente você perdeu!")
