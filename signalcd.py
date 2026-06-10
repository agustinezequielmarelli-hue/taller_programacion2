import signal
from time import sleep


def nuestro_handler(sig,frame):
    global contador
    contador=0
    print("sig",sig)
    print("saliendo...")
    nn=input("esta seguro que quiere salir: y/n ").upper()
    if nn =="Y":
        exit(1)

    
#registrar un handler para la señal ctrl-c
signal.signal(signal.SIGINT,nuestro_handler)
contador=0

while True:
    contador += 1
    print(f"procesando... {contador}")
    sleep(6)
