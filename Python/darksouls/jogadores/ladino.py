from Python.darksouls.jogadores.jogador import Jogador


class Ladino(Jogador):
    def __init__(self, nome: str, dano: int, agilidade: int):
        super().__init__(nome, dano)
        self.agilidade = agilidade

    def atacar(self, alvo, dano):
        dano_extra = self.agilidade // 2
        dano_total = dano + dano_extra
        print(f"{self.nome} ataca furtivamente e causa {dano_total} de dano em {alvo.nome}!")
        alvo.saude -= dano_total

    def defender(self, dano_recebido: int):
        esquiva = self.agilidade // 4
        dano_final = max(0, dano_recebido - esquiva)
        self.saude -= dano_final
        print(f"{self.nome} tenta esquivar e reduz {esquiva}. Sofre {dano_final}. Saúde: {self.saude}")
