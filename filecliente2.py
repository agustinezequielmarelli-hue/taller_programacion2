import socket
import json
serv_port=5001
serv_ip= "localhost"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.connect((serv_ip,serv_port))
    print("esperando datos")
    datos=conn.recv(1024)


    datos=datos.decode()
    print(datos)
    datos= json.loads(datos)
    for indice,archivo in enumerate(datos):

        print(f"{indice}.{archivo}")

    archivo_indice=int(input("ingrese el archivo a trasnferir {indice}"))
    print("archivos",datos )
    print("indice", archivo_indice)
    conn.sendall(archivo[archivo_indice].encode())

    with open(archivo[archivo_indice],"wb")as file:
        while True:
            files= conn.recv(1024)
            if not file:
                break
            file.write(files)

    print(f"archivo {archivo[archivo_indice]} transferido")