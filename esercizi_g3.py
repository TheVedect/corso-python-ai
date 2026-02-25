class NoValidNumbersError(Exception):
    pass

def ottieni_stringhe():
    lista = []
    parametro = True
    while parametro:
        lista.append(input("Inserisci un numero: "))
        if lista[-1] == "":
            lista.pop()
            parametro = False
    return lista

def converti_stringhe_a_numeri(lista):
    stringhe_numeri = []
    for string in lista:
        try:
            numero = int(string)
            stringhe_numeri.append(numero)
            print(numero, "è un numero valido!")
        except ValueError:
            print(string, "non è un numero valido!")

    if len(stringhe_numeri) == 0:
        print("Non ci sono stringhe valide da convertire in numeri!")
        return
    else:
        return stringhe_numeri

def scegli_numeri_validi(lista_numeri, soglia = 10):
    numeri_validi = []
    for numero in lista_numeri:
        if numero > soglia:
            numeri_validi.append(numero)
    if len(numeri_validi) == 0:
        raise NoValidNumbersError("Non ci sono numeri validi oltre la sogliaaaa!")
    else:
        return numeri_validi

def somma_numeri(lista_numeri):
    somma =0
    if len(lista_numeri) == 0:
        raise NoValidNumbersError("Non ci sono numeri validi oltre la sogliaaaa!")
    for numero in lista_numeri:
        somma += numero
    print("La somma dei numeri è:",somma)
    return somma

print("Benvenuto alla pipeline per sommare i numeri.")
numeri = ottieni_stringhe()
numeri = converti_stringhe_a_numeri(numeri)
numeri = scegli_numeri_validi(numeri)
sommafinale = somma_numeri(numeri)