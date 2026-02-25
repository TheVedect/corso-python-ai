numeri = [1,2,3,4,5,6,7,8,9]

# [A if condizione else B for elemento in sequenza]

risultato = ["Pari" if numero % 2 == 0 else "Dispari" for numero in numeri]
print(risultato)