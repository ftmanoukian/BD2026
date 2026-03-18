# if

if True:
  print("Si forzamos el resultado que ve el if a True, SIEMPRE va a correr el bloque")

var1 = 5
var2 = 5.0

if var1 == var2:
  print("var1 y var2 son iguales en valor")
else:
  print("var1 y var2 NO son iguales en valor")

var3 = 5
var4 = 'cinco'

if var3 > var4:
  print("var3 es mayor que var4")
elif var3 < var4:
  print("var3 es menor que var4")
else:
  print("var 3 es igual que var4")


if var3 == var4 and type(var3) == type(var4):
  print("var3 y var4 son iguales en valor y en tipo")
elif var3 == var4 and not type(var3) == type(var4):
  print("var3 y var4 son iguales en valor pero NO en tipo")
elif not var3 == var4 and type(var3) == type(var4):
  print("var3 y var4 NO son iguales en valor pero SI en tipo")
else:
  print("var3 y var4 NO coinciden en valor ni en tipo")