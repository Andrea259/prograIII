# Registra un nuevo auto en el concesionario.
def reg_auto():
    auto = {}
    auto['ruedas'] = 4
    auto['pasajeros'] = 5

    # Solicitar las 10 características principales del auto
    for i in range(10):
        caracteristica = input(f"Ingrese la característica {i+1}: ")
        auto[f"caracteristica_{i+1}"] = caracteristica

    precio_compra = float(input("Ingrese el precio de compra: "))
    auto['precio_venta'] = precio_compra * 1.4

    return auto

# Lista para almacenar los autos
autos = []

# Registrar varios autos
cantidad_autos = int(input("¿Cuántos autos desea registrar? "))
for _ in range(cantidad_autos):
    auto_nuevo = reg_auto()
    autos.append(auto_nuevo)

# Mostrar los autos registrados (opcional)
# Puedes implementar una función para mostrar los autos de forma más organizada
# si lo deseas.

print(autos)