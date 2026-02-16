from guerrier import Guerrier
import random


class Berserker(Guerrier):
    """Classe Berserker, hérite de Guerrier."""

    def __init__(self, nom: str, vie: int, attaque: int, force: int) -> None:
        """Init berserker."""
        super().__init__(nom, vie, attaque, force)

    def attaquer(self) -> int:
        """dégâts guerrier + vie perdue"""

        # Calcul de base
        degats_base = self.attaque + (self.force // 2) + random.randint(-2, 2)

        #ajouter le bonus bersek
        pv_perdus = self._vie_max - self.vie
        tranches_10pv = pv_perdus // 10
        bonus_berserker = tranches_10pv * 5

        degats_total = degats_base + bonus_berserker
        return degats_total

    def subir_degat(self, degat: int) -> None:
        """Calcul des dégâts (identique au guerrier parent).

        print "Le Berserker entre en FUREUR !!!!!!"""

        # Vérifier les pv
        etait_au_dessus_50 = self.vie > (self._vie_max * 0.5)

        # Appliquer les dégâts
        degat_final = degat - self.defense
        if degat_final < 0:
            degat_final = 0
        self.vie -= degat_final

        # revérifier pv
        est_en_dessous_50 = self.vie <= (self._vie_max * 0.5)

        # print petit message
        if etait_au_dessus_50 and est_en_dessous_50 and self.vie > 0:
            print(f"Le Berserker {self.nom} entre en FUREUR !")

    def __str__(self) -> str:
        return f"Berserker({self.nom}, vie={self.vie}, attaque={self.attaque}, force={self.force}, defense={self.defense})"

