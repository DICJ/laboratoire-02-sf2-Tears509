class Personnage:
    """Classe de base pour tous les personnages."""

    def __init__(self, nom: str, vie: int, attaque: int, defense: int) -> None:
        """Initialise classe personnage."""
        self.nom = nom
        self._vie_max = vie
        self.vie = vie
        self.attaque = attaque
        self.defense = defense

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
    def vie_max(self) -> int:
        return self._vie_max

    @vie_max.setter
    def vie_max(self, nouvelle_vie_max: int) -> None:
        if nouvelle_vie_max < 0:
            self._vie_max = 0
        elif nouvelle_vie_max > 500:
            self._vie_max = 500
        else:
            self._vie_max = nouvelle_vie_max

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
        """Calcul degats avec defense."""
        degat_final = degat - self.defense
        if degat_final < 0:
            degat_final = 0
        self.vie -= degat_final

    def reset(self) -> None:
        """Remet la vie du personnage au maximum."""
        self.vie = self._vie_max

    def __str__(self) -> str:
        return f"Personnage({self.nom}, vie={self.vie}, attaque={self.attaque})"
