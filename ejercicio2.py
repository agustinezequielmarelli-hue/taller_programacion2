# hacer una funcion que tome como argumento un str y retorne el caracter que mas veces aparec
# y la cantidad de veces
# "hola!!!"   --> !, 3
# 

def max_caracter(frase: str) -> tuple:
    max_char = frase[0]       
    max_count = 0             
    for c in frase:           
        count = 0
        for d in frase:       
            if c == d:
                count += 1
        if count > max_count: 
            max_count = count
            max_char = c
    return max_char, max_count

    
print(max_caracter("yqwertyaya"))  


def maxi(frase:str):
    caracteres={}
    for caracter in frase:
        if caracter in caracteres:
            caracteres [caracter] +=1
        else:
            caracteres[caracter]=1
    print(caracteres)

    
