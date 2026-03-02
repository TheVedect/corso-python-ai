import numpy as np

numeri = np.random.randint(1,101, 10)
media = np.mean(numeri)
mini = np.min(numeri)
maxi = np.max(numeri)

numeri3 = numeri * 3
mini3 = np.min(numeri3)
maxi3 = np.max(numeri3)

filtrati = numeri[numeri > 50]
print(filtrati)