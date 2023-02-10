def RunLength(strParam):
  resposta = ""
  cont = 1
  index = 1
  palavra = strParam + " "
  for letra in strParam:
    if(palavra[index] == letra):
      cont += 1
      index += 1
    else:
      resposta = resposta + (str(cont) + str(letra))
      cont = 1
      index += 1
  return resposta

# keep this function call here
print(RunLength("ttttttttttrrrrrrrxx"))
