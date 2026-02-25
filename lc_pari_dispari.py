numeri = [5, 12, 7, 20, 3, 18]

#Creare una lista che divida per 2 i numeri maggiori di 10 e lasci invariati gli altri

divisore = 2
numero_soglia = 10

trasformati = [numero / 2 if numero > numero_soglia else numero for numero in numeri]
print(trasformati)