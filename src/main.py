def capitalizar_palabra(palabra: str) -> str:
    """
    Cambia la primera letra de una palabra a mayúscula y todas las demás a minúscula

    :param cadena: la palabra a convertir
    :return: la palabra convertida
    """

    return palabra[0].upper() + palabra[1:].lower()


def capitalizar(cadena: str) -> str:
    """
        Cambia la primera letra de cada palabra de una cadena a mayúscula y todas las demás a minúscula
    
        :param cadena: la cadena a convertir
        :return: la cadena convertida
    """
    
    lista_palabras = cadena.split()
    palabras_capitalizadas = [capitalizar_palabra(palabra) for palabra in lista_palabras]
    
    return " ".join(palabras_capitalizadas)


def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea un nombre completo en una sola cadena, con cada primera letra en mayúscula.

    :param nombre: el nombre
    :param apellido1: primer apellido
    :param apellido2: segundo apellido

    :return: cadena formateada
    """
    return capitalizar(f"{nombre} {apellido1} {apellido2}")


def main():
    nombre = str(input("Introduce tu nombre: "))
    apellido1 = str(input("Introduce tu primer apellido: "))
    apellido2 = str(input("Introduce tu segundo apellido: "))

    nombre_formateado = formatear_nombre(nombre, apellido1, apellido2)
    print("\n", nombre_formateado)


if __name__ == "__main__":
    main()