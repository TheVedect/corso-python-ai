class Validator:
    def validazione_richieste(self, richieste):
        richieste_valide = []
        for richiesta in richieste:
            if richiesta["nome"] == "" or richiesta["nome"] == " ":
                continue
            if richiesta["email"].count("@") != 1:
                continue
            try:
                eta = int(richiesta["eta"])
                if eta < 18:
                    continue
            except TypeError:
                continue
            except ValueError:
                continue
            richieste_valide.append(richiesta)
        return richieste_valide

    def sanificazione_richieste(self, richieste):
        richieste_sanificate = []
        for richiesta in richieste:
            richiesta["nome"] = " ".join(richiesta["nome"].split())
            richiesta["email"] = richiesta["email"].strip().lower()
            richieste_sanificate.append(richiesta)
        return richieste_sanificate

    def aggiungi_seniority(self, richieste):
        for richiesta in richieste:
            if int(richiesta["eta"]) < 25:
                richiesta["seniority"] = "Junior"
            elif int(richiesta["eta"]) < 40:
                richiesta["seniority"] = "Adult"
            else:
                richiesta["seniority"] = "Senior"
        return richieste