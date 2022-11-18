import requests

URL = "https://pax.ulaval.ca/quoridor/api/v2/"

def lister_parties():
    res = requests.get(URL + "parties", auth=("VIBER138", "3beef511-3eb3-40bd-b170-bba3488d0c9b"))
    if res.status_code == 200:
        return res.json()
    else:
        print("[Erreur] Impossible to recuperer les parties")
        return {"parties": []}

def recuperer_partie(id_partie):
    res = requests.get(URL + "partie/" + id_partie, auth=("VIBER138", "3beef511-3eb3-40bd-b170-bba3488d0c9b"))
    if res.status_code == 200:
        return res.json()
    else:
        print("[Erreur] Impossible to recuperer la partie " + id_partie)
        return {"id": -1, "etat": None, "gagnant": None}

def debuter_partie():
    res = requests.post("partie", auth=("VIBER138", "3beef511-3eb3-40bd-b170-bba3488d0c9b"))

def jouer_coup():
    res = requests.put("jouer", auth=("VIBER138", "3beef511-3eb3-40bd-b170-bba3488d0c9b"))