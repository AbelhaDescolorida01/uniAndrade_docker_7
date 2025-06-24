class Inimigo:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def atacar(self):
        print(f"{self.nome} ataca causando {self.dano} de dano!")
