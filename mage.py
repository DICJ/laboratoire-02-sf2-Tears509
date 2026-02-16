from personnage import Personnage
from armure import Armure
import random


class Mage(Personnage):
    """Mage hérite de Personnage."""
    """Mage enfant de Personnage."""

    def __init__(self, nom: str, vie: int, attaque: int, mana: int) -> None:
        super().__init__(nom, vie, attaque)
        defense = Armure("armure magique", 7).defense
        super().__init__(nom, vie, attaque, defense)
        self._mana_max = mana
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

    @property
    def mana_max(self) -> int:
        return self._mana_max

    @mana_max.setter
    def mana_max(self, nouveau_mana_max: int) -> None:
        if nouveau_mana_max < 0:
            self._mana_max = 0
        elif nouveau_mana_max > 100:
            self._mana_max = 100
        else:
            self._mana_max = nouveau_mana_max

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

    def reset(self) -> None:
        """Remet la vie et le mana du mage au maximum."""
        super().reset()  # remettre la vie
        self.mana = self._mana_max  # Remet le mana

    def __str__(self) -> str:
        return f"Mage({self.nom}, vie={self.vie}, attaque={self.attaque}, mana={self.mana}, defense={self.defense})"