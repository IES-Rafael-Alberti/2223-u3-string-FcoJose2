'''
Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano

y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.
'''

def contarBanana(letra):
    palabra = "banana"
    letras = palabra.count(letra)
    return letras


if __name__ == "__main__":
    #Entrada
    letra = input("Introduce una letra: ")
    #Proceso
    contador = contarBanana(letra)
    #Salida
    print(contador)
