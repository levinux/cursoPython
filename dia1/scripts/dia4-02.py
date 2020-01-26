from func_dia4 import *

### Archivos CSV 
archivo = "nombres.csv"
naiveCsv(archivo)
betterCsv(archivo)

regs = [
    ["Levi", "36", "Hermosillo"],
    ["Jesus", "36", "Guadalajara"],
    ["Adrian", "37", "Agua Prieta"],
    ["Aristarco", "37", "Juchitan"]
]

naiveWriteCsv(regs)
betterWriteCsv(regs)

