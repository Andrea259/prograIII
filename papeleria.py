
def registrar_articulo():#Registra un nuevo artículo en la papelería.

  articulo = {}
  tipo = input("Ingrese el tipo de artículo (cuaderno o lápiz): ")
  articulo['tipo'] = tipo
  articulo['marca'] = 'HOJITAS' if tipo == 'cuaderno' else 'RAYAS'

  if tipo == 'cuaderno':
    hojas = int(input("Ingrese el número de hojas (50 o 100): "))
    articulo['hojas'] = hojas
  else:
    color = input("Ingrese el color del lápiz: ")
    articulo['color'] = color

  precio_compra = float(input("Ingrese el precio de compra: "))
  articulo['precio_venta'] = precio_compra * 1.3

  return articulo

def mostrar_articulos(articulos):
  """Muestra los detalles de los artículos registrados.

  Args:
    articulos: Una lista de diccionarios, donde cada diccionario representa un artículo.
  """

  for articulo in articulos:
    print("-------------------")
    print("Tipo:", articulo['tipo'])
    print("Marca:", articulo['marca'])
    if articulo['tipo'] == 'cuaderno':
      print("Hojas:", articulo['hojas'])
    else:
      print("Color:", articulo['color'])
    print("Precio de venta:", articulo['precio_venta'])
    print("-------------------")

# Lista para almacenar los artículos
articulos = []

# Registrar dos artículos
for _ in range(2):
  articulo_nuevo = registrar_articulo()
  articulos.append(articulo_nuevo)

# Mostrar los artículos registrados
mostrar_articulos(articulos)