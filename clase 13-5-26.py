#servidor tcp

import socket
#local host
ip_server = "127.0.0.1"

port_server=5001

#crear socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
    #asociar un ip y el puerto
    soc.bind((ip_server,port_server))
    #lo ponemos a escuchar las conexiones en el puerto
    soc.listen()
    print(f"escuchando conexiones en el puerto: {port_server}")

    
    #se queda aca hasta que llega una conexion 
    while True:
        conn, addr= soc.accept() #bloqueante
        with conn:
            print(f"se conecto_ {addr}")
            while True:
                datos= conn.recv(1024)
                if not datos:
                    break

                print(f"datos recibidos :", {datos.decode()})
                #enviamos los datos
                conn.sendall(datos)


