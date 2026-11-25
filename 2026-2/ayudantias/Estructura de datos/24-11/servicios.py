from collections.abc import Callable
from datetime import date, datetime, timedelta

from algoritmos import busquedaBinaria, ordenarBurbuja
from config import (
    ANIO_MIN,
    DIAS_MAX,
    DIAS_MIN,
    ESTADO_DEVUELTO,
    ESTADO_VIGENTE,
    FORMATO_FECHA,
    MAX_PRESTAMOS_SOCIO,
    MULTA_DIARIA,
    ROL_LARGO,
)
from repositorio import (
    cargarLibros,
    cargarPrestamos,
    cargarSocios,
    guardarLibros,
    guardarPrestamos,
    guardarSocios,
)
from tipos import FilaPrestamo, Libro, Prestamo, Socio


# ------------------------------- utilidades -------------------------------

def parsearFecha(texto: str) -> date | None:
    try:
        return datetime.strptime(texto.strip(), FORMATO_FECHA).date()
    except ValueError:
        return None


def _textoValido(texto: str) -> bool:
    return texto != "" and "," not in texto


def _siguienteId(ids: list[int]) -> int:
    return max(ids) + 1 if len(ids) > 0 else 1


def _idLibro(libro: Libro) -> int:
    return libro["id_libro"]


def fechaVencimiento(prestamo: Prestamo) -> date:
    return prestamo["fecha_prestamo"] + timedelta(days=prestamo["dias"])


def calcularMulta(fechaPrestamo: date, dias: int, fechaDevolucion: date) -> int:
    vence: date = fechaPrestamo + timedelta(days=dias)
    atraso: int = (fechaDevolucion - vence).days
    return max(0, atraso) * MULTA_DIARIA


# --------------------------------- socios ---------------------------------

def registrarSocio(rol: str, nombre: str, apellido: str, carrera: str) -> tuple[bool, str]:
    rol = rol.strip()
    nombre = nombre.strip().title()
    apellido = apellido.strip().title()
    carrera = carrera.strip().title()

    for campo in (nombre, apellido, carrera):
        if not _textoValido(campo):
            return False, "Nombre, apellido y carrera son obligatorios y no pueden llevar comas"
    if not (rol.isdigit() and len(rol) == ROL_LARGO):
        return False, f"El rol debe tener exactamente {ROL_LARGO} dígitos"

    socios: list[Socio] = cargarSocios()
    for s in socios:
        if s["rol"] == rol:
            return False, "Ya existe un socio con ese rol"

    nuevo: Socio = {
        "id_socio": _siguienteId([s["id_socio"] for s in socios]),
        "rol": rol,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera,
    }
    socios.append(nuevo)
    guardarSocios(socios)
    return True, f"Socio registrado con id {nuevo['id_socio']}"


def buscarSocio(idSocio: int) -> Socio | None:
    """Búsqueda secuencial."""
    for s in cargarSocios():
        if s["id_socio"] == idSocio:
            return s
    return None


# --------------------------------- libros ---------------------------------

def registrarLibro(titulo: str, autor: str, anio: int, copias: int) -> tuple[bool, str]:
    titulo = titulo.strip()
    autor = autor.strip()
    if not _textoValido(titulo) or not _textoValido(autor):
        return False, "Título y autor son obligatorios y no pueden llevar comas"
    if not ANIO_MIN <= anio <= date.today().year:
        return False, f"El año debe estar entre {ANIO_MIN} y {date.today().year}"
    if copias <= 0:
        return False, "Las copias deben ser un entero positivo"

    libros: list[Libro] = cargarLibros()
    for l in libros:
        if l["titulo"].lower() == titulo.lower() and l["autor"].lower() == autor.lower():
            return False, "Ese libro ya está registrado"

    nuevo: Libro = {
        "id_libro": _siguienteId([l["id_libro"] for l in libros]),
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "copias": copias,
    }
    libros.append(nuevo)
    guardarLibros(libros)
    return True, f"Libro registrado con id {nuevo['id_libro']}"


def buscarLibro(idLibro: int) -> Libro | None:
    """Búsqueda binaria (libros.csv se mantiene ordenado por id)."""
    return busquedaBinaria(cargarLibros(), idLibro, _idLibro)


def copiasDisponibles(libro: Libro, prestamos: list[Prestamo]) -> int:
    prestados: int = 0
    for p in prestamos:
        if p["id_libro"] == libro["id_libro"] and p["estado"] == ESTADO_VIGENTE:
            prestados += 1
    return libro["copias"] - prestados


def listarDisponibilidad() -> list[tuple[Libro, int]]:
    prestamos: list[Prestamo] = cargarPrestamos()
    return [(l, copiasDisponibles(l, prestamos)) for l in cargarLibros()]


# ------------------------------- préstamos -------------------------------

