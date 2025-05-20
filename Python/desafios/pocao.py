class Personagem:
    def __init__(self, nome: str):
        self.nome = nome
        self.saude = 10
        self.vivo = True

    def usar_pocao(self, pocao):
        if not self.vivo:
            print(f'{self.nome} já está morto e não pode usar poções.')
            return

        print(f'{self.nome} usou a poção: {pocao.tipo}')

        if isinstance(pocao, PocaoRoxa):
            self.saude += pocao.potencia  # potência negativa
            if self.saude <= 0:
                self.saude = 0
                self.vivo = False
                print(f'{self.nome} foi envenenado e morreu.')
            else:
                print(f'{self.nome} tem: {self.saude} pontos de vida')
        else:  # Poção de cura
            nova_saude = self.saude + pocao.potencia
            if nova_saude > 100:
                print(f'{self.nome} já está com a vida cheia.')
            else:
                self.saude = nova_saude
                print(f'{self.nome} tem: {self.saude} pontos de vida')


class PocaoVerde:
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo
        self.potencia = potencia


class PocaoRoxa:
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo
        self.potencia = -abs(potencia)  # garante que a potência é negativa


# Exemplo de uso
p1 = Personagem("Kratos")
pocao_verde = PocaoVerde("cura", 15)
pocao_roxa = PocaoRoxa("veneno", 15)

# Testes de poções
for _ in range(7):
    p1.usar_pocao(pocao_verde)

for _ in range(5):
    p1.usar_pocao(pocao_roxa)
