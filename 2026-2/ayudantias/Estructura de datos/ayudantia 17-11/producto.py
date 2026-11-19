class Producto:
    def __init__(self, codigo: int, nombre: str, categoria: str, precio: int, stock: int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def valorInventario(self) -> int:
        return self.precio * self.stock

    def aLinea(self) -> str:
        # Formato listo para escribir en el CSV (sin el salto de línea)
        return f"{self.codigo},{self.nombre},{self.categoria},{self.precio},{self.stock}"

    def info(self) -> str:
        precio = f"{self.precio:,}".replace(",", ".")
        return f"[{self.codigo:>2}] {self.nombre:<20} {self.categoria:<15} ${precio:>8}  Stock: {self.stock}"
