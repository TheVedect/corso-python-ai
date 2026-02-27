class Libro:
    def __init__(self, titolo, autore, numero_pagine, descrizione):
        self.titolo = titolo
        self.autore = autore
        self.numero_pagine = numero_pagine
        self.descrizione = descrizione

    def presentazione(self):
        print(f"{self.titolo} è un libro scritto da {self.autore}, che ha {self.numero_pagine} pagine.")
        print(f"La sua descrizione è: '{self.descrizione}'")

descrizione = "Questo libro è incentrato sulla presenza del proprio genere opposto all'interno del proprio io."
libro1 = Libro("Il Sesso Opposto", "Camilla", 288, descrizione)
libro1.presentazione()