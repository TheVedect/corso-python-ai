numeri = [5, 12, 26, 30, 20, 9, 14, 209]
#Creare una nuova lista solo con i numeri maggiori di 10 e divisi per 2
numero_soglia = 10
numero_divisore = 2

numeri_scelti_divisi = []

for numero in numeri:
    if numero > numero_soglia:
        numeri_scelti_divisi.append(numero / numero_divisore)

print(numeri_scelti_divisi)