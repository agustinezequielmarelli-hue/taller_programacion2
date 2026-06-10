"""
json con archivos
"""
import json

with open("precios_surtidos.json","r") as archivo:
    datos=json.load(archivo)

print("cantidad de registros",len(datos))
print(datos[0])
