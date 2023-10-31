class Jogador:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.cartas = []
        self.pontos = []

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def total_cartas(self):
        valor_total = 0
        for carta in self.cartas:
            if carta in ['Q', 'J', 'K']:
                valor_total += 10
            elif carta in ["A"]:
                valor_total += 1
            else:
                valor_total += carta

        return valor_total
