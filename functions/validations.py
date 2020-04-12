import re


def check_brand(brand: str) -> bool:
    pattern = re.compile(r"^\w+(\s\w+)*$")
    return pattern.match(brand) is not None


def check_model(model: str) -> bool:
    pattern = re.compile(r"^\w+(\s\w+)*$")
    return pattern.match(model) is not None


# Esta funcion quedara inservible cuando se ponga eun combo con los datos de la base de datos.
def check_os(os: str) -> bool:
    pattern = re.compile(r"^ios|android|windows phone|otro$", re.I)
    return pattern.match(os) is not None


def check_memory(memory: str) -> bool:
    pattern = re.compile(r"^\d+$")
    if pattern.match(memory):
        number = int(memory)
        return number > 0
    return False  # Esto solo ocurre cuando no cumple que está formado por uno o más digitos.


def check_price(price: str) -> bool:
    pattern = re.compile(r"^\d+(\.\d+)?$")
    if pattern.match(
            price):  # si cumple el patron, se devuelve True si es mayor que 0 (no se considera que pueda tener precio 0)
        return float(price) > 0.0
    return False  # Si no cumple el patron de float, se devuelve False.
