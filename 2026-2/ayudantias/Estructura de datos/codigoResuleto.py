import json
from os import system

system("cls")

print("--- SISTEMA DE ANÁLISIS FORENSE INICIADO ---")

# Cargar datos desde logs.json
try:
    with open("hackerLogs.json", "r", encoding="utf-8") as archivo:
        logs_interceptados = json.load(archivo)
    print(f"[+] Archivo logs.json cargado exitosamente. Se leyeron {len(logs_interceptados)} registros.\n")
except json.JSONDecodeError:
    print("[-] ERROR: El archivo 'logs.json' está corrupto o mal formateado.")
    logs_interceptados = {}


def limpiar_datos(diccionario: dict) -> dict:
    """
    Misión 1: Elimina los números negativos (ruido) de la lista de paquetes_red de cada usuario.
    """
    # Creamos un nuevo diccionario para no alterar la referencia mientras iteramos
    diccionario_limpio = {}

    for rut, datos in diccionario.items():
        try:
            # Filtramos solo los paquetes mayores o iguales a 0
            paquetes_validos = [p for p in datos["paquetes_red"] if p >= 0]

            # Copiamos la estructura original y actualizamos los paquetes
            diccionario_limpio[rut] = {
                "alias": datos.get("alias", "Desconocido"),
                "paquetes_red": paquetes_validos,
                "estado": datos.get("estado", "inactivo")
            }
        except KeyError as err:
            print(f"[-] Advertencia: El registro del RUT {rut} está incompleto (Falta campo {err}). Omitiendo...")
        except TypeError:
            print(f"[-] Advertencia: Los paquetes del RUT {rut} no son una lista válida. Omitiendo...")

    return diccionario_limpio


def analizar_sospechoso(diccionario_limpio: dict) -> str:
    """
    Misión 2: Encuentra al culpable activo con promedio de paquetes < 30.
    """
    for rut, datos in diccionario_limpio.items():
        try:
            estado = datos["estado"]
            paquetes = datos["paquetes_red"]

            # Validar que esté activo y que tenga paquetes registrados
            if estado == "activo" and len(paquetes) > 0:
                promedio = sum(paquetes) / len(paquetes)

                if promedio < 30:
                    print(f"[!] CULPABLE DETECTADO:")
                    print(f"    RUT: {rut}")
                    print(f"    Alias: {datos['alias']}")
                    print(f"    Paquetes limpios: {paquetes}")
                    print(f"    Promedio: {promedio:.2f}")
                    print("-" * 45)
                    return rut

        except ZeroDivisionError:
            # Captura de error en caso de que la lista quede en 0 elementos
            continue
        except Exception as err:
            print(f"[-] Error inesperado al analizar el RUT {rut}: {err}")

    return "No se encontró ningún sospechoso que cumpla el criterio."


# --- ZONA DE PRUEBAS ---
try:
    if not logs_interceptados:
        raise Exception("No hay registros para analizar.")

    print("--- PASO 1: LIMPIANDO DATOS ---")
    datos_limpios = limpiar_datos(logs_interceptados)
    print(f"[+] Limpieza completada exitosamente.\n")

    print("--- PASO 2: ANALIZANDO SOSPECHOSO ---")
    rut_culpable = analizar_sospechoso(datos_limpios)

    print("\n--- RESULTADO FINAL ---")
    print(f"Ingresa la clave en el HTML: {rut_culpable}")

except Exception as e:
    print(f"[-] Ocurrió un error general en la ejecución: {e}")