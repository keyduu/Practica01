import re
from validations import regex


def check_brand(brand):
    pattern = re.compile(regex.REGEX_BRAND)
    return pattern.match(brand) is not None


def check_model(model):
    pattern = re.compile(regex.REGEX_MODEL)
    return pattern.match(model) is not None

# Esta funcion quedara inservible cuando se ponga eun combo con los datos de la base de datos.
# def check_os(os):
#     pattern = re.compile(regex.REGEX_OS, re.I)
#     return pattern.match(os) is not None


def check_memory(memory):
    pattern = re.compile(regex.REGEX_MEMORY)
    if pattern.match(memory):
        number = int(memory)
        return number > 0
    return False  # Esto solo ocurre cuando no cumple que está formado por uno o más digitos.


def check_price(price):
    pattern = re.compile(regex.REGEX_PRICE)
    if pattern.match(price):  # si cumple el patron, se devuelve True si es mayor que 0 (no se considera que pueda tener precio 0)
        return float(price.replace(",",".")) > 0.0
    return False  # Si no cumple el patron de float, se devuelve False.
