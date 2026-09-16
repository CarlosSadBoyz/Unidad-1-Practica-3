
import json

ARCHIVO_DATOS = "dispositivos.json"


def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_datos(inventario):
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print("No se pudo guardar el archivo.")
