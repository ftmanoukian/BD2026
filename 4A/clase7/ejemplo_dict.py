persona_fran = {"Materia" : "BD", "Nombre" : "Fran", "Hobby" : "Musica"}
persona_manu = {"Nombre" : "Manu", "Materia" : "ISE", "Hobby" : "Cine"}
persona_ayax = {"Nombre" : "Ayax", "Materia" : "LDD", "Hobby" : "Medicina"}
persona_mechi = {"Nombre" : "Mechi", "Materia" : "Todas", "Hobby" : "Robotica"}
persona_marcos = {"Nombre" : "Marcos", "Materia" : "TI", "Hobby" : "Estudiar"}

personas = [persona_fran, persona_manu, persona_ayax, persona_mechi, persona_marcos]

for persona in personas:
  if persona['Materia'] == 'BD' or persona['Materia'] == 'ISE':
    print("Hola", persona["Nombre"], "aguante", persona["Materia"], "😎")  
  else:
    print("Hola", persona["Nombre"], "🙂")
