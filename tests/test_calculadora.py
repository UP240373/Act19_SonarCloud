import pytest
from pages.calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    es_par,
    promedio,
    numero_mayor,
)


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_es_par():
    assert es_par(4) is True
    assert es_par(7) is False


def test_promedio():
    assert promedio([1, 2, 3, 4]) == 2.5


def test_promedio_lista_vacia():
    with pytest.raises(ValueError):
        promedio([])


def test_numero_mayor():
    assert numero_mayor(3, 7) == 7
    assert numero_mayor(7, 3) == 7
    assert numero_mayor(5, 5) == 5
