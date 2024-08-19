#Registra un nuevo perro en la veterinaria.
def registrar_perrito():

  perrito = {}
  perrito['estado'] = 'ATENDIDO'  # Se cambia automáticamente a atendido al registrar

  # Solicitar las 8 características del perro
  for i in range(8):
    caracteristica = input(f"Ingrese la característica {i+1}: ")
    perrito[f"caracteristica_{i+1}"] = caracteristica

  # Solicitar el peso y clasificar por tamaño
  peso = float(input("Ingrese el peso del perro (en kg): "))
  perrito['tamaño'] = 'Perro grande' if peso >= 10 else 'Perro pequeño'

  return perrito

# Ejemplo de uso:
perro_nuevo = registrar_perrito()
print(perro_nuevo)