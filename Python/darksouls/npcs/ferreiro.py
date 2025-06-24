from .npc import Npc

class Ferreiro(Npc):
    def __init__(self, dialogo, amizade, inventario, metal):
        super().__init__(dialogo, amizade)
        self.inventario = inventario
        self.metal = metal

    def vender_item(self):
        print("O ferreiro vende itens.")
