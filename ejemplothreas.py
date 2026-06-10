import socket
import threading
ip_server="localhost"

port_server= 5000
MAX_PENDING_CONN=10
def server_func(conn,addr):
    print(f"cliente: ", addr)
    while True:
        try:
            datos= conn.recv(1024).decode()
            print("data received:", datos)
            conn.send(f"eco: {datos}".encode())
        except:
            break
        conn.close()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as conn:
    conn.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    conn.bind((ip_server,port_server))
    conn.listen(MAX_PENDING_CONN)

    while True:
        client_con, addr= conn.accept()
        thread_conn= threading.Thread(target=server_func,args=(client_con,addr))
        thread_conn.daemon=True
        thread_conn.start()
