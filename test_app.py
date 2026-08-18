import pytest
from app import (
    division,
    multiplicacion,
    obtener_mensaje_bienvenida,
    resta,
    suma,
)


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0


def test_resta():
    assert resta(5, 3) == 2
    assert resta(10, 20) == -10


def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(5, 0) == 0


def test_division():
    assert division(6, 3) == 2.0


def test_division_por_cero():
    """Valida que la división por cero lance una excepción adecuada."""
    with pytest.raises(ValueError, match="No se puede dividir entre cero."):
        division(10, 0)


def test_mensaje_bienvenida():
    assert "DevOps" in obtener_mensaje_bienvenida("DevOps")