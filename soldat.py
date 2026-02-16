from personnage import Personnage
import random

class Soldat(Personnage):
    """Classe Soldat, enfant de Personnage."""

    def __init__(self, nom: str, vie: int, attaque: int, defense: int) -> None:
        super().__init__(nom, vie, attaque)
        self.defense = defense

    def attaquer(self) -> int:
        """Calcul les dégâts."""
        degats = self.attaque + random.randint(-5, 5) # pas vraiment d'instructions alors...
        return degats

    def subir_degat(self, degat: int) -> None:
        """polymorphisme de subir_degat."""
        degat_final = degat - self.defense
        if degat_final < 0:
            degat_final = 0
        self.vie -= degat_final *0.9 # 10% moins de degats


    def __str__(self) -> str:
        return f"Soldat({self.nom}, vie={self.vie}, attaque={self.attaque}, defense={self.defense})"

