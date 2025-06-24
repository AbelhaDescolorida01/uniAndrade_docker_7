class Cavaleiro(Jogador):
    def __init__(self, nome: str, dano: int, armadura: int):
        super().__init__(nome, dano)
        self.armadura = armadura

    def atacar(self, alvo, dano):
        print(f"{self.nome} desfere golpe pesado e causa {dano}")
        alvo.saude -= dano

    def defender(self, dano_recebido: int):
        mitigacao = self.armadura
        dano_final = max(0, dano_recebido - mitigacao)
        self.saude -= dano_final
        print(f"{self.nome} usa armadura e mitiga {mitigacao}. Sofre {dano_final}. Saúde: {self.saude}")
