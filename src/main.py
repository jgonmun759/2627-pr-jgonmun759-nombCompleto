def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea un nombre completo en una sola cadena, con cada primera letra en mayúscula.

    :param nombre: el nombre
    :param apellido1: primer apellido
    :param apellido2: segundo apellido

    :returns: cadena formateada
    """

    return f"{nombre.title().strip()} {apellido1.title().strip()} {apellido2.title().strip()}"


def main():
    nombre = input("Introduce tu nombre: ")
    apellido1 = input("Introduce tu primer apellido: ")
    apellido2 = input("Introduce tu segundo apellido: ")

    nombre_formateado = formatear_nombre(nombre, apellido1, apellido2)
    print("\n", nombre_formateado)


if __name__ == "__main__":
    main()