# Funciones!
def proc():
    print("Esto es un procedimiento")


def func(x):
    return x ** 2


def func(x=1, y=2):
    return x ** y


# --------------
proc()
print("func(8)={}".format(func(8)))
print("func()={}".format(func()))
print("func(y=8, x=2)={}".format(func(y=8, x=2)))
