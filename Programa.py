def preguntarCharacter():
    character = input(" POR FAVOR INGRESAR EL VALOR A CAMBIAR \n :")
    return character
def preguntarPalabra():
    palabra = input(" POR FAVOR INGRESA LA PALABRA QUE DESEAS CAMBIAR \n :")
    return palabra
def resultadoPalabra ():
    palabra = preguntarPalabra()
    for resultadoCharacter in palabra:
        resultadoASCCI = ord(resultadoCharacter)
        resultadoBinario = bin(resultadoASCCI)[2:]
        print(f"El valor del character {resultadoCharacter} es {resultadoASCCI}. La representacion binaria de {resultadoCharacter} en un Byte es {resultadoBinario}")


def resultadoCharacter():
    character = preguntarCharacter()
    resultadoASCCI = ord(character)
    resultadoBinario = bin(resultadoASCCI)[2:]
    print(f"El valor del character {character} es {resultadoASCCI}. La representacion binaria de {character} en un Byte es {resultadoBinario}")


def menu ():
    menu = 0
    while menu != 3:
        menu = int(input("Menu \n ========================== \n1. Ingresar una Palabra \n2. Ingresar un Character \n3. Para salir del programa \n ========================== \n :"))
        if menu == 1:
            resultadoPalabra()
        elif menu == 2:
            resultadoCharacter()
    print ("MUCHAS GRACIAS POR USAR NUESTROS SERVICIOS")
menu()
