MAX_PENDINDING_CONN=5
dir_paht=r"C:\Users\Agustin\OneDrive\Escritorio\taller_programacion2"

import os
import socket
import json
severport = 5001
ip_server = "0.0.0.0"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    #asociar un ip y el puerto
    conn.bind((ip_server,severport))
    #lo ponemos a escuchar las conexiones en el puerto
    conn.listen(MAX_PENDINDING_CONN)
    print(f"escuchando conexiones en el puerto: {severport}")

    while True:
        clien_conn, addr = conn.accept()
        print(f"se conecto: {addr} ")

        #nombre_archivo=clien_conn.recv(1024).decode()
        archivos=os.listdir(dir_paht)
        print("archivos, ", archivos)
        obj= json.dumps(archivos)
        clien_conn.sendall(obj.encode())
        nombre_archivo=clien_conn.recv(1024).decode()

        print("buscando archivo")
        archivo=f"{dir_paht}/{nombre_archivo}"
        print=("transfiriendo datos")
        with open(archivo,"rb") as file:
            
            
           while True:
                datos = file.read(1024)
                if not datos:
                    break
                clien_conn.sendall(datos)

        clien_conn.close()    

