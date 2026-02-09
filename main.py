
from guerrier import Guerrier
from mage import Mage
from archer import Archer
from arene import Arene


arene = Arene()


def ajouter_personnage() -> None:
    """Ajoute un personnage"""
    print("\nQuel type de personnage ?")
    print("1. Guerrier")
    print("2. Mage")
    print("3. Archer")
    choix = input("choix (1, 2 ou 3): ")

    # vérif choix valide
    if choix not in ["1", "2", "3"]:
        print("vous devez choisir 1, 2 ou 3")
        return


    # évite de planter catch les str.
    try:
        nom = input("Nom : ")
        vie = int(input("Vie (0-500) : "))
        attaque = int(input("Attaque (0-50) : "))

        # créer le bon type de perso
        if choix == "1":
            force = int(input("Force (1-50) : "))
            personnage = Guerrier(nom, vie, attaque, force)
        elif choix == "2":
            mana = int(input("Mana (0-100) : "))
            personnage = Mage(nom, vie, attaque, mana)
        else:  # choix 3
            dexterite = int(input("Dextérité (40-70) :"))
            personnage = Archer(nom, vie, attaque, dexterite)
    except ValueError:
        print("entrée invalide, réessayez")
        return

    arene.ajouter_personnage(personnage)
    print(f"{nom} a été ajouté à l'arène")


def voir_personnages() -> None:
    """Affiche les personnages de l'arène."""
    arene.afficher_personnages()


def combattre() -> None:
    """Lance un combat entre 2 personnages."""
    # vérif nb min de persos
    if arene.nombre_personnages() < 2:
        print("il faut au moins 2 personnages dans l'arène")
        return

    voir_personnages()
    try:
        choix1 = int(input("Choisir le premier combattant (numéro) : ")) - 1
        choix2 = int(input("Choisir le deuxième combattant (numéro) : ")) - 1
    except ValueError:
        print("entrée invalide, réessayez")
        return

    # vérif choix
    if choix1 == choix2 or not (0 <= choix1 < arene.nombre_personnages()) or not (0 <= choix2 < arene.nombre_personnages()):
        print("choix non valide, vous devez ")
        return

    arene.combattre(choix1, choix2)


def afficher_historique() -> None:
    """Affiche l'historique des combats"""
    arene.afficher_historique()


def menu() -> None:
    """Boucle principale du menu."""
    continuer = True
    while continuer:
        print("1. Ajouter un personnage")
        print("2. Voir les personnages dans l'arène")
        print("3. Faire combattre deux personnages")
        print("4. Voir l'historique des combats")
        print("5. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_personnage()
        elif choix == "2":
            voir_personnages()
        elif choix == "3":
            combattre()
        elif choix == "4":
            afficher_historique()
        elif choix == "5":
            print("au revoir")
            continuer = False
        else:
            print("choix invalide, réessayez")


menu()