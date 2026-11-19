import os
from config import (ARCHIVO_PRODUCTOS, ARCHIVO_VENTAS, ARCHIVO_REPORTE, ENCODE,
                    ENCABEZADO_PRODUCTOS, ENCABEZADO_VENTAS, ENCABEZADO_REPORTE,
                    STOCK_MINIMO)
from producto import Producto


def pesos(n: int) -> str:
    return "$" + f"{n:,}".replace(",", ".")


# ======================= EJERCICIO 2: leer y guardar =======================

def listarTodos() -> list[Producto]:
    productos: list[Producto] = []
    with open(ARCHIVO_PRODUCTOS, "r", encoding=ENCODE) as f:
        lineas = f.readlines()
    for linea in lineas[1:]:          # [1:] salta el encabezado
        linea = linea.strip()
        if linea == "":
            continue
        d = linea.split(",")
        productos.append(Producto(int(d[0]), d[1], d[2], int(d[3]), int(d[4])))
    return productos


def guardarTodos(productos: list[Producto]) -> None:
    # Reescribe el archivo completo, conservando el encabezado
    with open(ARCHIVO_PRODUCTOS, "w", encoding=ENCODE) as f:
        f.write(ENCABEZADO_PRODUCTOS + "\n")
        for p in productos:
            f.write(p.aLinea() + "\n")


# ======================= EJERCICIO 3: búsquedas y altas =======================

def buscarxCodigo(codigo: int) -> Producto | None:
    for p in listarTodos():
        if p.codigo == codigo:
            return p
    return None


def buscarxCategoria(categoria: str) -> list[Producto]:
    filtro: list[Producto] = []
    for p in listarTodos():
        if p.categoria.lower() == categoria.strip().lower():
            filtro.append(p)
    return filtro


def nuevoCodigo(productos: list[Producto]) -> int:
    mayor = 0
    for p in productos:
        if p.codigo > mayor:
            mayor = p.codigo
    return mayor + 1


def agregar(nombre: str, categoria: str, precio: int, stock: int) -> tuple[bool, str]:
    nombre = nombre.strip()
    categoria = categoria.strip().capitalize()
    if nombre == "" or categoria == "":
        return False, "El nombre y la categoría no pueden estar vacíos"
    if "," in nombre or "," in categoria:
        return False, "No se permiten comas en nombre ni categoría"
    if precio <= 0:
        return False, "El precio debe ser mayor que 0"
    if stock < 0:
        return False, "El stock no puede ser negativo"

    productos = listarTodos()
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            return False, "Ya existe un producto con ese nombre"

    nuevo = Producto(nuevoCodigo(productos), nombre, categoria, precio, stock)
    with open(ARCHIVO_PRODUCTOS, "a", encoding=ENCODE) as f:   # modo "a": no pierde lo anterior
        f.write(nuevo.aLinea() + "\n")
    return True, f"Producto agregado con código {nuevo.codigo}"


# ======================= EJERCICIO 4: modificar, eliminar, vender =======================

def modificarPrecio(codigo: int, nuevoPrecio: int) -> bool:
    if nuevoPrecio <= 0:
        return False
    productos = listarTodos()
    encontrado = False
    for p in productos:
        if p.codigo == codigo:
            p.precio = nuevoPrecio
            encontrado = True
    if encontrado:
        guardarTodos(productos)
    return encontrado


def eliminar(codigo: int) -> bool:
    productos = listarTodos()
    restantes = [p for p in productos if p.codigo != codigo]
    if len(restantes) == len(productos):
        return False
    guardarTodos(restantes)
    return True


def listarVentas() -> list[dict[str, int]]:
    ventas: list[dict[str, int]] = []
    if not os.path.exists(ARCHIVO_VENTAS):
        return ventas
    with open(ARCHIVO_VENTAS, "r", encoding=ENCODE) as f:
        lineas = f.readlines()
    for linea in lineas[1:]:
        linea = linea.strip()
        if linea == "":
            continue
        d = linea.split(",")
        ventas.append({"id_venta": int(d[0]), "codigo": int(d[1]),
                       "cantidad": int(d[2]), "total": int(d[3])})
    return ventas


def siguienteIdVenta() -> int:
    mayor = 0
    for v in listarVentas():
        if v["id_venta"] > mayor:
            mayor = v["id_venta"]
    return mayor + 1


def registrarVenta(codigo: int, cantidad: int) -> tuple[bool, str]:
    producto = buscarxCodigo(codigo)
    if producto is None:
        return False, "El producto no existe"
    if cantidad <= 0:
        return False, "La cantidad debe ser mayor que 0"
    if cantidad > producto.stock:
        return False, f"Stock insuficiente (disponible: {producto.stock})"

    total = producto.precio * cantidad

    # 1) descontar stock (reescribe productos.csv)
    productos = listarTodos()
    for p in productos:
        if p.codigo == codigo:
            p.stock -= cantidad
    guardarTodos(productos)

    # 2) registrar la venta (agrega a ventas.csv)
    idVenta = siguienteIdVenta()
    if not os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, "w", encoding=ENCODE) as f:
            f.write(ENCABEZADO_VENTAS + "\n")
    with open(ARCHIVO_VENTAS, "a", encoding=ENCODE) as f:
        f.write(f"{idVenta},{codigo},{cantidad},{total}\n")

    return True, f"Venta {idVenta} registrada. Total: {pesos(total)}"


