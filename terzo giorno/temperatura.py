temperature = [18, 22, 30, 12, 15, 32, 27, 19, 28, 20]
# Creare una nuova lista con le temperature superiori a 20
temperature_alte = []
temp_soglia = 20

for temp in temperature:
    if temp > temp_soglia:
        temperature_alte.append(temp)
print(temperature_alte)