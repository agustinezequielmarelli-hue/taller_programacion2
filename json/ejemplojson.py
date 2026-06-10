"""
json:viene de java script objet notation

"""
import json

"""
pythin ---->JSON
"""
print("datos python")
datos={ "nombre":"juan",
       "apellido":"ana",
       "edad":26,
       "altura":178,
       "estado": True,
       "activo": False,
       "notas": None,
       "cursos":["0",1],
       "atributos": {
           "a":0,
           "b":1,
       },
       "colores":("rojo","azul")
       }
print(datos)
print(f"type",type(datos))
datos_json=json.dumps(datos,indent=4)
print(f"datos json ")
print(datos_json)
print(f"type",type(datos_json))
"""
JSON----> PYTHON
"""
datos_python=json.loads(datos_json)
print(f"python devuelta {datos_python}")