def registrarPrestamo(idLibro: int, idSocio: int, dias: int, fecha: date) -> tuple[bool, str]:
    if not DIAS_MIN <= dias <= DIAS_MAX:
        return False, f"Los días de préstamo deben estar entre {DIAS_MIN} y {DIAS_MAX}"
    socio: Socio | None = buscarSocio(idSocio)
    if socio is None:
        return False, "El socio no existe"
    libro: Libro | None = buscarLibro(idLibro)
    if libro is None:
        return False, "El libro no existe"

    prestamos: list[Prestamo] = cargarPrestamos()
    vigentesSocio: int = 0
    for p in prestamos:
        if p["id_socio"] == idSocio and p["estado"] == ESTADO_VIGENTE:
            if p["id_libro"] == idLibro:
                return False, "El socio ya tiene este libro en préstamo"
            vigentesSocio += 1
    if vigentesSocio >= MAX_PRESTAMOS_SOCIO:
        return False, f"El socio ya tiene {MAX_PRESTAMOS_SOCIO} préstamos vigentes"
    if copiasDisponibles(libro, prestamos) <= 0:
        return False, "No quedan copias disponibles de este libro"

    nuevo: Prestamo = {
        "id_prestamo": _siguienteId([p["id_prestamo"] for p in prestamos]),
        "id_libro": idLibro,
        "id_socio": idSocio,
        "fecha_prestamo": fecha,
        "dias": dias,
        "estado": ESTADO_VIGENTE,
        "fecha_devolucion": None,
        "multa": 0,
    }
    prestamos.append(nuevo)
    guardarPrestamos(prestamos)
    vence: date = fecha + timedelta(days=dias)
    return True, f"Préstamo {nuevo['id_prestamo']} registrado. Vence el {vence.isoformat()}"


def devolverPrestamo(idPrestamo: int, fecha: date) -> tuple[bool, str]:
    prestamos: list[Prestamo] = cargarPrestamos()
    for p in prestamos:
        if p["id_prestamo"] != idPrestamo:
            continue
        if p["estado"] == ESTADO_DEVUELTO:
            return False, "El préstamo ya fue devuelto"
        if fecha < p["fecha_prestamo"]:
            return False, "La devolución no puede ser anterior al préstamo"
        p["estado"] = ESTADO_DEVUELTO
        p["fecha_devolucion"] = fecha
        p["multa"] = calcularMulta(p["fecha_prestamo"], p["dias"], fecha)
        guardarPrestamos(prestamos)
        if p["multa"] > 0:
            return True, f"Devuelto con atraso. Multa: ${p['multa']}"
        return True, "Devuelto a tiempo. Sin multa"
    return False, "El préstamo no existe"


# --------------------------------- reportes ---------------------------------

def _clavePorFecha(fila: FilaPrestamo) -> str:
    return fila["fecha_prestamo"].isoformat()


def _clavePorTitulo(fila: FilaPrestamo) -> str:
    return fila["titulo"].lower()


def _clavePorVencimiento(fila: FilaPrestamo) -> str:
    return fila["vence"].isoformat()


CRITERIOS: dict[str, Callable[[FilaPrestamo], str]] = {
    "1": _clavePorFecha,
    "2": _clavePorTitulo,
    "3": _clavePorVencimiento,
}


def armarFilas(prestamos: list[Prestamo]) -> list[FilaPrestamo]:
    """Cruza préstamos con libros y socios usando los IDs (como un JOIN)."""
    libros: list[Libro] = cargarLibros()
    nombres: dict[int, str] = {s["id_socio"]: f"{s['nombre']} {s['apellido']}" for s in cargarSocios()}
    filas: list[FilaPrestamo] = []
    for p in prestamos:
        libro: Libro | None = busquedaBinaria(libros, p["id_libro"], _idLibro)
        if libro is None or p["id_socio"] not in nombres:
            raise ValueError(f"El préstamo {p['id_prestamo']} apunta a un libro o socio inexistente")
        filas.append({
            "id_prestamo": p["id_prestamo"],
            "socio": nombres[p["id_socio"]],
            "titulo": libro["titulo"],
            "fecha_prestamo": p["fecha_prestamo"],
            "vence": fechaVencimiento(p),
            "estado": p["estado"],
            "multa": p["multa"],
        })
    return filas


def prestamosDeSocio(idSocio: int, criterio: str) -> list[FilaPrestamo] | None:
    """Devuelve None si el socio no existe."""
    if buscarSocio(idSocio) is None:
        return None
    propios: list[Prestamo] = [p for p in cargarPrestamos() if p["id_socio"] == idSocio]
    return ordenarBurbuja(armarFilas(propios), CRITERIOS.get(criterio, _clavePorFecha))


def prestamosVencidos(fecha: date) -> list[FilaPrestamo]:
    vigentes: list[Prestamo] = [p for p in cargarPrestamos() if p["estado"] == ESTADO_VIGENTE]
    vencidos: list[FilaPrestamo] = [f for f in armarFilas(vigentes) if f["vence"] < fecha]
    return ordenarBurbuja(vencidos, _clavePorVencimiento)


def totalMultas() -> int:
    total: int = 0
    for p in cargarPrestamos():
        if p["estado"] == ESTADO_DEVUELTO:
            total += p["multa"]
    return total
