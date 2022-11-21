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

    
def jouer_coup(id_partie, type_coup, position, idul, secret):
    res = requests.put("jouer", auth=("VIBER138", "3beef511-3eb3-40bd-b170-bba3488d0c9b"), data={
        "id_partie": id_partie,
        "type_coup": type_coup,
        "position": position,
        "idul": idul,
        "secret": secret
    })

    if res.status_code == 200:
        data = res.json()
        if data["gagnant"] is None:
            raise StopIteration(data["gagnant"])
        else:
            return (id_partie, data)
    if res.status_code == 401:
        raise PermissionError(res.json())
    elif res.status_code == 406:
        raise RuntimeError(res.json())
    else:
        raise ConnectionError()