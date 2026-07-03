"""
Módulo de ejemplo para la actividad SonarCloud + CI.
VERSIÓN CORREGIDA — reemplaza pages/calculadora.py con este contenido
para la Parte 4 (o para un segundo commit que muestre la mejora del
Quality Gate).

Correcciones aplicadas:
  1. python:S2068 (Hard-coded credentials) -> las credenciales ahora se
     leen de variables de entorno con os.environ, no quedan en el código.
  2. Condición duplicada `b == 0 or b == 0` -> se deja una sola comparación.
  3. python:S1067 (Cognitive Complexity) -> se aplanan los condicionales
     anidados de `promedio` usando cláusulas de guarda (early return).
  4. Uso de `print` para reportar conexión -> se reemplaza por `logger`.
"""

import logging
import os

logger = logging.getLogger(__name__)

# FIX 1 — las credenciales ya no están hard-codeadas: se leen del entorno.
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
API_KEY = os.environ.get("API_KEY", "")


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
    # FIX 2 — condición única, sin duplicado.
    if b == 0:
        logger.error("Intento de división entre cero: a=%s, b=%s", a, b)
        raise ValueError("No se puede dividir entre cero")
    return a / b


def es_par(n: int) -> bool:
    """Regresa True si n es par."""
    return n % 2 == 0


def promedio(numeros: list) -> float:
    """Regresa el promedio de una lista de números."""
    # FIX 3 — cláusulas de guarda en vez de condicionales anidados.
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)


def numero_mayor(a: int, b: int) -> int:
    """Regresa el mayor entre dos números."""
    if a > b:
        return a
    return b


def conectar_bd():
    """Simula una conexión a base de datos usando la credencial del entorno."""
    # FIX 4 — se usa logger en vez de print, y ya no se imprime el valor
    # real de la credencial.
    logger.info("Conectando a la base de datos")
    return True
