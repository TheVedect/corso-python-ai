import csv
prodotti = [
    {"id": 1, "nome": "PC", "prezzo": 999.0},
    {"id": 2, "nome": "Monitor", "prezzo": 699.0},
    {"id": 3, "nome": "Mouse", "prezzo": 99.0},
    {"id": 4, "nome": "Tastiera", "prezzo": 129.0},
]

with open("prodotti.txt", "w") as f:
    colonne = prodotti[0].keys()
    writer = csv.DictWriter(f, fieldnames=colonne)
    writer.writeheader()
    for row in prodotti:
        writer.writerow(row)