
# Funciones utilitarias

def leer_float(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is None or valor >= minimo:
                return valor
            else:
                print(f"Debe ser mayor o igual que {minimo}.")
        except ValueError:
            print("Debe ingresar un número válido.")


def leer_int(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is None or valor >= minimo:
                return valor
            else:
                print(f"Debe ser mayor o igual que {minimo}.")
        except ValueError:
            print("Debe ingresar un número entero válido.")



# Funciones principales 


def generar_id(articulos):
    return len(articulos) + 1


def crear_articulo(articulos):
    print("\n--- Crear artículo ---")
    nombre = input("Nombre: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío: ").strip()
    precio = leer_float("Precio (>0): ", 0.01)
    stock = leer_int("Stock (≥0): ", 0)

    articulo = {"id": generar_id(articulos), "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
    articulos.append(articulo)
    print("Artículo agregado.\n")


def listar_articulos(articulos, solo_activos=None):
    print("\n--- Lista de artículos ---")
    for a in articulos:
        if solo_activos is True and not a["activo"]:
            mostrar = False
        elif solo_activos is False and a["activo"]:
            mostrar = False
        else:
            mostrar = True
        if mostrar:
            estado = "Activo" if a["activo"] else "Inactivo"
            print(f"ID {a['id']} | {a['nombre']} | ${a['precio']} | Stock: {a['stock']} | {estado}")
    print()


def buscar_articulo_por_id(articulos, id_busqueda):
    for a in articulos:
        if a["id"] == id_busqueda:
            return a
    return None


def actualizar_articulo(articulos):
    print("\n--- Actualizar artículo ---")
    id_b = leer_int("ID a actualizar: ", 1)
    art = buscar_articulo_por_id(articulos, id_b)
    if not art:
        print("No encontrado.\n")
        return

    nuevo_nombre = input("Nuevo nombre (Enter para mantener): ").strip()
    if nuevo_nombre:
        art["nombre"] = nuevo_nombre

    nuevo_precio = input("Nuevo precio (Enter para mantener): ").strip()
    if nuevo_precio:
        try:
            art["precio"] = float(nuevo_precio)
        except ValueError:
            print("Precio inválido.")

    nuevo_stock = input("Nuevo stock (Enter para mantener): ").strip()
    if nuevo_stock:
        try:
            art["stock"] = int(nuevo_stock)
        except ValueError:
            print("Stock inválido.")
    print("Artículo actualizado.\n")


def eliminar_articulo(articulos):
    print("\n--- Eliminar artículo ---")
    id_b = leer_int("ID a eliminar: ", 1)
    art = buscar_articulo_por_id(articulos, id_b)
    if art:
        articulos.remove(art)
        print("Artículo eliminado.\n")
    else:
        print("No encontrado.\n")


def alternar_activo(articulos):
    print("\n--- Alternar activo/inactivo ---")
    id_b = leer_int("ID del artículo: ", 1)
    art = buscar_articulo_por_id(articulos, id_b)
    if art:
        art["activo"] = not art["activo"]
        print(f"Ahora está {'activo' if art['activo'] else 'inactivo'}.\n")
    else:
        print("No encontrado.\n")


def menu_articulos():
    articulos = []
    salir = False
    while not salir:
        print("=== MENÚ ===")
        print("1. Crear artículo")
        print("2. Listar artículos")
        print("3. Buscar artículo por ID")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Activar / Desactivar")
        print("7. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_articulo(articulos)
        elif opcion == "2":
            print("1. Todos | 2. Activos | 3. Inactivos")
            sub = input("Elige una opción: ").strip()
            if sub == "2":
                listar_articulos(articulos, True)
            elif sub == "3":
                listar_articulos(articulos, False)
            else:
                listar_articulos(articulos)
        elif opcion == "3":
            id_b = leer_int("ID a buscar: ", 1)
            art = buscar_articulo_por_id(articulos, id_b)
            print(art if art else "No encontrado.", "\n")
        elif opcion == "4":
            actualizar_articulo(articulos)
        elif opcion == "5":
            eliminar_articulo(articulos)
        elif opcion == "6":
            alternar_activo(articulos)
        elif opcion == "7":
            print("Saliendo...")
            salir = True
        else:
            print("Opción no válida.\n")

# Programa principal

if __name__ == "__main__":
    menu_articulos()
