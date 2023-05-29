from sympy import Symbol, limit, sympify, rootof, diff
from sympy.polys.polyerrors import PolynomialError
from sympy.core.sympify import Basic
from sympy.core.function import Derivative
from math import floor
from tabulate import tabulate


x = Symbol('x')
func: Basic = sympify(input("Insira a funcao: "))
a, b, c = list(map(float, (input("Insira os 3 pontos da função: ").split(','))) )
h: float = abs(a - b)
expression_diff: Derivative = diff(diff(func, x), x)


def insere_valor_na_func(valor: float) -> float:
    return float(limit(func, x, valor))


def insere_valor_na_derivada(valor: float) -> float:
    return float(limit(expression_diff, x, valor))


def dif_central_3_pontos(xi_minus_1: float, xi: float, xi_plus_1: float) -> float:
    f = insere_valor_na_func
    return (f(xi_minus_1) - 2 * f(xi) + f(xi_plus_1))/h**2


def dif_progressiva_3_pontos(xi: float, xi_plus_1: float, xi_plus_2: float) -> float:
    f = insere_valor_na_func
    return (f(xi) - 2 * f(xi_plus_1) + f(xi_plus_2))/h**2


def dif_regressiva_3_pontos(xi_minus_2: float, xi_minus_1: float, xi: float) -> float:
    f = insere_valor_na_func
    return (f(xi_minus_2) - 2 * f(xi_minus_1) + f(xi))/h**2


if __name__ == "__main__":
    print(dif_central_3_pontos(a, b, c))
    print(insere_valor_na_derivada(b))
    