import numpy as np

dati = np.array([ #eta, altezza, peso
    [34, 167, 89],
    [37, 185, 92],
    [22, 173, 65]
])

print(dati.shape)
print(dati[:, 0])
media_su_colonna = np.mean(dati, axis=0) #Media corretta da fare, sulle colonne
media_su_riga = np.mean(dati, axis=1) #Media che in questo contesto non ha senso, sulle righe
print(media_su_colonna)
print(media_su_riga)

studenti = np.array([
    [80, 79, 90],
    [60, 75, 90],
    [88, 93, 90],
    [55, 60, 70]
])

"""
Ogni riga è uno studente ed ogni colonna una materia.
Devo trovare media per studente, per materia, studenti con media > 75, e normalizzare i dati
"""

media_materie = np.mean(studenti, axis=0)
media_studenti = np.mean(studenti, axis=1)
mask_studenti = media_studenti > 75
studenti_bravi = studenti[mask_studenti] #Funziona solo se le dimensioni corrispondono
normalizzati = (studenti - np.min(studenti)) / (np.max(studenti) - np.min(studenti))
print(media_materie)
print(media_studenti)
print(mask_studenti)
print(studenti_bravi)
print(normalizzati)
