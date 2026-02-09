from personnage import Personnage
import random


class Archer(Personnage):
    """Classe Archer, hérite de Personnage."""

    def __init__(self, nom: str, vie: int, attaque: int, dexterite: int) -> None:
        super().__init__(nom, vie, attaque)
        self.dexterite = dexterite

    @property
    def dexterite(self) -> int:

        return self._dexterite

    @dexterite.setter
    def dexterite(self, nouvelle_dexterite: int) -> None:
        if nouvelle_dexterite < 40:
            self._dexterite = 40
        elif nouvelle_dexterite > 70:
            self._dexterite = 70
        else:
            self._dexterite = nouvelle_dexterite

    def attaquer(self) -> int:
        """Calcule les dégâts (crit selon dexté)."""
        degats = self.attaque + 15
        nombre = random.randint(0, 100)

        # crit si nombre < dext
        if nombre < self.dexterite:
            degats *= 2
        return degats

    def __str__(self) -> str:
        return f"Archer({self.nom}, vie={self.vie}, attaque={self.attaque}, dexterite={self.dexterite})"

