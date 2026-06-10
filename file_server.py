"""
1.listar archivos
2. transferir
"""
MAX_PENDINDING_CONN=5
dir_paht="/home/agustin/files"
import socket
import os
severport = 5000
ip_server = "0.0.0.0"

with socket.socket(socket.AF_INK_STREAM) as conn:
    #asociar un ip y el puerto
    conn.bind((ip_server,severport))
    #lo ponemos a escuchar las conexiones en el puerto
    conn.listen(MAX_PENDINDING_CONN)
    print(f"escuchando conexiones en el puerto: {severport}")

    while True:
        clien_conn, addr = conn.accept()
        print(f"se conecto: {addr} ")

        nombre_archivo=clien_conn.recv(1024).decode()
        

        print(f"nombre del archivo: {nombre_archivo}")
        archivo=f"{dir_paht}/{nombre_archivo}"
        with open(archivo,"rb") as file:
            
            
            while True:
                datos = file.read(1024)
                if not datos:
                    break
                clien_conn.sendall(datos)

        clien_conn.close()    

