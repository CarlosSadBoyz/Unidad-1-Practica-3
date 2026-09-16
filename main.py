import time
from datos import cargar_datos, guardar_datos
from operaciones import mostrar_inventario, agregar_equipo, buscar_equipo, editar_equipo, eliminar_equipo


def mostrar_menu():
    print("\n========== INVENTARIO LIGA MX ==========")
    print("1. Agregar equipo")
    print("2. Mostrar inventario")
    print("3. Buscar equipo")
    print("4. Editar equipo")
    print("5. Eliminar equipo")
    print("6. Guardar y salir")
    print("7. Salir sin guardar")
    print("========================================")


def main():
    inventario = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        match opcion:
            case "1":
                agregar_equipo(inventario)
            case "2":
                mostrar_inventario(inventario)
            case "3":
                buscar_equipo(inventario)
            case "4":
                editar_equipo(inventario)
            case "5":
                eliminar_equipo(inventario)
            case "6":
                guardar_datos(inventario)
                print("Datos guardados.")
                break
            case "7":
                print("Salida sin guardar.")
                break
            case _:
                print("Opción no válida.")
        time.sleep(1)


if __name__ == "__main__":
    main()
