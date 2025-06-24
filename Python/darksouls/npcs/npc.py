class Npc:
    def __init__(self, dialogo, amizade):
        self.dialogo = dialogo
        self.amizade = amizade

    def falar(self):
        print(self.dialogo)