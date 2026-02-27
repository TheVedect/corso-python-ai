import csv
dataset = []

with open("dati.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for riga in reader:
        dataset.append(riga)

print(dataset)

with open("dati.csv", "w", newline='') as csvfile: #Per creare un dataset mio
    colonne = ["nome", "eta", "citta"]
    writer = csv.DictWriter(csvfile, fieldnames=colonne)
    writer.writeheader()
    writer.writerow({
        "nome": "Mimmo",
        "eta": 22,
        "citta": "Roma"
    })