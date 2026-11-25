from datetime import date
from typing import TypedDict


class Socio(TypedDict):
    id_socio: int
    rol: str
    nombre: str
    apellido: str
    carrera: str


class Libro(TypedDict):
    id_libro: int
    titulo: str
    autor: str
    anio: int
    copias: int


class Prestamo(TypedDict):
    id_prestamo: int
    id_libro: int
    id_socio: int
    fecha_prestamo: date
    dias: int
    estado: str
    fecha_devolucion: date | None
    multa: int


class FilaPrestamo(TypedDict):
    """Resultado de cruzar prestamos con libros y socios mediante sus IDs."""

    id_prestamo: int
    socio: str
    titulo: str
    fecha_prestamo: date
    vence: date
    estado: str
    multa: int