# ======================= EJERCICIO 5: estadísticas =======================

def agruparPorCategoria() -> dict[str, list[Producto]]:
    grupos: dict[str, list[Producto]] = {}
    for p in listarTodos():
        if p.categoria not in grupos:
            grupos[p.categoria] = []
        grupos[p.categoria].append(p)
    return grupos


def stockBajo(minimo: int = STOCK_MINIMO) -> list[Producto]:
    return [p for p in listarTodos() if p.stock <= minimo]


def resumenInventario() -> tuple[int, int]:
    unidades = 0
    valor = 0
    for p in listarTodos():
        unidades += p.stock
        valor += p.valorInventario()
    return unidades, valor


def productoMasCaro() -> Producto | None:
    mejor: Producto | None = None
    for p in listarTodos():
        if mejor is None or p.precio > mejor.precio:
            mejor = p
    return mejor


def ingresosPorCategoria() -> dict[str, int]:
    categoriaDe: dict[int, str] = {}
    ingresos: dict[str, int] = {}
    for p in listarTodos():
        categoriaDe[p.codigo] = p.categoria
        ingresos[p.categoria] = 0           # todas las categorías parten en 0
    for v in listarVentas():
        cat = categoriaDe.get(v["codigo"])
        if cat is None:                     # venta de un producto ya eliminado
            continue
        ingresos[cat] += v["total"]
    return ingresos


# ======================= EJERCICIO 6: reporte y menú =======================

def exportarReporte() -> int:
    grupos = agruparPorCategoria()
    ingresos = ingresosPorCategoria()
    with open(ARCHIVO_REPORTE, "w", encoding=ENCODE) as f:
        f.write(ENCABEZADO_REPORTE + "\n")
        for cat in sorted(grupos):
            lista = grupos[cat]
            unidades = sum(p.stock for p in lista)
            valor = sum(p.valorInventario() for p in lista)
            f.write(f"{cat},{len(lista)},{unidades},{valor},{ingresos[cat]}\n")
    return len(grupos)


def pedirEntero(mensaje: str) -> int | None:
    try:
        return int(input(mensaje))
    except ValueError:
        print("Debe ingresar un número entero")
        return None


def mostrarEstadisticas() -> None:
    unidades, valor = resumenInventario()
    print(f"Unidades en bodega: {unidades}")
    print(f"Valor total del inventario: {pesos(valor)}")
    caro = productoMasCaro()
    if caro is not None:
        print(f"Producto más caro: {caro.nombre} ({pesos(caro.precio)})")
    print("Productos por categoría:")
    for cat, lista in agruparPorCategoria().items():
        print(f"  {cat}: {len(lista)}")
    print("Ingresos por ventas:")
    for cat, total in ingresosPorCategoria().items():
        print(f"  {cat}: {pesos(total)}")
    print(f"Productos con stock <= {STOCK_MINIMO}:")
    for p in stockBajo():
        print("  " + p.info())


def menu() -> None:
    while True:
        print("\n1. Listar productos")
        print("2. Agregar producto")
        print("3. Buscar por código")
        print("4. Buscar por categoría")
        print("5. Modificar precio")
        print("6. Eliminar producto")
        print("7. Registrar venta")
        print("8. Estadísticas")
        print("9. Exportar reporte")
        print("0. Salir")
        op = input("Ingrese su opción: ")

        if op == "1":
            for p in listarTodos():
                print(p.info())

        elif op == "2":
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = pedirEntero("Precio: ")
            stock = pedirEntero("Stock inicial: ")
            if precio is not None and stock is not None:
                ok, msg = agregar(nombre, categoria, precio, stock)
                print(msg)

        elif op == "3":
            codigo = pedirEntero("Código: ")
            if codigo is not None:
                p = buscarxCodigo(codigo)
                print(p.info() if p is not None else "Producto no encontrado")

        elif op == "4":
            resultado = buscarxCategoria(input("Categoría: "))
            if len(resultado) == 0:
                print("Sin resultados")
            for p in resultado:
                print(p.info())

        elif op == "5":
            codigo = pedirEntero("Código: ")
            precio = pedirEntero("Nuevo precio: ")
            if codigo is not None and precio is not None:
                print("Precio actualizado" if modificarPrecio(codigo, precio)
                      else "No se pudo modificar (código inexistente o precio inválido)")

        elif op == "6":
            codigo = pedirEntero("Código a eliminar: ")
            if codigo is not None:
                print("Producto eliminado" if eliminar(codigo) else "Producto no encontrado")

        elif op == "7":
            codigo = pedirEntero("Código: ")
            cantidad = pedirEntero("Cantidad: ")
            if codigo is not None and cantidad is not None:
                ok, msg = registrarVenta(codigo, cantidad)
                print(msg)

        elif op == "8":
            mostrarEstadisticas()

        elif op == "9":
            n = exportarReporte()
            print(f"Reporte generado con {n} categorías")

        elif op == "0":
            print("Fin del programa")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
