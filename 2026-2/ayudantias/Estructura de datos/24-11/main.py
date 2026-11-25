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
