# Ayudantía — Gestión de inventario con archivos CSV, clases y tipos

**Duración:** 1 h 10 min
**Archivos entregados:** `productos.csv`, `ventas.csv`

## Contexto

Una tienda de tecnología guarda su información en dos archivos CSV (ambos con fila de encabezado):

- `productos.csv` → `codigo,nombre,categoria,precio,stock`
- `ventas.csv` → `id_venta,codigo,cantidad,total`

Ambos se relacionan por `codigo`. Se debe construir un programa por consola con menú que permita administrar el inventario y registrar ventas. Los cambios deben **persistir** al cerrar y volver a abrir el programa.

## Objetivos

1. Leer, agregar y reescribir archivos de texto (modos `"r"`, `"a"` y `"w"`).
2. Convertir líneas de texto (`split`, `strip`) en objetos y convertir tipos (`int`).
3. Definir una clase con atributos tipados y métodos.
4. Usar *type hints* en todas las funciones: `list[Producto]`, `dict[str, list[Producto]]`, `tuple[bool, str]`, `Producto | None`.
5. Usar diccionarios para agrupar y acumular datos.
6. Relacionar dos archivos mediante un identificador.
7. Validar entradas sin que el programa termine abruptamente.

## Estructura del proyecto

```
config.py        → constantes (nombres de archivo, encoding, encabezados)
producto.py      → clase Producto
inventario.py    → funciones y menú
productos.csv
ventas.csv
```

---

## Ejercicio 1 — Configuración y clase `Producto` (10 min)

**Qué hay que hacer**

1. En `config.py` defina las constantes: `ARCHIVO_PRODUCTOS`, `ARCHIVO_VENTAS`, `ARCHIVO_REPORTE`, `ENCODE`, `ENCABEZADO_PRODUCTOS`, `ENCABEZADO_VENTAS`, `ENCABEZADO_REPORTE` y `STOCK_MINIMO` (valor 5).
2. En `producto.py` cree la clase `Producto` con los atributos `codigo: int`, `nombre: str`, `categoria: str`, `precio: int`, `stock: int`.
3. Agregue los métodos:
   - `valorInventario(self) -> int` → precio × stock.
   - `aLinea(self) -> str` → texto en formato CSV, sin salto de línea.
   - `info(self) -> str` → texto legible para mostrar por pantalla.

---

## Ejercicio 2 — Leer y guardar el archivo (10 min)

**Qué hay que hacer**

1. `listarTodos() -> list[Producto]`: leer `productos.csv`, **saltar el encabezado**, ignorar líneas vacías y devolver una lista de objetos `Producto` (con `precio` y `stock` convertidos a `int`).
2. `guardarTodos(productos: list[Producto]) -> None`: reescribir `productos.csv` completo, **conservando el encabezado**.

*Prueba:* leer la lista, guardarla sin cambios y comprobar que el archivo queda idéntico.

---

## Ejercicio 3 — Búsquedas y altas (15 min)

**Qué hay que hacer**

1. `buscarxCodigo(codigo: int) -> Producto | None`.
2. `buscarxCategoria(categoria: str) -> list[Producto]` (sin distinguir mayúsculas/minúsculas).
3. `nuevoCodigo(productos: list[Producto]) -> int`: devuelve el mayor código existente + 1.
4. `agregar(nombre: str, categoria: str, precio: int, stock: int) -> tuple[bool, str]`:
   - Rechazar nombre o categoría vacíos, o que contengan comas.
   - Rechazar `precio <= 0` y `stock < 0`.
   - Rechazar nombres repetidos.
   - Si todo está bien, **agregar la línea al final del archivo** (sin reescribirlo) y devolver `(True, mensaje)`. Si no, `(False, motivo)`.

---

## Ejercicio 4 — Modificar, eliminar y vender (15 min)

**Qué hay que hacer**

1. `modificarPrecio(codigo: int, nuevoPrecio: int) -> bool`: rechaza precios no positivos o códigos inexistentes.
2. `eliminar(codigo: int) -> bool`: elimina el producto y reescribe el archivo.
3. `listarVentas() -> list[dict[str, int]]`: lee `ventas.csv` y devuelve cada venta como diccionario con las claves `id_venta`, `codigo`, `cantidad` y `total`. Si el archivo no existe, devuelve una lista vacía.
4. `siguienteIdVenta() -> int`.
5. `registrarVenta(codigo: int, cantidad: int) -> tuple[bool, str]`:
   - Validar que el producto exista, que la cantidad sea positiva y que haya stock suficiente.
   - Descontar el stock en `productos.csv`.
   - Agregar la venta a `ventas.csv` con `total = precio × cantidad`.

---

## Ejercicio 5 — Diccionarios y estadísticas (15 min)

**Qué hay que hacer**

1. `agruparPorCategoria() -> dict[str, list[Producto]]`.
2. `stockBajo(minimo: int = STOCK_MINIMO) -> list[Producto]`: productos con stock menor o igual al mínimo.
3. `resumenInventario() -> tuple[int, int]`: `(unidades totales, valor total del inventario)`.
4. `productoMasCaro() -> Producto | None`.
5. `ingresosPorCategoria() -> dict[str, int]`: relacionar `ventas.csv` con `productos.csv` mediante `codigo` y sumar los totales por categoría. Todas las categorías deben aparecer, incluso con ingreso 0. Ignorar ventas de productos que ya no existen.

---

## Ejercicio 6 — Reporte y menú (5 min)

**Qué hay que hacer**

1. `exportarReporte() -> int`: crear o sobrescribir `reporte_inventario.csv` con las columnas
   `categoria,cantidad_productos,unidades,valor_inventario,ingresos`, una fila por categoría (ordenadas alfabéticamente). Devuelve la cantidad de filas escritas. No debe modificar los archivos originales.
2. Implementar un menú con ciclo `while True` y las opciones:

```
1. Listar productos        6. Eliminar producto
2. Agregar producto        7. Registrar venta
3. Buscar por código       8. Estadísticas
4. Buscar por categoría    9. Exportar reporte
5. Modificar precio        0. Salir
```

3. Las entradas numéricas deben validarse con `try/except ValueError`: si el usuario escribe texto, mostrar un mensaje y volver al menú.

---

## Casos de prueba sugeridos

- Agregar un producto, cerrar el programa, abrirlo de nuevo y verificar que sigue ahí.
- Agregar un nombre repetido, un precio `0` y un stock negativo → deben rechazarse.
- Vender más unidades que el stock (por ejemplo, código 20 que tiene stock 0) → debe rechazarse.
- Vender el producto 17 (stock 2) en dos ventas de 1 unidad → la tercera debe fallar.
- Eliminar un producto que tiene ventas → `ingresosPorCategoria()` no debe caerse.
- Escribir `abc` donde se pide un número → el programa no debe cerrarse.
- Exportar el reporte y comprobar que incluye las 6 categorías.
