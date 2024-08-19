#Registra un nuevo dispositivo electrónico PHR.
def registrar_dispo():
  dispositivo = {}
  dispositivo['marca'] = 'PHR'

  # Solicitar las 6 características del dispositivo
  for i in range(6):
    caracteristica = input(f"Ingrese la característica {i+1}: ")
    dispositivo[f"caracteristica_{i+1}"] = caracteristica

  precio_compra = float(input("Ingrese el precio de compra: "))
  dispositivo['precio_venta'] = precio_compra * 1.7

  return dispositivo

# Lista para almacenar los dispositivos
dispositivos = []

# Registrar varios dispositivos
cantidad_dispositivos = int(input("¿Cuántos dispositivos desea registrar? "))
for _ in range(cantidad_dispositivos):
  dispositivo_nuevo = registrar_dispo()
  dispositivos.append(dispositivo_nuevo)
print(dispositivos)