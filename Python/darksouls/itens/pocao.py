from .item import Item

class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, "Pocao")
        self.cura = cura

    def usar(self):
        print(f"Usando {self.nome}, curando {self.cura} de vida.")
