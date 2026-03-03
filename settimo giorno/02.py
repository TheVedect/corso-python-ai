import pandas as pd

dati = {
    "settore": ["Tech", "Retail", "Finance", "Tech", "Tech", "Retail", "Finance"],
    "dipendenti": [50, 70, 30, 90, 80, 75, 20],
    "fatturato": [50000, 60000, 33000, 120000, 90000, 85000, 18000],
}

df = pd.DataFrame(dati)

#Fatturato medio per settore
print(df.groupby("settore")["fatturato"].mean())
#Numero totale di dipendenti per settore
print(df.groupby("settore")["dipendenti"].sum())
#Settore con massimo fatturato totale
totali = df.groupby("settore")["fatturato"].sum()
print(totali.idxmax()) #Mi restituisce l'indice con il massimo valore.