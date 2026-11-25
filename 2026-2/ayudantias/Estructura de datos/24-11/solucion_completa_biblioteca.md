# Solución — Ayudantía final: Sistema de Préstamos de Biblioteca

Solución completa organizada según los ejercicios de la guía. Todo el código pasa `mypy --strict`.

**Estructura del proyecto**

```
biblioteca/
├── config.py
├── tipos.py
├── algoritmos.py
├── repositorio.py
├── servicios.py
├── main.py
├── socios.csv
├── libros.csv
├── prestamos.csv
└── requirements.txt
```

**Instalar y ejecutar**

```bash
pip install -r requirements.txt
python main.py
```

**Verificar tipos (opcional)**

```bash
pip install mypy types-colorama
mypy --strict *.py
```

---

## Ejercicio 1 — Modelo y persistencia

Constantes con tipo, `TypedDict` para cada entidad y lectura/escritura de CSV. Puntos clave:

- `_leerFilas` crea el archivo si no existe o está vacío, y lanza `ValueError` si una fila tiene columnas de más o de menos.
- `_escribirFilas` escribe en un archivo temporal y lo reemplaza con `os.replace`, así un fallo a medio escribir no corrompe el CSV.
- `cargarLibros` valida que los IDs estén en orden ascendente, requisito de la búsqueda binaria.

**`config.py`**

```python
import os

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
ENCODE: str = "utf-8"
FORMATO_FECHA: str = "%Y-%m-%d"

ARCHIVO_SOCIOS: str = os.path.join(BASE_DIR, "socios.csv")
ARCHIVO_LIBROS: str = os.path.join(BASE_DIR, "libros.csv")
ARCHIVO_PRESTAMOS: str = os.path.join(BASE_DIR, "prestamos.csv")

ENC_SOCIOS: str = "id_socio,rol,nombre,apellido,carrera"
ENC_LIBROS: str = "id_libro,titulo,autor,anio,copias"
ENC_PRESTAMOS: str = (
    "id_prestamo,id_libro,id_socio,fecha_prestamo,dias,estado,fecha_devolucion,multa"
)

ESTADO_VIGENTE: str = "VIGENTE"
ESTADO_DEVUELTO: str = "DEVUELTO"

ROL_LARGO: int = 9
ANIO_MIN: int = 1450
DIAS_MIN: int = 1
DIAS_MAX: int = 14
MAX_PRESTAMOS_SOCIO: int = 3
MULTA_DIARIA: int = 500
```

**`tipos.py`**

```python
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
```

**`repositorio.py`**

```python
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
```

---

## Ejercicio 2 — Algoritmos manuales

- `ordenarBurbuja` compara con `>` estricto, por eso es **estable**: los empates conservan el orden de entrada. Trabaja sobre una copia y corta antes si no hubo intercambios.
- `busquedaBinaria` exige que la lista esté ordenada por la clave consultada.


**`algoritmos.py`**

```python
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def ordenarBurbuja(datos: list[T], clave: Callable[[T], str]) -> list[T]:
    """Bubble Sort estable y ascendente. No modifica la lista original.

    Solo intercambia si el elemento de la izquierda es ESTRICTAMENTE mayor,
    por eso los empates conservan su orden de entrada.
    """
    copia: list[T] = list(datos)
    n: int = len(copia)
    for i in range(n - 1):
        huboCambio: bool = False
        for j in range(n - 1 - i):
            if clave(copia[j]) > clave(copia[j + 1]):
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                huboCambio = True
        if not huboCambio:
            break
    return copia


def busquedaBinaria(datos: list[T], buscado: int, clave: Callable[[T], int]) -> T | None:
    """Busca por ID en una lista ORDENADA ascendentemente por esa clave."""
    bajo: int = 0
    alto: int = len(datos) - 1
    while bajo <= alto:
        medio: int = (bajo + alto) // 2
        valor: int = clave(datos[medio])
        if valor == buscado:
            return datos[medio]
        if valor < buscado:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None
```

---

## Ejercicios 3, 4 y 5 — Servicios (`servicios.py`)

Un solo módulo con la lógica de negocio. No usa `print` ni `input`. Las funciones están agrupadas en el mismo orden de la guía:

| Ejercicio | Funciones |
|---|---|
| 3. Socios y libros | `registrarSocio`, `buscarSocio`, `registrarLibro`, `buscarLibro`, `copiasDisponibles` |
| 4. Préstamos y devoluciones | `calcularMulta`, `registrarPrestamo`, `devolverPrestamo` |
| 5. Reportes con ordenamiento | `armarFilas`, `prestamosDeSocio`, `prestamosVencidos`, `totalMultas` |

Las funciones auxiliares (`parsearFecha`, `_textoValido`, `_siguienteId`, `_idLibro`, `fechaVencimiento`, `listarDisponibilidad` y las `_clavePor...`) apoyan a las anteriores.


**`servicios.py`**

```python
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
```

---

## Ejercicio 6 — Menú con colorama

Las funciones de salida (`titulo`, `encabezado`, `exito`, `error`, `aviso`) concentran el uso de colorama. Cada opción del menú es una función y se despacha con el diccionario `ACCIONES`. Todo se ejecuta dentro de `try/except (OSError, ValueError)`.


**`main.py`**

```python
from collections.abc import Callable
from datetime import date

from colorama import Fore, Style, init

from config import ESTADO_VIGENTE, MULTA_DIARIA
from servicios import (
    buscarLibro,
    devolverPrestamo,
    listarDisponibilidad,
    parsearFecha,
    prestamosDeSocio,
    prestamosVencidos,
    registrarLibro,
    registrarPrestamo,
    registrarSocio,
    totalMultas,
)
from repositorio import cargarSocios
from tipos import FilaPrestamo, Libro, Socio

init(autoreset=True)


# ----------------------------- salida con colorama -----------------------------

def titulo(texto: str) -> None:
    print(Style.BRIGHT + Fore.CYAN + f"\n=== {texto} ===")


def encabezado(texto: str) -> None:
    print(Style.BRIGHT + Fore.BLUE + texto)


def exito(texto: str) -> None:
    print(Fore.GREEN + "✔ " + texto)


def error(texto: str) -> None:
    print(Fore.RED + "✘ " + texto)


def aviso(texto: str) -> None:
    print(Fore.YELLOW + "! " + texto)


def mostrarResultado(resultado: tuple[bool, str]) -> None:
    ok, mensaje = resultado
    if ok:
        exito(mensaje)
    else:
        error(mensaje)


# ------------------------------ entrada validada ------------------------------

def pedirEntero(mensaje: str) -> int | None:
    try:
        return int(input(mensaje).strip())
    except ValueError:
        error("Debe ingresar un número entero")
        return None


def pedirFecha(mensaje: str) -> date | None:
    """Enter = hoy. Devuelve None si el formato es inválido."""
    texto: str = input(f"{mensaje} (AAAA-MM-DD, Enter = hoy): ").strip()
    if texto == "":
        return date.today()
    fecha: date | None = parsearFecha(texto)
    if fecha is None:
        error("Fecha inválida, use el formato AAAA-MM-DD")
    return fecha


# ----------------------------------- reportes -----------------------------------

def imprimirFilas(filas: list[FilaPrestamo]) -> None:
    if len(filas) == 0:
        aviso("Sin resultados")
        return
    encabezado(f"{'ID':>3} {'Socio':<20} {'Título':<30} {'Préstamo':<10} {'Vence':<10} {'Estado':<9} {'Multa':>6}")
    for f in filas:
        color: str = Fore.GREEN if f["estado"] == ESTADO_VIGENTE else Fore.WHITE
        print(
            color
            + f"{f['id_prestamo']:>3} {f['socio']:<20} {f['titulo'][:30]:<30} "
            + f"{f['fecha_prestamo'].isoformat():<10} {f['vence'].isoformat():<10} "
            + f"{f['estado']:<9} {f['multa']:>6}"
        )


# ---------------------------------- opciones ----------------------------------

def opcionRegistrarSocio() -> None:
    titulo("Registrar socio")
    rol: str = input("Rol (9 dígitos): ")
    nombre: str = input("Nombre: ")
    apellido: str = input("Apellido: ")
    carrera: str = input("Carrera: ")
    mostrarResultado(registrarSocio(rol, nombre, apellido, carrera))


def opcionListarSocios() -> None:
    titulo("Socios")
    encabezado(f"{'ID':>3} {'Rol':<10} {'Nombre':<22} {'Carrera'}")
    socios: list[Socio] = cargarSocios()
    for s in socios:
        print(f"{s['id_socio']:>3} {s['rol']:<10} {s['nombre'] + ' ' + s['apellido']:<22} {s['carrera']}")


def opcionRegistrarLibro() -> None:
    titulo("Registrar libro")
    tit: str = input("Título: ")
    autor: str = input("Autor: ")
    anio: int | None = pedirEntero("Año: ")
    copias: int | None = pedirEntero("Copias: ")
    if anio is not None and copias is not None:
        mostrarResultado(registrarLibro(tit, autor, anio, copias))


def opcionListarLibros() -> None:
    titulo("Libros y disponibilidad")
    encabezado(f"{'ID':>3} {'Título':<32} {'Autor':<18} {'Año':>4} {'Disp.':>6}")
    for libro, disponibles in listarDisponibilidad():
        color: str = Fore.GREEN if disponibles > 0 else Fore.RED
        print(
            color
            + f"{libro['id_libro']:>3} {libro['titulo'][:32]:<32} {libro['autor'][:18]:<18} "
            + f"{libro['anio']:>4} {disponibles:>3}/{libro['copias']:<2}"
        )


def opcionBuscarLibro() -> None:
    titulo("Buscar libro por id")
    idLibro: int | None = pedirEntero("Id del libro: ")
    if idLibro is None:
        return
    libro: Libro | None = buscarLibro(idLibro)
    if libro is None:
        error("Libro no encontrado")
    else:
        exito(f"{libro['titulo']} — {libro['autor']} ({libro['anio']}), {libro['copias']} copias")


def opcionRegistrarPrestamo() -> None:
    titulo("Registrar préstamo")
    idSocio: int | None = pedirEntero("Id del socio: ")
    idLibro: int | None = pedirEntero("Id del libro: ")
    dias: int | None = pedirEntero("Días de préstamo: ")
    fecha: date | None = pedirFecha("Fecha del préstamo")
    if idSocio is not None and idLibro is not None and dias is not None and fecha is not None:
        mostrarResultado(registrarPrestamo(idLibro, idSocio, dias, fecha))


def opcionDevolver() -> None:
    titulo("Devolver libro")
    idPrestamo: int | None = pedirEntero("Id del préstamo: ")
    fecha: date | None = pedirFecha("Fecha de devolución")
    if idPrestamo is not None and fecha is not None:
        mostrarResultado(devolverPrestamo(idPrestamo, fecha))


def opcionPrestamosSocio() -> None:
    titulo("Préstamos de un socio")
    idSocio: int | None = pedirEntero("Id del socio: ")
    if idSocio is None:
        return
    print("Ordenar por: 1. Fecha de préstamo  2. Título  3. Vencimiento")
    criterio: str = input("Opción: ").strip()
    filas: list[FilaPrestamo] | None = prestamosDeSocio(idSocio, criterio)
    if filas is None:
        error("El socio no existe")
    else:
        imprimirFilas(filas)


def opcionVencidos() -> None:
    titulo("Préstamos vencidos")
    fecha: date | None = pedirFecha("Fecha de consulta")
    if fecha is not None:
        imprimirFilas(prestamosVencidos(fecha))


def opcionTotalMultas() -> None:
    titulo("Multas cobradas")
    aviso(f"Tarifa de atraso: ${MULTA_DIARIA} por día")
    exito(f"Total recaudado: ${totalMultas()}")


ACCIONES: dict[str, Callable[[], None]] = {
    "1": opcionRegistrarSocio,
    "2": opcionListarSocios,
    "3": opcionRegistrarLibro,
    "4": opcionListarLibros,
    "5": opcionBuscarLibro,
    "6": opcionRegistrarPrestamo,
    "7": opcionDevolver,
    "8": opcionPrestamosSocio,
    "9": opcionVencidos,
    "10": opcionTotalMultas,
}


def mostrarMenu() -> None:
    titulo("Biblioteca Campus")
    print("1. Registrar socio        6. Registrar préstamo")
    print("2. Listar socios          7. Devolver libro")
    print("3. Registrar libro        8. Préstamos de un socio")
    print("4. Listar libros          9. Préstamos vencidos")
    print("5. Buscar libro por id   10. Total de multas")
    print("0. Salir")


def main() -> None:
    while True:
        mostrarMenu()
        op: str = input("Ingrese su opción: ").strip()
        if op == "0":
            aviso("Fin del programa")
            break
        accion: Callable[[], None] | None = ACCIONES.get(op)
        if accion is None:
            error("Opción inválida")
            continue
        try:
            accion()
        except (OSError, ValueError) as e:
            error(f"Problema con los archivos o los datos: {e}")


if __name__ == "__main__":
    main()
```

