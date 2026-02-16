class Armure:
    def __init__(self, nom, defense):
        self.nom = nom
        self._defense = defense


    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, nouvelle_defense):
        if nouvelle_defense < 0:
            self._defense = 0
        elif nouvelle_defense > 15:
            self._defense = 15
        else:
            self._defense = nouvelle_defense


    def __str__(self):
        return f"Armure: {self.nom}, Défense: {self.defense}"

