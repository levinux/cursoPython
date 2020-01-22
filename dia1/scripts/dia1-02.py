# Declaracion de listas

milista = [ "mangos", "platanos", "fresas" ]
mi2lista = list([i for i in range(10)])

print(milista)
print(mi2lista)

# Operaciones de suma, multiplicacion
unos = [1] * 3
muchos = mi2lista + unos
print(unos)
print(muchos)

del muchos[0]
print(muchos)

del muchos
#print(muchos) ### ERROR!!!

numeros = [9, 1, 16, 84, 822, 4845, 438, 23734, 9345, 724372, 32852, 4578324, 4353, 8345, 8435, 345, 98734]
print(numeros[:5])
print(numeros[:-1])
print(numeros[2:15:3])
numeros[3:8] = [i for i in range(10000, 10006)]
print(numeros)
print("Total de elementos en 'numeros': " + str(len(numeros)))

### Diccionarios
mapa1 = dict(uno=1, dos=2, tres=3)
print(mapa1['dos'])
vacio = {}
vacio['id'] = 89
vacio['nombre'] = "Levi"
vacio['favoritos'] = ['tocino', 'mazapan', 'conchas', 'malteadas']
print(vacio)
