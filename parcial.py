
from dataclasses import dataclass,field,asdict
import csv
import json
import uuid
import os 
from datetime import datetime
categoria_validas=["motor","frenos","ruleman","semieje","homocinetica"]
inventario=[]
archivo_json='repuestos.json'

def iso_now()-> str:
     
    return datetime.now().isoformat()


@dataclass
class Repuestos:
    respuesto_id:str=field(default_factory=uuid.uuid4)
    nombre: str=""
    marca: str=""
    modelo_auto:str=""
    categoria: str=field(default_factory="motor")
    precio:float=field(default_factory=1)
    stock:int=field(default_factory=0)
    fecha_ingreso:  str = field(default_factory=iso_now)
    fecha_modificado:  str = field(default_factory=iso_now)


def cargar_json():
    global inventario
    if os.path.exists(archivo_json):
        with open(archivo_json,'r',encoding='utf-8') as archivo:
            data=json.load(archivo)
            inventario=[]
            for item in data:
                repuesto = Repuestos(
                    respuesto_id=item.get("respuesto_id",uuid.uuid4()),
                    nombre=item.get("nombre", ""),
                    marca=item.get("marca", ""),
                    modelo_auto=item.get("modelo_auto", ""),
                    categoria=item.get("categoria", "motor"),
                    precio=item.get("precio", 0.0),
                    stock=item.get("stock", 0),
                    fecha_ingreso=item.get("fecha_ingreso", iso_now()),
                    fecha_modificado=item.get("fecha_modificado", iso_now())
                )
                inventario.append(repuesto)
    else:
        inventario=[]
        guardar_json()


def guardar_json():
    try:
        data = []
        for r in inventario:
            d = asdict(r)
            d["respuesto_id"] = str(d["respuesto_id"])  
            data.append(d)
        with open(archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)
        print(f"Inventario guardado correctamente en {archivo_json}")
    except Exception as e:
        print("Error al guardar el inventario:", e)








def agregar_repuesto():
    print("ingreso a agregar un nuevo repuesto")

    try:
        
            
            nombre=input("Nombre del repuesto:").strip()
            
        
            marca=input("Marca del repuesto:").strip()
            modelo_auto=input("Modelo de coche:").strip()
            categoria = input(f"Categoría ({', '.join(categoria_validas)}): ").strip()
            precio=(input("Precio:"))
            stock=(input("stock:"))
            if not nombre or not marca or not categoria or not modelo_auto or not precio or not stock:
                print("Todos los campos son obligatorios.")
                return
            precio=float(precio)
            if precio<=0:
                print("el precio no puede ser 0 o un numero negativo")
            stock=int(stock)
            if stock <0:
                print("el stock no puede ser negativo")

             
            

            nuevo=Repuestos(nombre=nombre,marca=marca,modelo_auto=modelo_auto,categoria=categoria,precio=precio,stock=stock)
            inventario.append(nuevo)
            guardar_json()

    except ValueError:
        print("El precio y el stock del repuesto no puede ser letras")

def listar_repuestos():
    print("los repuestos cargados son :")
    if inventario==[]:
        print("el inventario esta vacio")
    else:
       mostrar_productos()
       
def buscar_repuestos():
    buscador=input("ingrese el nombre del repuesto o marca de este:").strip().lower()
    encontrado= False
    
    for item in inventario:
        if buscador in item.nombre.lower() or buscador in item.marca.lower():
            mostrar_productos()
            encontrado=True
    if encontrado==False:
        print("no existe ningun producto o marca con este nombre")
def actualizar_repuestos():
    repuesto_id=input("ingrese el repuesto a actualizar por id:").strip().lower()
    repuesto=buscar_por_id(repuesto_id)
    if repuesto:
        try:
            nuevoprecio=float(input("precio:"))
            nuevostock=int(input("stock:"))
            if nuevoprecio <=0 or nuevostock <0:
                print("el precio y/o el stock no pueden tener estos valores")
                return
            repuesto.precio=nuevoprecio
            repuesto.stock=nuevostock
            repuesto.fecha_modificado= iso_now()
            guardar_json()
            print(f"el repuesto {repuesto.nombre} fue actualizado exitosamente")

        except ValueError:
            print("el precio y el stock tienen que ser numeros")
    else:
        print("no se encontro un repuesto con este ID")    
            
def eliminar_repuesto():
    repuesto_id=input("ingrese el repuesto a eliminar por id:").strip().lower()
    repuesto=buscar_por_id(repuesto_id)
    if repuesto:
        inventario.remove(repuesto)
        guardar_json()
        print(f"Se elimino el repuesto: {repuesto.nombre}")
    else:
        print("no se encontro un repuesto con este id")


def buscar_por_id(id):
    
    for item in inventario:
        if str(item.respuesto_id).lower()==id:
            return item
    return None


def mostrar_productos():
    encabezado = f"{'ID':36} | {'Nombre':15} | {'Marca':10} | {'Modelo':10} | {'Categoría':12} | {'Precio':8} | {'Stock':5}"
    print(encabezado)
    print("-" * len(encabezado))

    
    for r in inventario:
        fila = f"{str(r.respuesto_id):36} | {r.nombre:15} | {r.marca:10} | {r.modelo_auto:10} | {r.categoria:12} | ${r.precio:<7.2f} | {r.stock:<5}"
        print(fila)

def exportar_csv():
    archivo_csv='repuesto.csv'
    with open(archivo_csv,'w',newline="",encoding='utf-8') as exportar:
        encabezados=csv.writer(exportar)
        encabezados.writerow(["id","nombre","marca","modelo auto","categoria","precio","Stock","fecha de ingreso","ultima modificacion"])
        for item in inventario:
            encabezados.writerow([
                str(item.respuesto_id),
                item.nombre,
                item.marca,
                item.modelo_auto,
                item.categoria,
                item.precio,
                item.stock,
                item.fecha_ingreso,
                item.fecha_modificado
            ])

if __name__== "__main__":
    cargar_json()
    abm_repuestos_init={'1':'nuevo repuesto','2':'listar repuestos','3':'buscar repuestos','4':'actualizar repuestos','5':'eliminar repuestos','7':'exportar a csv','9':'salir'}

   
    while True:
        print("\n=== ABM Repuestos ===")
        
        for key, value in abm_repuestos_init.items():
            print(f"{key}. {value}")

    
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            agregar_repuesto()
        elif opcion == '2':
            listar_repuestos()
        elif opcion == '3':
            buscar_repuestos()
        elif opcion == '4':
            actualizar_repuestos()
        elif opcion == '5':
            eliminar_repuesto()
        elif opcion == '7':
            exportar_csv()
        elif opcion == '9':
            guardar_json()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
