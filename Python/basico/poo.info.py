class Player: 
    host = "localhost:8080"

    def __init__(self, nome, arma):
        self.__nome = nome 
        self.__arma = arma 

    def get_nome(self):
        print(f"nome: {self.__nome}")

    def set_nome(self, nome):
        self.nome = nome


kratos = Player('kratos', 'laminas')
henry = Player('henry', 'espada')

kratos.set_nome("vivaldi")  
kratos.get_nome()           

