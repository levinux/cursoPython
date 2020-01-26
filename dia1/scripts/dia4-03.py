import json

### Archivos JSON
datos = {
    "nombre": "Levi Sandoval",
    "edad": 24,
    "comidas": ( "calzone", "pizza", "tocino", "malteadas", "cacahuates" )
}

print("'Dumpeando' en formato JSON:")
print(json.dumps(datos))

jsonfile = open("datos.js", "wt")
jsonfile.write("datos=" + json.dumps(datos) + "\n")
jsonfile.close()
print("Ahora abre el archivo 'datos.html' en tu navegador por favor")

