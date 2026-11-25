# Ayudantía final — Sistema de Préstamos de Biblioteca

**Duración:** 1 hora · **Modalidad:** individual o en parejas · **Tecnologías:** Python · archivos CSV · colorama · type hints

| Archivos entregados | Para instalar y ejecutar |
|---|---|
| `socios.csv`, `libros.csv`, `prestamos.csv`, `requirements.txt` | `pip install -r requirements.txt` y luego `python main.py` |

---

## 1. Contexto

La Biblioteca Campus necesita una aplicación de consola para administrar **socios**, **libros** y **préstamos**. La información se guarda en tres archivos CSV relacionados por identificadores (sin base de datos):

| Archivo | Campos |
|---|---|
| `socios.csv` | `id_socio, rol, nombre, apellido, carrera` |
| `libros.csv` | `id_libro, titulo, autor, anio, copias` |
| `prestamos.csv` | `id_prestamo, id_libro, id_socio, fecha_prestamo, dias, estado, fecha_devolucion, multa` |

`prestamos.csv` no repite datos de socios ni de libros: los reportes los obtienen **cruzando por ID**.

## 2. Reglas de negocio

- El **rol** del socio tiene exactamente 9 dígitos y no se puede repetir.
- Un libro tiene `copias` físicas. Copias disponibles = copias − préstamos `VIGENTE` de ese libro.
- Un préstamo dura entre **1 y 14 días**. Vence en `fecha_prestamo + dias`.
- Un socio puede tener como máximo **3 préstamos vigentes** y no puede tener dos veces el mismo libro vigente.
- Al devolver, la multa es **$500 por cada día de atraso** (0 si se devuelve a tiempo o el mismo día del vencimiento).
- Un préstamo devuelto no se puede devolver otra vez. Un préstamo está **vencido** si está vigente y su fecha de vencimiento es anterior a la fecha de consulta.
- Los textos no pueden estar vacíos ni contener comas (romperían el CSV).

## 3. Objetivos

1. Leer y escribir archivos CSV, manejando archivos inexistentes, vacíos o corruptos.
2. Modelar datos con **`TypedDict`** y anotar el tipo de **todos** los parámetros y retornos.
3. Relacionar tres archivos mediante IDs (equivalente a un JOIN).
4. Implementar **a mano** dos técnicas: **Bubble Sort** (ordenamiento) y **búsqueda binaria**. No se permite `sort()` ni `sorted()` para ordenar los reportes.
5. Validar entradas y reglas de negocio, y manejar excepciones (`ValueError`, `OSError`).
6. Usar `colorama` con criterio: títulos, éxito, error, aviso y encabezados de tablas.

## 4. Requisitos técnicos

- Módulos separados: `config.py`, `tipos.py`, `algoritmos.py`, `repositorio.py`, `servicios.py`, `main.py`.
- Las funciones que modifican datos devuelven `tuple[bool, str]` (¿se pudo?, mensaje). La capa de servicios **no usa `print` ni `input`**.
- Fechas como `datetime.date`, no como `str`, dentro del programa. En el CSV se guardan como `AAAA-MM-DD`.
- El código debe pasar sin errores: `mypy --strict *.py`.
- El orden persistido de los archivos no debe alterarse al generar reportes.

---

## 5. Ejercicios

### Ejercicio 1 — Modelo y persistencia (10 min)

**Qué hay que hacer**

1. En `config.py` defina las rutas, el encoding, los encabezados y las constantes de las reglas (días máximos, multa, etc.), todas con su tipo.
2. En `tipos.py` defina los `TypedDict`: `Socio`, `Libro`, `Prestamo` y `FilaPrestamo` (resultado del cruce: `id_prestamo, socio, titulo, fecha_prestamo, vence, estado, multa`).
3. En `repositorio.py` implemente:

| Función | Descripción |
|---|---|
| `cargarSocios() -> list[Socio]` | Lee el CSV; si no existe o está vacío, lo crea con su encabezado |
| `guardarSocios(socios: list[Socio]) -> None` | Reescribe el archivo completo |
| `cargarLibros() -> list[Libro]` | Igual, pero falla con `ValueError` si los IDs no están en orden ascendente |
| `guardarLibros(libros: list[Libro]) -> None` | |
| `cargarPrestamos() -> list[Prestamo]` | Convierte fechas a `date` y la devolución vacía a `None` |
| `guardarPrestamos(prestamos: list[Prestamo]) -> None` | |

Una fila con cantidad de columnas incorrecta debe lanzar `ValueError` indicando archivo y línea.

### Ejercicio 2 — Algoritmos manuales (10 min)

**Qué hay que hacer** (en `algoritmos.py`, de forma genérica con `TypeVar`)

| Función | Descripción |
|---|---|
| `ordenarBurbuja(datos: list[T], clave: Callable[[T], str]) -> list[T]` | Bubble Sort ascendente que **devuelve una copia** y se detiene antes si no hubo intercambios. Debe ser **estable** (empates conservan su orden) |
| `busquedaBinaria(datos: list[T], buscado: int, clave: Callable[[T], int]) -> T \| None` | Busca por ID en una lista ordenada |

*Pregunta de discusión:* ¿por qué la búsqueda binaria es válida para `libros.csv` pero no la usamos para `socios`? (Respuesta esperada: la usamos en libros porque se consulta mucho por ID y el archivo se mantiene ordenado por ID; en socios basta una búsqueda secuencial, y es útil comparar ambas.)

