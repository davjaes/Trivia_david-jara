print("#######cuestionario########")

pregunta1 = "Quien descubrio america = "
pregunta2 = "En que año descubrieron america = "
pregunta3 = "Como se llama las 3 carabelas = "

respuesta1 = "Cristobal Colon"
respuesta2 = "1492"
respuesta3 = "La niña la pinta y la santa maria"

entrada1 = input(f"pregunta 1:{pregunta1}")
entrada2 = input(f"pregunta 2:{pregunta2}")
entrada3 = input(f"pregunta 3:{pregunta3}")

aciertos1 = False
aciertos2 = False
aciertos3 = False

if (entrada1 == respuesta1):
    aciertos1 = True

else:
  aciertos1 = False

  
  
if (entrada2 == respuesta2):
    aciertos2 = True
    
else: 
  aciertos2 = False



if (entrada3 == respuesta3):
    aciertos3 = True

else:
  aciertos3 = False


print("\n")


if (aciertos1 == True):
  print("pregunta 1 es correcta")
else:
  print("pregunta 1 es incorrecta")

  
  if (aciertos2 == True):
  print("pregunta 2 es correcta")
else:  
print("pregunta 2 es incorrecta")


if (aciertos3 == True):
  print("pregunta 3 es correcta")
else:
  print("pregunta 3 es incorrecta")
  