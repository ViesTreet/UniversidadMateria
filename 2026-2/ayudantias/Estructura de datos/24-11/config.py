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