### Ejercicio 3 — Socios y libros (10 min)

**Qué hay que hacer** (en `servicios.py`)

| Función | Descripción |
|---|---|
| `registrarSocio(rol: str, nombre: str, apellido: str, carrera: str) -> tuple[bool, str]` | Valida las reglas, normaliza con `.strip().title()`, asigna el siguiente ID |
| `buscarSocio(idSocio: int) -> Socio \| None` | Búsqueda secuencial |
| `registrarLibro(titulo: str, autor: str, anio: int, copias: int) -> tuple[bool, str]` | Año entre 1450 y el año actual, copias positivas, sin repetir título + autor |
| `buscarLibro(idLibro: int) -> Libro \| None` | Usa `busquedaBinaria` |
| `copiasDisponibles(libro: Libro, prestamos: list[Prestamo]) -> int` | |

### Ejercicio 4 — Préstamos y devoluciones (15 min)

**Qué hay que hacer**

| Función | Descripción |
|---|---|
| `calcularMulta(fechaPrestamo: date, dias: int, fechaDevolucion: date) -> int` | Multa según la regla de atraso |
| `registrarPrestamo(idLibro: int, idSocio: int, dias: int, fecha: date) -> tuple[bool, str]` | Valida días, existencia de socio y libro, máximo de préstamos, libro repetido y copias disponibles. Estado inicial `VIGENTE`, devolución `None`, multa 0 |
| `devolverPrestamo(idPrestamo: int, fecha: date) -> tuple[bool, str]` | Rechaza préstamos inexistentes, ya devueltos o con fecha anterior al préstamo. Registra fecha y multa, y cambia el estado a `DEVUELTO` |

### Ejercicio 5 — Reportes con ordenamiento (10 min)

**Qué hay que hacer**

| Función | Descripción |
|---|---|
| `armarFilas(prestamos: list[Prestamo]) -> list[FilaPrestamo]` | Cruza préstamos con libros (búsqueda binaria) y socios (por ID). Si un ID no existe, lanza `ValueError` |
| `prestamosDeSocio(idSocio: int, criterio: str) -> list[FilaPrestamo] \| None` | Devuelve `None` si el socio no existe. Criterios: `"1"` fecha de préstamo, `"2"` título (sin distinguir mayúsculas), `"3"` vencimiento. Ordena con `ordenarBurbuja` |
| `prestamosVencidos(fecha: date) -> list[FilaPrestamo]` | Vigentes vencidos a esa fecha, ordenados por vencimiento |
| `totalMultas() -> int` | Suma de multas de los préstamos devueltos |

### Ejercicio 6 — Menú con colorama (5 min)

**Qué hay que hacer** (en `main.py`)

1. Funciones `titulo`, `encabezado`, `exito`, `error` y `aviso`, cada una con un color distinto.
2. `pedirEntero(mensaje: str) -> int | None` y `pedirFecha(mensaje: str) -> date | None` (Enter = hoy). Ante un dato inválido muestran un error y devuelven `None`, sin cerrar el programa.
3. Menú con ciclo hasta elegir salir, con las opciones: registrar y listar socios, registrar y listar libros (mostrando disponibles/total), buscar libro por ID, registrar préstamo, devolver, préstamos de un socio, vencidos y total de multas.
4. Cada operación se ejecuta dentro de un `try/except (OSError, ValueError)` que muestra el problema en rojo.

---

## 6. Pruebas mínimas de aceptación

Con los CSV entregados y como fecha de consulta/devolución **2026-11-24**:

| Escenario | Resultado esperado |
|---|---|
| Registrar socio con rol repetido (`202573001`) o de largo distinto de 9 | Rechazado |
| Registrar libro con 0 copias, año futuro o título + autor repetido | Rechazado |
| Préstamo de 15 días, o de 0 días | Rechazado |
| Préstamo del libro 4 (1 copia, ya prestada) | Rechazado: sin copias |
| Cuarto préstamo vigente para el socio 3 | Rechazado |
| Socio 1 pide el libro 1 (ya lo tiene vigente) | Rechazado |
| Socio o libro inexistente | Rechazado |
| Préstamo válido (socio 6, libro 2, 7 días) | Aceptado; vence el 2026-12-01 |
| Devolver préstamo 9 (vencía el 2026-11-08) | Multa `$8000` |
| Devolver préstamo 9 por segunda vez | Rechazado |
| Devolver préstamo 5 el 2026-11-20 | Sin multa |
| Préstamos del socio 1 ordenados por **fecha** | Préstamos 1, 2, 5 |
| Préstamos del socio 1 ordenados por **título** | Préstamos 2, 1, 5 (los empates mantienen su orden: estabilidad) |
| Préstamos vencidos al 2026-11-24 (datos originales) | Préstamos 9 y 4, en ese orden |
| Total de multas (datos originales) | `$2500` |
| Borrar un CSV o dejarlo vacío y ejecutar | El programa lo recrea, sin caerse |
| Agregar una fila con columnas de menos a un CSV | Mensaje de error en rojo, el programa sigue |
| Cerrar y volver a abrir el programa | Los datos se conservan |
| `mypy --strict *.py` | Sin errores |

## 7. Si falta tiempo

Dejen para el final: `prestamosVencidos`, `totalMultas` y la opción 3 (vencimiento) del criterio de orden. El núcleo evaluable son los ejercicios 1 al 4 más `prestamosDeSocio`.
