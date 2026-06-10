import socket
filename="archivo1.txt"
serv_port=5000
serv_ip= "localhost"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conn:
    conn.connect(serv_ip,serv_port)
    conn.sendall(filename.encode())

    with open(filename,"wb") as file:
        while True:
            datos= conn.recv(1024)
            if not datos:
                break        
            file.write(datos)



print(f"archivo {filename} transferido")