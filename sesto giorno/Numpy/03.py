import numpy as np
#Ogni dimensione aggiunge un contesto
x = 5 #Scalare
v = np.array([1,2,3,4,5]) #Vettore
m = np.array([ #Matrice
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
t = np.array([ #Tensore
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(t.shape)
a = np.array([1,2,3,4,5,6])
b = 10
c = a + b #Questo è broadcasting: permette di operare su dati di dimensione diversa intelligentemente.

a1 = np.array([
    [1,2,3],
    [4,5,6]
])
b1 = np.array([10, 20, 30])
c1 = a1 + b1 #Numpy va a confrontare le dimensioni da destra a sinistra
#Queste sono compatibili solo se uguali o se una delle due è 1.

d = np.array([1,2,3,4,5,6])
d1 = d.reshape(2,3) #Può essere fatto automaticamente con un -1 all'ultimo elemento.
print(d1)
e = d[0:2].copy() #copy() mi permette di non modificare l'array originale, poiché non crea referenze [view]