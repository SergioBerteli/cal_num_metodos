from sympy import Symbol, limit, sympify, rootof, diff
from sympy.polys.polyerrors import PolynomialError
from sympy.core.sympify import Basic
from sympy.core.function import Derivative
from math import floor
from tabulate import tabulate


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


def dif_central_3_pontos_y(yi_minus_1: float, yi: float, yi_plus_1: float) -> float:
    return (yi_minus_1 - 2 * yi + yi_plus_1)/h**2


def dif_progressiva_3_pontos_y(yi: float, yi_plus_1: float, yi_plus_2: float) -> float:
    return (yi - 2 * yi_plus_1 + yi_plus_2)/h**2


def dif_regressiva_3_pontos_y(yi_minus_2: float, yi_minus_1: float, yi: float) -> float:
    return (yi_minus_2 - 2 * yi_minus_1 + yi)/h**2


if __name__ == "__main__":
    x = Symbol('x')
    a, b, c = list(map(float, (input("Insira os 3 pontos da função: ").split(','))))
    h: float = abs(a - b)
    if (opt := input("1 - Valores de f(x)\n2 - Função f(x)\n")) == "1":
        fa, fb, fc = list(map(float, (input("Insira os 3 valores de f(x): ").split(','))))
        if (opt := input("1 - Progressiva\n2 - Regressiva\n3 - Central\n")) == "1":
            res = dif_progressiva_3_pontos_y(a, b, c, fa, fb, fc)
        elif opt == "2":
            res = dif_regressiva_3_pontos_y(a, b, c, fa, fb, fc)
        elif opt == "3":
            res = dif_central_3_pontos_y(a, b, c, fa, fb, fc)
    elif opt == "2":
        func: Basic = sympify(input("Insira a funcao: "))
        expression_diff: Derivative = diff(diff(func, x), x)
        if (opt := input("1 - Progressiva\n2 - Regressiva\n3 - Central\n")) == "1":
            res = dif_progressiva_3_pontos(a, b, c)
        elif opt == "2":
            res = dif_regressiva_3_pontos(a, b, c)
        elif opt == "3":
            res = dif_central_3_pontos(a, b, c)
        print(f'Derivada da função: {expression_diff}')
        print(f'Solução analítica: {insere_valor_na_derivada(b)}')
    print(f'Solução numérica: {res}')