#Esempio fittizzio del funzionamento RAG
documenti = [
    "Il sistema accetta pagamenti con carta",
    "Il sistema permette il login con SPID",
    "Il servizio è attivo 24 ore su 24"
]

def embedding_testuale (testo):
    return len(testo)

def ricerca_similarita(domanda, documenti):
    valore_domanda = embedding_testuale(domanda)
    migliore = None
    distanza_minima = float('inf')
    for doc in documenti:
        distanza = abs(valore_domanda - embedding_testuale(doc))
        if distanza < distanza_minima:
            distanza_minima = distanza
            migliore = doc
    return migliore

domanda = "Come posso pagare con la carta, per favore?"
contesto = ricerca_similarita(domanda, documenti)
print(domanda)
print(contesto)