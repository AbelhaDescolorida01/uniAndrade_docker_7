from jogadores.cavaleiro import Cavaleiro
from itens.arma import Arma
from itens.pocao import Pocao
from inimigos.chefe import Chefe
from inimigos.mago import MagoSombrio
from inimigos.cacador import CacadorCorrompido
from npcs.ferreiro import Ferreiro

def main():
    print("=== Dark Souls RPG ===")

    jogador = Cavaleiro("Arthur", 100, armadura=5, resistencia=10)
    espada = Arma("Espada Longa", 15, 10)
    pocao = Pocao("Poção de Cura", 25)

    inimigo1 = Chefe("Senhor das Cinzas", 25)
    inimigo2 = MortoVivo("Zumbi", 10, podridao=8, velocidade=3)
    inimigo3 = MagoSombrio("Feiticeiro das Sombras", 20, mana=30)
    inimigo4 = CacadorCorrompido("Caçador Corrompido", 18, agilidade=7)

    ferreiro = Ferreiro("Posso forjar algo para você?", amizade=5, inventario=[], metal="Aço")

    while True:
        print("\n1 - Atacar inimigo")
        print("2 - Usar arma")
        print("3 - Usar poção")
        print("4 - Conversar com o ferreiro")
        print("5 - Sair")

        escolha = input("Escolha uma ação: ")

        if escolha == "1":
            inimigo = input("Escolha o inimigo: 1 - Chefe | 2 - Morto-vivo | 3 - Mago Sombrio | 4 - Caçador Corrompido: ")

            if inimigo == "1":
                inimigo1.atacar()
                jogador.defender(inimigo1.dano)
            elif inimigo == "2":
                inimigo2.morder()
                jogador.defender(inimigo2.dano)
            elif inimigo == "3":
                inimigo3.atacar()
                jogador.defender(inimigo3.dano)
            elif inimigo == "4":
                inimigo4.atacar()
                jogador.defender(inimigo4.dano)
            else:
                print("Inimigo inválido.")

        elif escolha == "2":
            espada.usar()

        elif escolha == "3":
            pocao.usar()

        elif escolha == "4":
            ferreiro.falar()
            ferreiro.vender_item()

        elif escolha == "5":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
