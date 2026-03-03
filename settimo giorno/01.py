import pandas as pd

dati = {
    "nome": ["Ciccio", "anna", " Marcello", "Francesca","PAOLO"],
    "email": ["ciccio@email.it", " anna@email.com", "mercello@raveyard.com ", "francesca@email.com", "paolo@paolo.it"],
    "eta": [25, 22, 38, 20, 21],
    "stipendio": [1200, 1800, 1900, 2100, 1750],
    "citta": ["Roma", "Milano", "Firenze", "Roma", "Roma"],
    "categoria": ["A", "A", "B", "A", "B"],
    "vendite": [240, 250, 190, 310, 370]
}


df = pd.DataFrame(dati) #Questo DataFrame è come una tabella.
#print(df.isnull())      #Permette di vedere quali valori sono 'None'
#print(df.isnull().sum())
#print(df)               #Ogni colonna si chiama series, ed ogni riga ha un indice
#print(df.head())        #Ci dà informazioni sulle prime righe
#print(df.info())        #Ci da varie informazioni varie sui valori delle colonne
#print(df.describe())    #Ci dà statistiche rapide sui valori delle colonne numeriche
#print(df.dropna())      #Permette di togliere le righe che hanno dei NaN

#Pulizia nome
df["nome"] = df["nome"].str.strip().str.title() #Permette di gestire i problemi

#Pulizia email
df["email"] = df["email"].str.strip().str.lower()
df = df.dropna(subset=["email"])
df = df[df["email"].str.contains("@")]

#Pulizia stipendio.
media_stipendio = df["stipendio"].mean()
df["stipendio"] = df["stipendio"].fillna(media_stipendio)

#Pulizia età
df["eta"] = pd.to_numeric(df["eta"], errors="coerce") #Mi permette di sostituire valori che danno errore con NaN
df["eta"] = df["eta"].fillna(df["eta"].mean())  #Mi permette di sostituire le righe con NaN, usando la media,
                                                #Cosa che è convenzione giusta da seguire nel ML.
df["eta"] = df["eta"].astype("int") #Mi permette di convertire il dato da un tipo all'altro.
#print(df.info())

#Raggruppare vendite per città e categoria.
print(df.groupby(["categoria","citta"])["vendite"].sum())
print(df.groupby(["categoria","citta"])["vendite"].agg(["sum","count"])) #Per fare più aggregati insieme.


#df_filtrato = df[df["eta"] < 30] #Per filtrare i dati sull'età, e viene mantenuto l'indice.
