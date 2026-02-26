import csv
import csv_processing
import json

def purifica_dati(lista_dict, cosa_tornare = 1):
    primo = []
    secondo = []
    for dato in lista_dict:
        if dato["nome"] == "":
            secondo.append(dato)
            continue
        try:
            isinstance(int(dato["eta"]), int)
        except ValueError:
            secondo.append(dato)
            continue
        if dato["citta"] == "":
            secondo.append(dato)
            continue
        primo.append(dato)
    if cosa_tornare == 1:
        return primo
    else:
        return secondo

def aggiungi_seniority(lista_dict):
    for dato in lista_dict:
        if int(dato["eta"]) > 28:
            dato["seniority"] = "Senior"
        elif int(dato["eta"]) > 26:
            dato["seniority"] = "Mid"
        else:
            dato["seniority"] = "Junior"
    print(lista_dict)

with open("esercizio_dataset_csv_json.txt", "r") as f:
    reader = csv.DictReader(f)
    dati = []
    for row in reader:
        print(row)
        dati.append(row)
    print(dati)

    utenti_non_validi = purifica_dati(dati, 2)
    utenti_validi = purifica_dati(dati, 1)

    print(utenti_non_validi)
    print(utenti_validi)

aggiungi_seniority(utenti_validi)

with open("utenti_validi.csv", "w",newline='') as f:
    writer = csv.DictWriter(f, fieldnames=utenti_validi[0].keys())
    writer.writeheader()
    for dato in utenti_validi:
        writer.writerow(dato)

with open("utenti_non_validi.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=utenti_non_validi[0].keys())
    writer.writeheader()
    for dato in utenti_non_validi:
        writer.writerow(dato)

with open("utenti.json", "w") as f:
    json.dump(utenti_validi,f,indent=4)