from Python.darksouls.jogadores.jogador import Jogador


class Escudeiro(Jogador):
    def __init__(self, nome: str, dano: int, escudo: int):
        super().__init__(nome, dano)
        self.escudo = escudo

    def atacar(self, alvo, dano):
        print(f"{self.nome} ataca com sua lança e causa {dano}")
        alvo.saude -= dano

    def defender(self, dano_recebido: int):
        bloqueio = self.escudo
        dano_final = max(0, dano_recebido - bloqueio)
        self.saude -= dano_final
        print(f"{self.nome} usa o escudo e bloqueia {bloqueio}. Sofre {dano_final}. Saúde: {self.saude}")
