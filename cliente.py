import sys
import socket
server_ip= "127.0.0.1"
server_port= 5001
#data
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
    soc.connect((server_ip,server_port))
    soc.sendall("hola server".encode())

    datos = soc.recv(1024)
    print(f"datos:, {datos.decode()}")