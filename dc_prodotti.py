prodotti = [
    {"id": 1, "nome": "PC", "prezzo": 999.0},
    {"id": 2, "nome": "Monitor", "prezzo": 699.0},
    {"id": 3, "nome": "Mouse", "prezzo": 99.0},
    {"id": 4, "nome": "Tastiera", "prezzo": 129.0},
]

indice = {p["id"]: p for p in prodotti}
print(indice)