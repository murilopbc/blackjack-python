from dealer import Dealer
from jogador import Jogador

dealer = Dealer("Croupier")
jogadores = []

qtd_jogadores = int(input("Quantos jogadores participarão?: "))

if qtd_jogadores <= 1:
    print("Valor Inválido")
else:
    for i in range(qtd_jogadores):
        nome = input(f"\nDigite o nome do Jogador {i + 1}: ")
        idade = int(input(f"Digite a idade do Jogador {i + 1}: "))
        if idade < 18:
            print("Você é de menor! Não é permitido jogar")
            exit()
        else:
            jogador = Jogador(nome, idade)
            jogador.cartas = [dealer.distribuir_carta(), dealer.distribuir_carta()]
            jogadores.append(jogador)

    for jogador in jogadores:
        print(f"\nJogador: {jogador.getNome()}\nCartas: {jogador.cartas}\nPontuação: {jogador.total_cartas()}\n---------------")

for i in range(qtd_jogadores):
    while True:
        acao = input(f"\n{jogadores[i].nome}, deseja 'pedir' ou 'passar'? ").lower()
        if acao == 'pedir':
            carta = dealer.distribuir_carta()
            jogadores[i].cartas.append(carta)
            print(f"Jogador: {jogadores[i].getNome()}\nCartas: {jogadores[i].cartas}\nPontuação: {jogadores[i].total_cartas()}")
            if jogadores[i].total_cartas() > 21:
                print(f"{jogadores[i].getNome()}, você ultrapassou 21! Você perdeu!")
                break
        elif acao == 'passar':
            break

vencedor = dealer.vencedor(jogadores)
perdedor = dealer.perdedor(jogadores)
empate = dealer.empate(jogadores)

if vencedor:
    print(f"\n{dealer.vencedor(jogadores)}, você venceu!\n")
elif perdedor:
    print(f"\n{dealer.perdedor(jogadores)}, você perdeu!\n")
elif empate:
    print("\nO jogo terminou em empate.\n")
