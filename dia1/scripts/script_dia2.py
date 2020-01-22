def factorial(valor=0):
    fact = 1
    while valor > 0:
        fact *= valor
        valor -= 1
    return fact

raw = input("Dame un numero: ")
if raw.isnumeric():
    valor = int(raw)
    fact = factorial(valor)
    print("El factorial de {} es {}".format(raw, fact))
else:
    print("Que me des un numero... terminando...")
