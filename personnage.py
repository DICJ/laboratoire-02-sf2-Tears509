class Personnage:
    """Classe de base pour tous les personnages."""

    def __init__(self, nom: str, vie: int, attaque: int) -> None:
        """Initialise classe personnage."""
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    @property
    def vie(self) -> int:
        return self._vie

    @vie.setter
    def vie(self, nouvelle_vie: int) -> None:
        if nouvelle_vie < 0:
            self._vie = 0
        elif nouvelle_vie > 500:
            self._vie = 500
        else:
            self._vie = nouvelle_vie

    @property
    def attaque(self) -> int:
        return self._attaque

    @attaque.setter
    def attaque(self, nouvelle_attaque: int) -> None:
        if nouvelle_attaque < 0:
            self._attaque = 0
        elif nouvelle_attaque > 50:
            self._attaque = 50
        else:
            self._attaque = nouvelle_attaque

    def subir_degat(self, degat: int) -> None:
        self.vie -= degat

    def __str__(self) -> str:
        return f"Personnage({self.nom}, vie={self.vie}, attaque={self.attaque})"
