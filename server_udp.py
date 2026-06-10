import socket
from datetime import datetime
ip_server = "127.0.0.1"

port_server=5001

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as soc:
    soc.bind((ip_server,port_server))
    #lo ponemos a escuchar las conexiones en el puerto
    
    while True:
        

        datos,addr=soc.recvfrom(1024)
        
        print("datos recibidos", datos.decode())
        fecha_hora= datetime.now().strftime("%H:%M:%Y")
        soc.sendto(fecha_hora.encode(), addr)




