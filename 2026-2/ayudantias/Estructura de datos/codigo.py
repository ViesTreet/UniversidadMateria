"""Un atacante vulneró una red local en el Gran Concepción y borró los registros principales. Sin embargo, el equipo de seguridad logró interceptar un archivo JSON con logs de conexiones en bruto."""

print("--- SISTEMA DE ANÁLISIS FORENSE INICIADO ---")

try:
    with open("HackerLogs.json", "r", encoding="utf-8") as archivo:
        logs_interceptados = json.load(archivo)
    print(f"[+] Archivo logs.json cargado exitosamente. Se leyeron {len(logs_interceptados)} registros.\n")
except json.JSONDecodeError:
    print("[-] ERROR: El archivo 'logs.json' está corrupto o mal formateado.")
    logs_interceptados = {}

def limpiar_datos(diccionario: dict) -> dict:
    """
    Misión 1: El atacante metió ruido en los paquetes de red (números negativos).
    Debes recorrer el diccionario y eliminar cualquier número negativo de las listas de 'paquetes_red'.
    Retorna el diccionario limpio.
    """
    # Escribe tu código aquí...
    pass

def analizar_sospechoso(diccionario_limpio: dict) -> str:
    """
    Misión 2: El verdadero culpable es aquel que, después de limpiar sus datos, 
    tenga un promedio de paquetes de red inferior a 30 y esté 'activo'.
    Retorna el RUT del culpable.
    """
    # Escribe tu código aquí...
    pass

# --- ZONA DE PRUEBAS ---
# Aquí los alumnos deben llamar a las funciones e imprimir el RUT culpable.
# 1. Llamar a limpiar_datos()
# 2. Llamar a analizar_sospechoso()
# 3. Imprimir el RUT encontrado para ingresarlo en el HTML.