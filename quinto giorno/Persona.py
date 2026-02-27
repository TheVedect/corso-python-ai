class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}, ed ho {self.eta} anni!")

if __name__ == "__main__":
    p1 = Persona("Ciccio", 26)
    p2 = Persona("Francesca", 23)
    print(p1.saluta())
    print(p2.saluta())