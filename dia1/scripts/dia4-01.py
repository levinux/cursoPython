print("El contenido de cancion.txt es:")
cancion = open("cancion.txt", "rt")
for linea in cancion:
    print(linea.strip())
cancion.close()

print("Escribiendo la otra parte de la cancion...")
estrofa = [
    "Mama, life is just began\n",
    "But now I've gone\n",
    "and thrown it all away\n"
]

cancion = open("cancion2.txt", "wt")
for linea in estrofa:
    cancion.write(linea)
cancion.close()
print("Listo! La estrofa esta en cancion2.txt")

