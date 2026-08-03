def isint(dato):
  for indice, caracter in enumerate(dato):
    if indice == 0 and (caracter == '-' or caracter == '+'):
      continue
    elif caracter.isnumeric():
      continue
    else:
      return False
  return True

print(isint("1234"))
print(isint("1234a"))
print(isint("-1234"))