# Hacer una funcion que tome como argumento una lista de numeros y retorne el menor valor de la lista.


def menor(numeros: list)-> int:
	menorvalor=numeros[0]
	for n in numeros:
		if n < menorvalor:
			menorvalor=n
	
	return menorvalor



lista = [5, 7, 8, 9, 4]

resultado = menor(lista)

print("menor: ", resultado)
