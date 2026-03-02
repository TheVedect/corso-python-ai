import numpy as np

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array = np.array(numeri)
nuovi = array * 2
print(nuovi)

numeri_random = np.random.randint(1,101, 10)
print(numeri_random)
media = np.mean(numeri_random)
maxx = np.max(numeri_random)
minn = np.min(numeri_random)
print(media)
print(maxx)
print(minn)

punteggi = np.array([23, 6, 43, 64, 245, 54, 66, 345, 33, 67])
media_punteggi = np.mean(punteggi)
sopra_media = punteggi > media_punteggi  #Maschera Booleana
numero_sopra_media = np.sum(sopra_media) #Così conto quanti voto sono sopra la media
percentuale = numero_sopra_media / len(sopra_media) * 100
min_punteggi = np.min(punteggi)
max_punteggi = np.max(punteggi)
normalizzati = (punteggi - min_punteggi) / (max_punteggi - min_punteggi)
print(type(punteggi))
print(type(media_punteggi))
print(type(sopra_media))
print(sopra_media)
print(percentuale)
print(normalizzati)
