import ErroreCustom

def dividi(a, b):
    if b == 0:
        raise ZeroDivisionError("Scemo, stai dividendo per zero!")
    if b == 7:
        raise ErroreCustom
    return a / b

try:
    print(dividi(1, 0))
except (ZeroDivisionError, ValueError) as e:
    print(e)
except ErroreCustom:
    print("Non mi piace il 7: è la massima misura di ogni cosa!")