class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def usar(self):
        print(f"Usando {self.nome}")