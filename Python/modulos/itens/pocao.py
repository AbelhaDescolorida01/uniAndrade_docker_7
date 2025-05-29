class Poção:
    def _init_(self, nome):
        self.nome = nome
    
    def usar(self):
        print(f"usou poção: {self.nome}!")