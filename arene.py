from details_combat import DetailsCombat
from personnage import Personnage


class Arene:
    """Gère les personnages et les combats."""

    def __init__(self) -> None:
        """Init l'arène avec listes vides."""
        """Init arène avec listes vides."""
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
        """lance un combat"""
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
            print("commence par combattre on verra apres pour l'historique...")
            return
        print("historique")
        for i, combat in enumerate(self._historique_combats, 1):
            print(f"  {i}. {combat}")
            print(f"{i}. {combat}")

    def soigner_personnage(self, index: int) -> None:
        """reset la vie du perso selon lindice."""
        if 0 <= index < len(self._personnages):
            personnage = self._personnages[index]
            personnage.reset()
            print(f"{personnage.nom} a été soigné")
        else:
            print("invalide.")

    def nettoyer_arene(self) -> None:
        """Supprime persos morts (vie <= 0)."""
        personnages_vivants = [p for p in self._personnages if p.vie > 0]
        nb_morts = len(self._personnages) - len(personnages_vivants)
        self._personnages = personnages_vivants
        print(f"{nb_morts} personnages morts ont été supprimés de l'arène.")

    def lancer_battle_royal(self) -> None:
        """combat un a un et retire ceux morts."""
        if len(self._personnages) < 2:
            print("Il faut au moins 2 personnages pour lancer un Battle Royal.")
            return

        print("\n=== BATTLE ROYAL ===")
        print(f"{len(self._personnages)} personnages entrent dans l'arène!")

        # Soigner tous les personnages avant de commencer
        print("\nSoins de tous les participants...")
        for personnage in self._personnages:
            personnage.reset()
        print("Tous les personnages sont prêts!\n")

        # Combats jusqu'à ce qu'il n'en reste qu'un
        while len(self._personnages) > 1:
            print(f"\n--- {len(self._personnages)} personnages restants ---")

            # Faire combattre les 2 premiers personnages
            attaquant = self._personnages[0]
            defenseur = self._personnages[1]

            # Créer les détails du combat
            details = DetailsCombat(attaquant.nom, defenseur.nom)
            print(f"\nCombat : {attaquant.nom} VS {defenseur.nom}")

            # Boucle de combat
            while attaquant.vie > 0 and defenseur.vie > 0:
                details.incrementer_tour()

                # Attaquant frappe
                degats = attaquant.attaquer()
                defenseur.subir_degat(degats)
                print(f"{attaquant.nom} inflige {degats} dégâts à {defenseur.nom} (vie: {defenseur.vie}).")

                # Vérifier si défenseur est mort
                if defenseur.vie <= 0:
                    break

                # Inverser les rôles
                attaquant, defenseur = defenseur, attaquant

            # Déterminer le gagnant et le perdant
            if attaquant.vie > 0:
                gagnant = attaquant
                perdant = defenseur
            else:
                gagnant = defenseur
                perdant = attaquant

            # Ajouter à l'historique
            details.definir_vainqueur(gagnant.nom)
            self._historique_combats.append(details)

            print(f"\n{gagnant.nom} remporte le combat!")

            # Soigner le survivant
            gagnant.reset()
            print(f"{gagnant.nom} est soigné pour le prochain combat.")

            # Supprimer le perdant de la liste
            self._personnages.remove(perdant)
            print(f"{perdant.nom} est éliminé du Battle Royal.")

        # Afficher le winner
        champion = self._personnages[0]
        print(f"{champion.nom} a gagne")


