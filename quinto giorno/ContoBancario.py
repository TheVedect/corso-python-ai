class ContoBancario:

    def __init__(self, saldo): #Un trattino basso avverte, ma due la nasconde proprio, all'esterno.
        self._saldo = saldo   #Questo accade se richiamo la variabile direttamente con gli underscore.

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo

    def preleva(self, importo):
        if 0 < importo <= self._saldo:
            self._saldo -= importo

    def mostra_saldo(self):
        return self._saldo

conto_di_ciccio = ContoBancario(10000)
conto_di_ciccio.deposita(100)
conto_di_ciccio.preleva(200)
print(conto_di_ciccio.mostra_saldo())