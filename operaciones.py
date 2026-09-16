def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return

    print("\nCODIGO | NOMBRE | CANTIDAD | ESTADO | UBICACION")
    print("-" * 60)

    for equipo in inventario:
        print(equipo["codigo"], "|", equipo["nombre"], "|", equipo["cantidad"],
              "|", equipo["estado"], "|", equipo["ubicacion"])


def agregar_equipo(inventario):
    codigo = input("Código: ")
    nombre = input("Nombre del equipo: ")
    ubicacion = input("Ciudad: ")
    estado = input("Estado (Bueno, Regular, Dañado o En reparación): ")

    if not codigo or not nombre or not ubicacion:
        print("No dejes datos vacíos.")
        return

    if estado not in ("Bueno", "Regular", "Dañado", "En reparación"):
        print("Estado no válido.")
        return

    try:
        cantidad = int(input("Cantidad de jugadores: "))
    except ValueError:
        print("La cantidad debe ser un número.")
        return

    inventario.append({
        "codigo": codigo,
        "nombre": nombre,
        "cantidad": cantidad,
        "estado": estado,
        "ubicacion": ubicacion
    })

    print("Equipo agregado.")


def buscar_equipo(inventario):
    dato = input("Código o nombre: ").lower()

    for equipo in inventario:
        if dato in equipo["codigo"].lower() or dato in equipo["nombre"].lower():
            print(equipo)
            return

    print("No se encontró el equipo.")


def editar_equipo(inventario):
    codigo = input("Código del equipo: ").lower()

    for equipo in inventario:
        if equipo["codigo"].lower() == codigo:
            try:
                equipo["cantidad"] = int(input("Nueva cantidad: "))
                print("Equipo actualizado.")
            except ValueError:
                print("La cantidad debe ser un número.")
            return

    print("No se encontró el equipo.")


def eliminar_equipo(inventario):
    codigo = input("Código del equipo: ").lower()

    for equipo in inventario:
        if equipo["codigo"].lower() == codigo:
            inventario.remove(equipo)
            print("Equipo eliminado.")
            return

    print("No se encontró el equipo.")