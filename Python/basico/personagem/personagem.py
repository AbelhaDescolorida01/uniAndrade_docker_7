class PersonagemGame:
    def __init__(self, nome, classe, pontos_magia, pontos_vida):
        self.nome = nome
        self.classe = classe
        self.pontos_magia = pontos_magia
        self.pontos_vida = pontos_vida
        self.inventario = [] 

    def mostrar_status(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Pontos de Magia: {self.pontos_magia}")
        print(f"Pontos de Vida: {self.pontos_vida}")
        print(f"Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}")

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{item} adicionado ao inventário de {self.nome}.")


personagem1 = PersonagemGame("Arthas", "Paladino", 80, 150)
personagem2 = PersonagemGame("Morgana", "Feiticeira", 200, 90)


personagem1.adicionar_item("Espada Sagrada")
personagem1.adicionar_item("Poção de Vida")

personagem2.adicionar_item("Cajado Místico")
personagem2.adicionar_item("Poção de Magia")


print("\n Personagem 1 ")
personagem1.mostrar_status()

print("\n Personagem 2 ")
personagem2.mostrar_status()
