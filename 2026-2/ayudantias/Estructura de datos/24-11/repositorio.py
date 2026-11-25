import os
from datetime import date, datetime

from config import (
    ARCHIVO_LIBROS,
    ARCHIVO_PRESTAMOS,
    ARCHIVO_SOCIOS,
    ENC_LIBROS,
    ENC_PRESTAMOS,
    ENC_SOCIOS,
    ENCODE,
    FORMATO_FECHA,
)
from tipos import Libro, Prestamo, Socio


# ----------------------------- utilidades internas -----------------------------

def _leerFilas(ruta: str, encabezado: str, columnas: int) -> list[list[str]]:
    """Lee un CSV. Si no existe o está vacío, lo crea solo con el encabezado."""
    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        _escribirFilas(ruta, encabezado, [])
    with open(ruta, "r", encoding=ENCODE) as f:
        lineas: list[str] = f.read().splitlines()
    filas: list[list[str]] = []
    for numero, linea in enumerate(lineas[1:], start=2):
        if linea.strip() == "":
            continue
        datos: list[str] = linea.split(",")
        if len(datos) != columnas:
            raise ValueError(f"{os.path.basename(ruta)}, línea {numero}: se esperaban {columnas} columnas")
        filas.append(datos)
    return filas


def _escribirFilas(ruta: str, encabezado: str, filas: list[list[str]]) -> None:
    """Escribe en un archivo temporal y luego lo reemplaza (evita dejar el CSV a medias)."""
    temporal: str = ruta + ".tmp"
    with open(temporal, "w", encoding=ENCODE) as f:
        f.write(encabezado + "\n")
        for fila in filas:
            f.write(",".join(fila) + "\n")
    os.replace(temporal, ruta)


def _textoAFecha(texto: str) -> date:
    return datetime.strptime(texto, FORMATO_FECHA).date()


def _fechaATexto(fecha: date | None) -> str:
    return "" if fecha is None else fecha.isoformat()


# ----------------------------------- socios -----------------------------------

def cargarSocios() -> list[Socio]:
    socios: list[Socio] = []
    for d in _leerFilas(ARCHIVO_SOCIOS, ENC_SOCIOS, 5):
        socios.append({
            "id_socio": int(d[0]),
            "rol": d[1],
            "nombre": d[2],
            "apellido": d[3],
            "carrera": d[4],
        })
    return socios


def guardarSocios(socios: list[Socio]) -> None:
    filas: list[list[str]] = [
        [str(s["id_socio"]), s["rol"], s["nombre"], s["apellido"], s["carrera"]]
        for s in socios
    ]
    _escribirFilas(ARCHIVO_SOCIOS, ENC_SOCIOS, filas)


# ----------------------------------- libros -----------------------------------

def cargarLibros() -> list[Libro]:
    """Devuelve los libros ordenados por id (requisito de la búsqueda binaria)."""
    libros: list[Libro] = []
    for d in _leerFilas(ARCHIVO_LIBROS, ENC_LIBROS, 5):
        libros.append({
            "id_libro": int(d[0]),
            "titulo": d[1],
            "autor": d[2],
            "anio": int(d[3]),
            "copias": int(d[4]),
        })
    for i in range(1, len(libros)):
        if libros[i]["id_libro"] <= libros[i - 1]["id_libro"]:
            raise ValueError("libros.csv debe estar ordenado por id_libro y sin repetidos")
    return libros


def guardarLibros(libros: list[Libro]) -> None:
    filas: list[list[str]] = [
        [str(l["id_libro"]), l["titulo"], l["autor"], str(l["anio"]), str(l["copias"])]
        for l in libros
    ]
    _escribirFilas(ARCHIVO_LIBROS, ENC_LIBROS, filas)


# ---------------------------------- préstamos ----------------------------------

def cargarPrestamos() -> list[Prestamo]:
    prestamos: list[Prestamo] = []
    for d in _leerFilas(ARCHIVO_PRESTAMOS, ENC_PRESTAMOS, 8):
        prestamos.append({
            "id_prestamo": int(d[0]),
            "id_libro": int(d[1]),
            "id_socio": int(d[2]),
            "fecha_prestamo": _textoAFecha(d[3]),
            "dias": int(d[4]),
            "estado": d[5],
            "fecha_devolucion": _textoAFecha(d[6]) if d[6] != "" else None,
            "multa": int(d[7]),
        })
    return prestamos


def guardarPrestamos(prestamos: list[Prestamo]) -> None:
    filas: list[list[str]] = [
        [
            str(p["id_prestamo"]),
            str(p["id_libro"]),
            str(p["id_socio"]),
            p["fecha_prestamo"].isoformat(),
            str(p["dias"]),
            p["estado"],
            _fechaATexto(p["fecha_devolucion"]),
            str(p["multa"]),
        ]
        for p in prestamos
    ]
    _escribirFilas(ARCHIVO_PRESTAMOS, ENC_PRESTAMOS, filas)
