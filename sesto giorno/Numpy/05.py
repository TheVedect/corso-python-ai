import numpy as np
np.set_printoptions(linewidth=200)
#Creare un modello bancario per sapere se un prestito ad una persona può essere concesso.

np.random.seed(42)

#Età, reddito annuo, numero debiti, prestigio crediti, approvazione
dataset = np.array([
    [25, 30000, 2, 650, 1],
    [45, 80000, 1, 720, 1],
    [35, 50000, 5, 580, 0],
    [23, 25000, 3, 600, 0],
    [52, 120000, 0, 800, 1],
    [40, 70000, 4, 610, 0]
])

X = dataset[:, 0:-1] #Mi prendo tutte le colonne tranne l'ultima, e tutte le righe. Sono le features.
y = dataset[:, -1] #Mi prendo solo l'ultima colonna, e tutte le righe. Questo è il dato.

minimo = np.min(X, axis=0)
massimo = np.max(X, axis=0)

X_norm = (X - minimo) / (massimo - minimo) #Già qui l'AI può capire meglio i parametri.
print(X_norm)

#Ora tocca fare feature engineering: creare variabile affinché il modello possa capire
#Qui devo essere bravo io

reddito = X[:, 1]
debito = X[:, 2]
rapporto_debiti = debito / reddito #So che questo "può" andare bene

#In questo dataset può ad esempio capire che più questa variabile è 0 e più ha probabilità di
#avere il finanziamento, ma non è ancora finita, dunque aggiungo un'altra cosa.
rapporto_debiti = rapporto_debiti.reshape(-1,1)
print(rapporto_debiti)
X_enhanced = np.hstack((X_norm, rapporto_debiti))
print(X_enhanced)
indeces = np.arange(len(X_enhanced))
np.random.shuffle(indeces)

#Ora devo decidere quanti elementi vanno in allenamento per l'IA, in questo caso 80%.
#Il restante va in test.

train_size = int(len(X_enhanced) * 0.8)
train_idx = indeces[:train_size]
test_idx = indeces[train_size:]

X_train = X_enhanced[train_idx]
X_test = X_enhanced[test_idx]

y_train = y[train_idx]
y_test = y[test_idx]

print(y_train)
#Ora dovrei passare questi dati all'interno di un modello di Machine Learning e farlo allenare su x_test.
#Se ottengo y_test, allora va bene ed eventualmente posso usarlo, altrimente serve di più.