# LIST COMPREHENSION

numeri = [10, 20, 30]
#Aggiungere 5 ad ogni numero

nuovi = [numero + 5 for numero in numeri]
print(nuovi)

#filtrare con le list comprehension

numeri_2 = [1,2,3,4,5,6,7,8,9]

numeri_pari = [numero for numero in numeri_2 if numeri_2 % 2 == 0]
print(numeri_pari)

# filtraggio + trasformazione

numeri_pari_x_10 = [numero * 10 for numero in numeri_2 if numero % 2 == 0]
print(numeri_pari_x_10)