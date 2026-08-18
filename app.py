"""Módulo de la Calculadora Simple para el pipeline CI/CD."""


def suma(a: float, b: float) -> float:
    """Calcula la suma de dos números."""
    return a + b


def resta(a: float, b: float) -> float:
    """Calcula la resta de dos números."""
    return a - b


def multiplicacion(a: float, b: float) -> float:
    """Calcula la multiplicación de dos números."""
    return a * b


def division(a: float, b: float) -> float:
    """Calcula la división de dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def obtener_mensaje_bienvenida(nombre: str = "Equipo DevOps") -> str:
    """Retorna un mensaje de bienvenida personalizado."""
    return f"¡Hola, {nombre}! Bienvenido a la Calculadora CI/CD."


if __name__ == "__main__":
    print("=" * 35)
    print(obtener_mensaje_bienvenida())
    print("=" * 35)

    print(f"Suma (10 + 5): {suma(10, 5)}")
    print(f"Resta (10 - 5): {resta(10, 5)}")
    print(f"Multiplicación (10 * 5): {multiplicacion(10, 5)}")
    print(f"División (10 / 5): {division(10, 5)}")