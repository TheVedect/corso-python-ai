import Richiesta
import Validator
import  Pipeline
import csv
import json



with open("requests.csv", "r") as csvfile:
    richieste = csv.DictReader(csvfile)
    validator = Validator.Validator()
    pipeline = Pipeline.Pipeline(validator,richieste)

    richieste_valide = pipeline.esegui()
    for richiesta in richieste_valide:
        print(richiesta)

with open('output.json', 'w') as outfile:
    statistiche = pipeline.crea_statistiche(richieste_valide)
    json.dump(statistiche, outfile, indent=4)