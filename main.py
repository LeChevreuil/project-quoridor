import quoridor
import api

# Point d'entree
quoridor.analyser_commande()

DEBUG = {
    "joueurs":  [
        {"nom": "IDUL", "murs": 7, "pos": [5,5]},
        {"nom": "automate", "murs": 3, "pos": [8,6]}
    ],
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
        "verticaux": [[6,2], [4,4],[2,6],[7,5],[7,7]]
    }
}

PARTIE = [
        {
            "id": "5559cafd-6966-4465-af6f-67a784016b41",
            "date": "2022-09-23 11:58:20",
            "joueurs": ["IDUL", "automate"],
            "gagnant": None
        },
        {
            "id": "80a0a0d2-059d-4539-9d53-78b3f6045943",
            "date": "2022-09-24 14:23:59",
            "joueurs": ["IDUL", "automate"],
            "gagnant": "automate"
        }
]

#print(quoridor.formater_jeu(DEBUG))
#print(quoridor.formater_les_parties(PARTIE))

print(api.lister_parties())