from personnage import Personnage
import random


class Mage(Personnage):
    """Mage hérite de Personnage."""

    def __init__(self, nom: str, vie: int, attaque: int, mana: int) -> None:
        super().__init__(nom, vie, attaque)
        self.mana = mana

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, nouveau_mana: int) -> None:
        if nouveau_mana < 0:
            self._mana = 0
        elif nouveau_mana > 100:
            self._mana = 100
        else:
            self._mana = nouveau_mana

    def diminuer_mana(self) -> None:
        """retire random mana """
        self.mana -= random.randint(15, 25)

    def attaquer(self) -> int:
        """Calcule les dégâts (plus de dégâts si mana)."""
        if self.mana > 0:
            degats = self.attaque + 60
            self.diminuer_mana()
        else:
            degats = self.attaque
        return degats

    def __str__(self) -> str:
        return f"Mage({self.nom}, vie={self.vie}, attaque={self.attaque}, mana={self.mana})"