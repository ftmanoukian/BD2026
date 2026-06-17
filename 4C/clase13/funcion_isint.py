#La función isint tiene que devolver True si 'valor' se puede
# convertir a int, y False si no se puede convertir.

def isint(valor):
  if valor[0] == '+' or valor[0] == '-':
    if valor[1:].isnumeric():
      return True
    
  elif valor.isnumeric():
    return True
  
  else:
    return False
  
print(isint("123"))
print(isint("+123"))
print(isint("-123"))
print(isint("1+23"))
print(isint("12.3"))