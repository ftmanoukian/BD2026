persona_fran = {"Materia" : "BD", "Nombre" : "Fran", "Hobby" : "Musica"}
persona_manu = {"Nombre" : "Manu", "Materia" : "ISE", "Hobby" : "Cine"}
persona_ayax = {"Nombre" : "Ayax", "Materia" : "LDD", "Hobby" : "Medicina"}
persona_mechi = {"Nombre" : "Mechi", "Materia" : "Todas", "Hobby" : "Robotica"}
persona_marcos = {"Nombre" : "Marcos", "Materia" : "TI", "Hobby" : "Estudiar"}

personas = [persona_fran, persona_manu, persona_ayax, persona_mechi, persona_marcos]

for persona in personas:
  if persona["Materia"] in ("BD", "TI"):
    print("Hola", persona["Nombre"], "no me compila el código")
  else:
    print("Hola", persona["Nombre"])