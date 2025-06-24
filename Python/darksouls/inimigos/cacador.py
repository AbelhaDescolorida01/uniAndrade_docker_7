from inimigo import Inimigo

class cacador(Inimigo):
    def __init__(self, nome, dano, agilidade):
        super().__init__(nome, dano)
        self.agilidade = agilidade

    def atacar(self):
        print(f"{self.nome} ataca rapidamente causando {self.dano} de dano!")

    def esquivar(self):
        print(f"{self.nome} usa sua agilidade {self.agilidade} para tentar esquivar!")
