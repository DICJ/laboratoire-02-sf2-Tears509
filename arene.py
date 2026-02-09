from details_combat import DetailsCombat
from personnage import Personnage


class Arene:
    """Gère les personnages et les combats."""

    def __init__(self) -> None:
        """Init l'arène avec listes vides."""
        self._personnages: list[Personnage] = []
        self._historique_combats: list[DetailsCombat] = []

    def ajouter_personnage(self, personnage: Personnage) -> None:
        """Ajoute un personagfe"""
        self._personnages.append(personnage)

    def afficher_personnages(self) -> None:
        """Affiche tous les personnages."""
        if not self._personnages:
            print("l'arène est vide")
            return
        print("personnages dans l'arène :")
        for i, p in enumerate(self._personnages, 1):
            print(f"  {i}. {p}")

    def get_personnage(self, index: int) -> Personnage:
        return self._personnages[index]

    def nombre_personnages(self) -> int:
        return len(self._personnages)

    def combattre(self, index1: int, index2: int) -> None:
        """ance un combat"""
        attaquant = self._personnages[index1]
        defenseur = self._personnages[index2]

        # créer les détails du combat
        details = DetailsCombat(attaquant.nom, defenseur.nom)

        print(f"combat : {attaquant.nom} VS {defenseur.nom}")

        while attaquant.vie > 0 and defenseur.vie > 0:
            # +1 nb tours
            details.incrementer_tour()

            # attaquant
            degats = attaquant.attaquer()
            defenseur.subir_degat(degats)
            print(f"{attaquant.nom} inflige {degats} dégâts {defenseur.nom}.")

            # vérif si défenseur vianvat
            if defenseur.vie <= 0:
                break

            # inverser roles et boucler
            attaquant, defenseur = defenseur, attaquant

        # détermine gagnant
        if attaquant.vie > 0:
            gagnant = attaquant
        else:
            gagnant = defenseur

        # add a l'historique
        details.definir_vainqueur(gagnant.nom)
        self._historique_combats.append(details)

        print(f"le vainqueur est {gagnant.nom}")

    def afficher_historique(self) -> None:
        """Affiche l'historique des combats."""
        if not self._historique_combats:
            print("aucun combat n'a encore eu lieu")
            return
        print("historique")
        for i, combat in enumerate(self._historique_combats, 1):
            print(f"  {i}. {combat}")
