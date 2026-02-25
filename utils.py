class ZeroExponentiationError(Exception):
    print("ZeroExponentiationError, idiota!")

def leggi_dati():
    print("leggi dati")


def pulisci_dati():
    print("pulisci dati")


def cancella_dati():
    print("cancella dati")


def salva_dati():
    print("salva dati")

def converti_in_maiuscolo(string):
    if not isinstance(string, str):
        raise TypeError("string")
    return string.upper()

def somma_numeri (numero1, numero2):
    if (not isinstance(numero1, int) and not isinstance(numero1, float)) or (not isinstance(numero2, int) and not isinstance(numero2, float)):
        raise TypeError("Devono essere entrambi numeri")
    return numero1 + numero2

def sottrazione_numeri (numero1, numero2):
    if (not isinstance(numero1, int) and not isinstance(numero1, float)) or (not isinstance(numero2, int) and not isinstance(numero2, float)):
        raise TypeError("Devono essere entrambi numeri")
    return numero1 - numero2

def prodotto_numeri (numero1, numero2):
    if (not isinstance(numero1, int) and not isinstance(numero1, float)) or (not isinstance(numero2, int) and not isinstance(numero2, float)):
        raise TypeError("Devono essere entrambi numeri")
    return numero1 * numero2

def divisione_numeri (numero1, numero2):
    if (not isinstance(numero1, int) and not isinstance(numero1, float)) or (not isinstance(numero2, int) and not isinstance(numero2, float)):
        raise TypeError("Devono essere entrambi numeri")
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        print("Hai diviso per 0")

def esponenziazione_numeri (numero1, numero2):
    if numero1 == 0 and numero2 == 0:
        raise ZeroExponentiationError("DAJE")
    return numero1 ** numero2