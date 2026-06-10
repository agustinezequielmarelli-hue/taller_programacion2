"""
dar de alta a un alumno
nombre
edad 
fecha y hora de creacion
guardar archivo en json
"""
from datetime import datetime
import json

alumno={"nombre":"agustin",
         "edad": 26,
         "fecha":datetime.now().isoformat(),
        }
print(alumno)
archivo_json=json.dumps(alumno)
fecha= datetime.fromisoformat(alumno["fecha"])
alumno["fecha"]=fecha

#with open(archivo_json,w)

class alumnos:
    def __init__(self):
        self.nombre=nombre
        self.edad=edad
        self.fecha= datetime.now()



    def to_json(self):
        self.fecha=self.fecha.strftime()
