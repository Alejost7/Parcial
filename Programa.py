def resultadoPalabra ():
  palabra = preguntarPalabra()
  for resultadoCharacter in palabra:
      resultadoASCCI = ord(resultadoCharacter)
      resultadoBinario = bin(resultadoASCCI)[2:]
      print(f"El valor del character {resultadoCharacter} es {resultadoASCCI}. La representacion binaria de {resultadoCharacter} en un Byte es {resultadoBinario}")