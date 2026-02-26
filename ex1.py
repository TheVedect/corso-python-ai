import csv
from csv_processing import writer

dataset = []

with open("dati_ex1.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dataset.append(row)

with open("dati_ex1_nuovi.csv", "w", newline='') as f:
    nuovo_dataset = []
    for row in dataset:
        if int(row["eta"]) >= 27:
            row["categoria"] = "Senior"
        else:
            row["categoria"] = "Junior"
        nuovo_dataset.append(row)
    writer = csv.DictWriter(f, fieldnames= nuovo_dataset[0].keys())
    writer.writeheader()
    for row in nuovo_dataset:
        writer.writerow(row)