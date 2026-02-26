numeri = [3,6,9,12,15,18,21,24,27,30]

#Creare un dizionario con chiave numero e valore il numero diviso per 3

nomi = ["Anna", "Ciccio", "Francesca", "Annibale"]

#Creare un dizionario con chiave nome e valore "Lungoo" o "Corto" a seconda se il nome ha più o meno di 5 caratteri
lunghezza_minima = 5
tabellina_del_3 = {numero: numero / 3 for numero in numeri}
print(tabellina_del_3)
lunghezza_nomi = {n: "Lungo" if len(nomi) > lunghezza_minima else "Corto" for n in nomi}
print(lunghezza_nomi)

