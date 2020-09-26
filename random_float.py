import random

def random_float(integer_min=0, integer_max=None , min_decimal=0, max_decimal=None):
    """
    integer_min: minimum integer number for integer side. by default it is 0
    integer_max: maximum integer number for integer side. by default it is integer_min + 1
    min_decimal: minimum decimal number for float side. by default it is 0
    max_decimal: maximum decimal number for float side. by default it is min_decimal + 1
    """
    if (max_decimal is None):
        max_decimal = min_decimal+1
    if (min_decimal > max_decimal):
        min_decimal, max_decimal = max_decimal, min_decimal
    if (integer_max is None): 
        integer_max = integer_min + 1
    if (integer_min > integer_max):
        integer_min, integer_max = integer_max, integer_min
    integer = random.randint(integer_min, integer_max)
    floatSide = (random.randint(10**min_decimal, 10**max_decimal))*(10**(-max_decimal))
    randFloat = integer + floatSide
    return randFloat


