from personnage import Personnage
import random


class Guerrier(Personnage):
    """Classe Guerrier, enfant de Personnage."""

    def __init__(self, nom: str, vie: int, attaque: int, force: int) -> None:
        super().__init__(nom, vie, attaque)
        self.force = force

    @property
    def force(self) -> int:
        return self._force

    @force.setter
    def force(self, nouvelle_force: int) -> None:
        if nouvelle_force < 1:
            self._force = 1
        elif nouvelle_force > 50:
            self._force = 50
        else:
            self._force = nouvelle_force

    def attaquer(self) -> int:
        """Calcul les dégâts."""
        degats = self.attaque + (self.force // 2) + random.randint(-2, 2)
        return degats

    def __str__(self) -> str:
        return f"Guerrier({self.nom}, vie={self.vie}, attaque={self.attaque}, force={self.force})"
