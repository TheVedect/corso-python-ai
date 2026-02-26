import json
prompt = f""""
Genera la descrizione di questo utente:
Si chiama Ciccio ed ha 28 anni
"""
with open("utente.json", "r") as f:
    u = json.load(f)

def vincenzo_gpt(prompt, context):
    risposta = "Ciao, ecco la tua descrizione: \n"
    descrizione = f"L'utente di chiama {context['nome']} e ha {context['eta']} anni"
    return risposta + descrizione

print(vincenzo_gpt(prompt, u))