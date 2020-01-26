import csv

def naiveCsv(archivo):
    f = open(archivo, "rt")
    for linea in f:
        array = linea.split(",")
        print("Nombre: {}".format(array[2].strip('\n')))
        print("Apellido paterno: {}".format(array[0]))
        print("Apellido materno: {}".format(array[1]))
        print("=====================================\n")


def betterCsv(archivo):
    with open(archivo, "rt") as f:
        reader = csv.reader(f)
        for linea in reader:
            print("Nombre: {}".format(linea[2]))


def naiveWriteCsv(registros):
    f = open("registros1.csv", "wt")
    for registro in registros:
        f.write(",".join(registro) + '\n')
    f.close()
    print("naiveWriteCsv: Archivo csv generado!")


def betterWriteCsv(registros):
    with open("registros2.csv", "wt") as archivo:
        writer = csv.writer(archivo, delimiter='#')
        for registro in registros:
            writer.writerow(registro)
    print("betterWriteCsv: Archivo csv generado!")


# mocos

