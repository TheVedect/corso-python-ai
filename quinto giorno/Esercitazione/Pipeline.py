class Pipeline:
    def __init__(self, validator, richieste):
        self._validator = validator
        self._richieste = richieste

    def esegui(self):
        richieste = self._validator.validazione_richieste(self._richieste)
        richieste = self._validator.sanificazione_richieste(richieste)
        #richieste = self._validator.aggiungi_seniority(richieste)
        return richieste