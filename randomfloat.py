import random

def random_float(integer_min=0, integer_max=None , min_decimal=0, max_decimal=None):
    """
    integer_min: 
    integer_max
    min_decimal
    max_decimal
    """
    if (max_decimal == None) or (min_decimal > max_decimal):
        max_decimal = min_decimal+1
    if (integer_max == None) or (integer_min > integer_max):
        integer_max = integer_min + 1
    integer = random.randint(integer_min, integer_max)
    floatSide = (random.randint(10**min_decimal, 10**max_decimal))*(10**(-max_decimal))
    randFloat = integer + floatSide
    return randFloat


