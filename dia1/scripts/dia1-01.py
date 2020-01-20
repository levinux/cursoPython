### Documentacion oficial: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# Diferentes maneras de declarar strings

"""Como documentacion:
    En lineas multiples... Esto se imprimira en HTML cuando se ejecute
    un comando especial que documenta este tipo de comentarios"""

x = """Cuando
    hay toda
    una historia que contar"""

y = "La manera clasica unilinea"
z = 'En comillas simples, que es exactamente igual que el anterior...'

print(x)
print(y)
print(z)

### Tambien se pueden hacer operaciones de multiplicacion y suma con strings!

x = "jaja" * 5
y = "mua" + x * 3
print(y)

### Encontrando a Nemo
resumen = """
La pelicula trata acerca de un pecesito llamado Nemo con una aleta deforme y cuya familia sufrio
una tragedia el dia en que el nacio. Aun asi es un pez muy valiente y quiere demostrarle su valor
a su preocupado padre
"""

print("Nemo" in resumen)

### Rebanadas e indices en strings
palindromo = "Anita lava la tina".upper()
print(palindromo[0:5])
print(palindromo[:10])
print(palindromo[11:])
print(palindromo[-4:])
