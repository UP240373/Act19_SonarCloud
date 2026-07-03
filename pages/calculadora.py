"""
Módulo de ejemplo para la actividad SonarCloud + CI.
Contiene operaciones simples con validación básica de entradas.
"""

import logging

logger = logging.getLogger(__name__)


def sumar(a: float, b: float) -> float:
    """Regresa la suma de a y b."""
    return a + b


def restar(a: float, b: float) -> float:
    """Regresa la resta de a menos b."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Regresa el producto de a y b."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Regresa la división de a entre b.

    Lanza ValueError si b es cero.
    """
    if b == 0:
        logger.error("Intento de división entre cero: a=%s, b=%s", a, b)
        raise ValueError("No se puede dividir entre cero")
    return a / b


def es_par(n: int) -> bool:
    """Regresa True si n es par."""
    return n % 2 == 0


def promedio(numeros: list) -> float:
    """Regresa el promedio de una lista de números.

    Lanza ValueError si la lista está vacía.
    """
    if not numeros:
        logger.error("Se intentó calcular el promedio de una lista vacía")
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)


def numero_mayor(a: int, b: int) -> int:
    """Regresa el mayor entre dos números."""
    if a > b:
        return a
    return b
