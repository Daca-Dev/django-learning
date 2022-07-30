""" Funciones extra de la aplicación users """

import random
import string


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """ Generador de códigos aleatorio """
    return ''.join(random.choice(chars) for _ in range(size))
