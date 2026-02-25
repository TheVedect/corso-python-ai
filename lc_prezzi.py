prezzi = [12.5, 9.9, 15.0, 7.5, 30.0]
#Crea una lista con i prezzi maggiori di 10
prezzo_soglia = 10
prezzi_alti = [prezzo for prezzo in prezzi if prezzo > prezzo_soglia]
print(prezzi_alti)