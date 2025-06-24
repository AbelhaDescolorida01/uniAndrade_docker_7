from .inimigo import Inimigo

class Mago(Inimigo):
    def __init__(self, nome, dano, mana):
        super().__init__(nome, dano)
        self.mana = mana

    def atacar(self):
        if self.mana >= 10:
            print(f"{self.nome} lança uma magia sombria causando {self.dano}")
            self.mana -= 10
        else:
            print(f"{self.nome} está sem mana e faz um ataque fraco causando {self.dano // 2}")

    def recuperar_mana(self):
        print(f"{self.nome} recupera 20 de mana!")
        self.mana += 20
