
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

