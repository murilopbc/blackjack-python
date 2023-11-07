# CRIAÇÃO DA CLASSE JOGADOR - ATRIBUTOS NOME E IDADE ESTÃO PRIVADOS

class Jogador:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
        self.cartas = []
        self.pontos = []
        self.parou = False
        self.saldo = 1000
        self.apostou = False

# FUNÇÃO GET PARA ACESSAR O NOME

    def getNome(self):
        return self.__nome

# FUNÇÃO GET PARA ACESSARA IDADE

    def getIdade(self):
        return self.__idade

# FUNÇÃO VALOR INDIVIDUAL DE CADA CARTA

    def totalCartas(self):
        valor_total = 0
        for carta in self.cartas:
            if carta in ['Q', 'J', 'K']:
                valor_total += 10
            elif carta == "A":
                valor_total += 1
            else:
                valor_total += carta
        return valor_total

    def jogou(self, tf):
        self.parou = tf

    def getJogou(self):
        return self.parou
