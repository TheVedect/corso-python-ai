class Pipeline:
    def __init__(self, validator, richieste):
        self._validator = validator
        self._richieste = richieste

    def esegui(self):
        richieste = self._validator.validazione_richieste(self._richieste)
        richieste = self._validator.sanificazione_richieste(richieste)
        richieste = self._validator.aggiungi_seniority(richieste)
        return richieste

    def crea_statistiche(self, richieste):
        totale_richieste = len(richieste)
        servizi = []
        for richiesta in richieste:
            servizi.append(richiesta["servizio"])
        servizi_unici = set(servizi)
        conteggio_servizi = {}
        for richiesta in richieste:
            servizio = richiesta["servizio"]
            if servizio not in conteggio_servizi:
                conteggio_servizi[servizio] = 0
            else:
                conteggio_servizi[servizio] += 1
        statistiche = {}
        statistiche["totale_richieste"] = totale_richieste
        statistiche["servizi"] = servizi
        statistiche["conteggio_servizi"] = conteggio_servizi
        statistiche["richieste"] = richieste
        return statistiche