import numpy as np

np.set_printoptions(linewidth=200) # Imposta il numero di caratteri per riga
#Simulo dataset Machine Learning
dataset = np.random.uniform(0,100,(5,4))
#Per finta, ogni riga è una persona, le colonne sono: età, altezza, peso e punteggio
print(dataset)
#Devo normalizzare solo le ultime 3 colonne, aggiungere una colonna con la media di queste.
#Devo poi fare una copia del dataset, per prevenire la modifica

dataset_originale = dataset.copy() #Lavoro sul dataset, non sulla copia
features_ds  = dataset[:, 1:] #Seleziono tutte le righe, ma solo le ultime 3 colonne
print(features_ds)

minimo = np.min(features_ds, axis=0)
massimo = np.max(features_ds, axis=0)
features_norm = (features_ds - minimo) / (massimo - minimo)
print(features_norm)
#Ora devo sostituire la normalizzazione al dataset
dataset[:, 1:] = features_norm #Ora non mi interessa, ma c'è stato il casting da float ad intero
print(dataset)                 #Perché dataset è un array di interi ed ndarray deve avere un solo tipo.

media_feature = np.mean(dataset[:, 1:], axis=1) #Creo le medie
media_feature = media_feature.reshape(-1,1)     #E ne modifico la forma per aggiungerle successivamente
print(media_feature)

dataset_con_media = np.hstack((dataset, media_feature)) #Aggiungo la colonna delle medie
print(dataset_con_media)