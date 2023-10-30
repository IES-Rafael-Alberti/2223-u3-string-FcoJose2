'''Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.'''

def leerReversa(cadena:str) -> list:
    lista = []
    indice = 0
    '''Esto invierte la cadena'''
    cadena = cadena[::-1]
    while indice < len(cadena):
        letra = cadena[indice]
        lista.append(letra)
        indice = indice + 1
    return lista



if __name__ == "__main__":
    #Entrada
    cadena = input("Introduce una cadena de texto: ")
    #Proceso
    letras = leerReversa(cadena)
    #Salida
    print(letras)