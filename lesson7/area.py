from math import sqrt


def rectangle_area(a: int | float, b: int | float) -> int | float:
    return a * b


def triangle_area(a: int | float, b: int | float, c: int | float) -> int | float:
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
