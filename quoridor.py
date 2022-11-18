import argparse

def analyser_commande():
    parser = argparse.ArgumentParser(description="Quoridor")

    parser.add_argument('idul', metavar='idul', type=str, help='IDUL du joueur')
    parser.add_argument("-p", "--parties", help="Lister les parties existantes")

    return parser.parse_args()

def formater_legende(joueurs):
    resultat = "Légende:\n"

    compte = 1
    for joueur in joueurs:
        murs = joueur["murs"]
        resultat += "   " + str(compte) + "=" + joueur["nom"] + ",\tmurs=" + ("|" * int(murs)) + "\n"
        compte += 1

    return resultat

def formater_damier(joueurs, murs):
    padding = 3
    lignes = ["   " + "-" * padding * 9]

    # construire le damier
    for y in range(9, 0, -1):
        temp = str(y) + " |"
        for x in range(1, 10):

            # verifier si c'est un joueur
            numJoueur = 1
            joueurPlace = False
            for joueur in joueurs:
                if x == joueur["pos"][0] and y == joueur["pos"][1]:
                    temp += " " + str(numJoueur) + " "
                    joueurPlace = True
                numJoueur += 1

            # sinon
            if not joueurPlace:
                temp += " . "    

        temp += "|" + "" 
        lignes.append(temp) 

        # verifier murs horizontaux
        ligne = "  |" + (" " * 3 * 9) + "|"

        lignes.append(ligne)

    resulat = "\n".join(lignes) + "\n"
    resulat += "--|" + "-" * padding * 9 + "\n"
    resulat += "  |"

    for i in range(1, 10):
        resulat += " " + str(i) + " "

    resulat += "\n"
    return resulat

def formater_jeu(etat_jeu):
    return formater_legende(etat_jeu["joueurs"]) + formater_damier(etat_jeu["joueurs"], etat_jeu["murs"])

def formater_les_parties(list_parties):
    ligne = []
    count = 1
    print(list_parties)
    for partie in list_parties:
        temp = str(count) + (" : " if count <= 9 else ": ") + partie["date"] + ", " + partie["joueurs"][0] + " vs " + partie["joueurs"][1]
        temp += ", gagnant: " + partie["gagnant"] if partie["gagnant"] is not None else ""
        ligne.append(temp)
        count += 1
    return "\n".join(ligne)


def recuperer_le_coup():
    print("Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV): ")
    type_coup = input()
    print("Donnez la position où appliquer ce coup (x,y): ")
    pos = input()
    