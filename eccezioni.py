#Usarlo sempre quando può fallire, mai al posto di if else
try:
    numero_1 = int(input("Inserire un numero: "))
    numero_2 = int(input("Inserire un altro numero: "))
    print("Risultato:", numero_1 / numero_2)
except ValueError:
    print("Errore, il numero non è il numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero!")
else:
    print("Operazione eseguita con successo!")
finally:
    print("Qualsiasi cosa succeda, io vengo eseguito!")