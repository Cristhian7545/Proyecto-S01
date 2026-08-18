def suma(a, b):
    """Calcula la suma de dos números."""
    return a + b


def resta(a, b):
    """Calcula la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Calcula la multiplicación de dos números."""
    return a * b


def division(a, b):
    """Calcula la división de dos números."""
    return a / b


if __name__ == "__main__":
    print("=== CALCULADORA SIMPLE ===")

    resultado_suma = suma(10, 5)
    resultado_resta = resta(10, 5)
    resultado_multiplicacion = multiplicacion(10, 5)
    resultado_division = division(10, 5)

    print(f"Suma (10 + 5): {resultado_suma}")
    print(f"Resta (10 - 5): {resultado_resta}")
    print(f"Multiplicación (10 * 5): {resultado_multiplicacion}")
    print(f"División (10 / 5): {resultado_division}")