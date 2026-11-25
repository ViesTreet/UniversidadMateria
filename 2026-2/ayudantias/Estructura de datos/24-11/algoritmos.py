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
