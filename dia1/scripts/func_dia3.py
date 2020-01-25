def factorial(valor=0):
    fact = 1
    while valor > 0:
        fact *= valor
        valor -= 1
    return fact


def fibo(x0=0, x1=1, max=100):
    x = x0 + x1
    # print(x)

    if x > max:
        return x
    else:
        return fibo(x1, x, max)


def parFibo(x0=0, x1=1, max=100, suma=0):
    x = x0 + x1
    par = x % 2

    if x > max:
        return x1
    else:
        if par == 0:
            suma += x
        return parFibo(x1, x, max, suma), suma

