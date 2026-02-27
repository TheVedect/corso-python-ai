l = open("dati.txt", "r")

print(l.read())
l.close()

with open("dati.txt", "r") as f: # Meglio questa modalità, che chiude automaticamente f
    contenuto = f.readlines()    # E mi consente di vedere il contenuto senza che rimanga aperto

for line in contenuto:
    print(line)

with open("dati.txt", "a") as f:
    f.write("\nPippo")

with open("dati.txt", "r") as f: #Se voglio pulire dei nomi sporchi [Poi li salvo in un file nuovo]
    nomi_puliti = [r.strip().title().replace("\n", "") for r in f.readlines()]

"""
r -> lettura
w -> scrittura e sovrascrittura
a -> append
r+ -> lettura e scrittura
"""