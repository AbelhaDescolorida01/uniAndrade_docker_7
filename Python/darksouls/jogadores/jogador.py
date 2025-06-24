class Jogador:
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.saude = 100

    def atacar(self, alvo, dano: int):
        print(f"{self.nome} ataca causando {dano} de dano em {alvo.nome}!")
        alvo.saude -= dano

    def defender(self, dano_recebido: int):
        self.saude -= dano_recebido
        print(f"{self.nome} recebe {dano_recebido} de dano. Saúde atual: {self.saude}")
