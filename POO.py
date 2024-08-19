"""
creare un sistema para gestionar una pequeña biblioteca. 
y que se pueda agregar nuevos libros, buscar libros por título o autor, y mostrar 
información sobre los libros que esten disponibles disponibles.
"""
#crear clase libro
class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}"
    
#creacion clase biblio
class biblio:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

if __name__ == "__main__":
    biblioteca = biblio()

    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Mostrar todos los libros")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
            año = int(input("Ingrese el año: "))
            nuevo_libro = libro(titulo, autor, año)
            biblioteca.agregar_libro(nuevo_libro)
            print("Libro agregado exitosamente.")
        elif opcion == 2:
            titulo = input("Ingrese el título a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                print(libro)
            else:
                print("Libro no encontrado.")
        elif opcion == 3:
            biblioteca.mostrar_libros()
        elif opcion == 4:
            break
        else:
            print("Opción inválida.")