---

## Archivos de datos


**`socios.csv`**

```csv
id_socio,rol,nombre,apellido,carrera
1,202573001,Camila,Soto,Informática
2,202573002,Diego,Pérez,Electrónica
3,202573003,Valentina,Araya,Informática
4,202573004,Martín,Salinas,Civil
5,202573005,Fernanda,Vega,Informática
6,202573006,Joaquín,Torres,Industrial
```

**`libros.csv`**

```csv
id_libro,titulo,autor,anio,copias
1,Estructuras de Datos en Python,Luis Martínez,2021,3
2,Algoritmos y Complejidad,Ana Torres,2018,2
3,Bases de Datos Relacionales,Carlos Rojas,2019,2
4,Redes de Computadoras,Andrew Tanenbaum,2011,1
5,Sistemas Operativos Modernos,Andrew Tanenbaum,2015,2
6,Cálculo de una Variable,James Stewart,2016,4
7,Arquitectura de Computadores,John Hennessy,2017,1
8,Ingeniería de Software,Ian Sommerville,2016,2
```

**`prestamos.csv`**

```csv
id_prestamo,id_libro,id_socio,fecha_prestamo,dias,estado,fecha_devolucion,multa
1,1,1,2026-10-01,7,DEVUELTO,2026-10-06,0
2,2,1,2026-10-10,7,DEVUELTO,2026-10-20,1500
3,3,2,2026-10-15,14,DEVUELTO,2026-10-29,0
4,4,3,2026-11-10,7,VIGENTE,,0
5,1,1,2026-11-18,7,VIGENTE,,0
6,6,4,2026-11-05,7,DEVUELTO,2026-11-14,1000
7,5,3,2026-11-20,7,VIGENTE,,0
8,7,3,2026-11-21,7,VIGENTE,,0
9,8,5,2026-11-01,7,VIGENTE,,0
10,6,2,2026-11-22,5,VIGENTE,,0
```

