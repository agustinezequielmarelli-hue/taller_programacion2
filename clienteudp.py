import socket
import sys
ip_server = "127.0.0.1"

port_server=5001
datos = sys.argv[1]
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as soc:
    #mandamos al server
    soc.sendto(datos.encode(),(ip_server,port_server))
    #recibimos del server
    dato, dir =soc.recvfrom(1024)
    print(f"datos , {dato.decode()}")
    