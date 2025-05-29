class Arma:
    def _init_(self, nome):
        self.nome = nome
    
    def usar(self):
        print(f"usou arma: {self.nome}!")