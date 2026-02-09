class DetailsCombat:
    """Enregistre les infos du combat."""

    def __init__(self, nom_personnage_1: str, nom_personnage_2: str) -> None:
        """Initialise les détails avec les 2 combattants."""
        self.nom_personnage_1 = nom_personnage_1
        self.nom_personnage_2 = nom_personnage_2
        self.vainqueur = ""
        self.nombre_tours = 0

    def incrementer_tour(self) -> None:
        """Augmente le nb de tours de 1."""
        self.nombre_tours += 1

    def definir_vainqueur(self, nom_vainqueur: str) -> None:
        """Enregistre le nom du vainqueur."""
        self.vainqueur = nom_vainqueur

    def __str__(self) -> str:
        return (f"combat: {self.nom_personnage_1} VS {self.nom_personnage_2} | "
                f"vainqueur: {self.vainqueur} | tours: {self.nombre_tours}")
