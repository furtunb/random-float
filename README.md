# random-float
If you want to get float and random number from Python, this is what you want


HOW TO USE

just use random_float() function


DIFFERENCES WITH random.uniform()

First of all in random.uniform() you need to give a, b values as an interval, but with random_float() you don't need to do that, you can give the integer interval(integer_min, integer_max) if you prefer to. Other difference is; with random_float() you can determine the length of the decimal side(min_decimal, max_decimal). 

SPECIFICATIONS

random_float uses integer_min, integer_max, min_decimal, max_decimal

integer_min: minimum integer number for integer side. by default it is 0

integer_max: maximum integer number for integer side. by default it is integer_min + 1

min_decimal: minimum decimal number for float side. by default it is 0

max_decimal: maximum decimal number for float side. by default it is min_decimal + 1 

