import json

with open("utenti.json", "r") as f:
    dati = json.load(f)
    print(dati)

with open("utenti.json", "r") as f:
    utenti = json.load(f)

for u in utenti:
    eta = u["eta"] #JSON supporta il fatto che il numero sia tale e non una stringa da convertire
    if eta > 27:
        u["categoria"] = "Senior"
    else:
        u["categoria"] = "Junior"

with open("utenti_classificati.json", "w") as f:
    json.dump(utenti, f, indent=4)