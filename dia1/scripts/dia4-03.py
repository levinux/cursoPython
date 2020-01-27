import json

### Archivos JSON
datos = {
    "nombre": "Levi Ismael Sandoval Medina",
    "edad": 24,
    "comidas": ( "calzone", "pizza", "tocino", "malteadas", "cacahuates","almendras" )
}

print("'Dumpeando' en formato JSON a datos.js")
jsonfile = open("datos.js", "wt")
jsonfile.write("datos=" + json.dumps(datos) + "\n")
jsonfile.close()
print("Ahora abre el archivo 'datos.html' en tu navegador por favor")