**`requirements.txt`**

```text
colorama>=0.4.6
```

---

## Resultados esperados de las pruebas de aceptación

Con los CSV originales y fecha **2026-11-24**:

| Escenario | Resultado |
|---|---|
| Rol repetido o de largo distinto de 9 | `Ya existe un socio con ese rol` / `El rol debe tener exactamente 9 dígitos` |
| Libro con 0 copias, año futuro o repetido | Rechazado |
| Préstamo de 0 o 15 días | `Los días de préstamo deben estar entre 1 y 14` |
| Préstamo del libro 4 | `No quedan copias disponibles de este libro` |
| Cuarto préstamo del socio 3 | `El socio ya tiene 3 préstamos vigentes` |
| Socio 1 pide el libro 1 | `El socio ya tiene este libro en préstamo` |
| Socio 6, libro 2, 7 días | `Préstamo 11 registrado. Vence el 2026-12-01` |
| Devolver préstamo 9 | `Devuelto con atraso. Multa: $8000` |
| Devolver préstamo 9 otra vez | `El préstamo ya fue devuelto` |
| Devolver préstamo 5 el 2026-11-20 | `Devuelto a tiempo. Sin multa` |
| Socio 1 por fecha | Préstamos 1, 2, 5 |
| Socio 1 por título | Préstamos 2, 1, 5 (estable: empate entre 1 y 5) |
| Vencidos al 2026-11-24 (datos originales) | Préstamos 9 y 4 |
| Total de multas (datos originales) | `$2500` |
| CSV inexistente o vacío | Se recrea con su encabezado |
| Fila con columnas faltantes | Error en rojo, el programa sigue |
