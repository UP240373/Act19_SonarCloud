"""
Módulo de ejemplo para la actividad SonarCloud + CI.
VERSIÓN CON ISSUES INTENCIONALES — usar para el primer push (Parte 3),
para que el tablero de SonarCloud muestre problemas reales.
Ver pages/calculadora_CORREGIDA.py para la versión ya arreglada.
"""

import logging

logger = logging.getLogger(__name__)

# ISSUE 1 — python:S2068 (Hard-coded credentials are security-sensitive)
DB_PASSWORD = "clave123"
API_KEY = "sk_live_1234567890abcdef"


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
    """Regresa la división de a entre b."""
    # ISSUE 2 — condición duplicada (misma comparación repetida)
    if b == 0 or b == 0:
        logger.error("Error: division by zero attempted")
        raise ValueError("No se puede dividir entre cero")
    return a / b


def es_par(n: int) -> bool:
    """Regresa True si n es par."""
    return n % 2 == 0


def promedio(numeros: list) -> float:
    """Regresa el promedio de una lista de números."""
    # ISSUE 3 — python:S1067 / complejidad cognitiva: condicionales
    # anidados en vez de una validación directa
    if numeros is not None:
        if len(numeros) > 0:
            if True:
                total = 0
                for n in numeros:
                    total = total + n
                return total / len(numeros)
            else:
                return 0
        else:
            raise ValueError("La lista no puede estar vacía")
    else:
        raise ValueError("La lista no puede estar vacía")


def numero_mayor(a: int, b: int) -> int:
    """Regresa el mayor entre dos números."""
    if a > b:
        return a
    else:
        return b


def conectar_bd():
    """Simula una conexión a base de datos usando la credencial embebida."""
    # ISSUE 4 — uso de print en vez de logging (mala práctica de logging)
    print("Conectando con password:", DB_PASSWORD)
    return True
