from .item import Item

class Arma(Item):
    def __init__(self, nome, dano, resistencia):
        super().__init__(nome, "Arma")
        self.dano = dano
        self.resistencia = resistencia

    def usar(self):
        print(f"Atacando com {self.nome}, causando {self.dano} de dano.")