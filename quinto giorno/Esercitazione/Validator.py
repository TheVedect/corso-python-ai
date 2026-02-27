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
                pass
            except ValueError:
                pass
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
        richieste_seniority = [
            "Junior" if int(richiesta["eta"]) < 25 else
            "Adult" if int(richiesta["eta"]) < 40 else "Senior"
            for richiesta in richieste
        ]
        return richieste_seniority