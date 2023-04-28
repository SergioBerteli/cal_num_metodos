from sympy import Symbol, limit, sympify, rootof, diff
from sympy.polys.polyerrors import PolynomialError
from sympy.core.sympify import Basic
from sympy.core.function import Derivative
from math import floor
from tabulate import tabulate


def insere_valor_na_func(func: Basic | Derivative, valor: float) -> float:
    return float(limit(func, x, valor))


def monta_dict(xi: float | int) -> dict:
    """
    Cria dicionário
    :param xi:
    :return:
    """
    line: dict = dict()
    fx: float | int = insere_valor_na_func(expression, xi)
    fx_linha: float | int = insere_valor_na_func(expression_diff, xi)
    xi_plus_1: float | int = xi - fx / fx_linha
    line['xi'] = xi
    line['f(x)'] = fx
    line['f\'(x)'] = fx_linha
    line['xi_plus_1'] = xi_plus_1
    line['error'] = (abs(xi_plus_1 - xi) / abs(xi_plus_1)) * 100
    return line


def newton_rapson(xi: int, tol_error: float) -> tuple:
    """
    Monta a tabela utilizando o metodo de newton rapson
    :param xi:
    :param tol_error:
    :return:
    """
    tentativas: list = list()
    error: float | None = None
    while error is None or error > tol_error:
        line: dict = monta_dict(xi)
        tentativas.append(line)
        error = line['error']
        xi = line['xi_plus_1']
    table: list = list()
    for value in tentativas:
        linha: list = list()
        for key, element in value.items():
            linha.append(element)
        table.append(linha)
    head: list = ['xi', 'f(x)', 'f\'(x)', 'xi_plus_1', 'error']
    tabela_final: str = tabulate(table, headers=head, tablefmt="grid")

    res_final: float = tentativas[-1]['xi_plus_1']

    return tabela_final, float(res_final)


def get_interval(expr) -> int:
    """
    Pegar o numero inteiro mais proximo da raiz arredondado para baixo
    :return: Numero inteiro mais proximo da raiz arredondado para baixo
    """
    raiz = rootof(expr, 0)
    return floor(raiz)


if __name__ == '__main__':
    x = Symbol('x')
    expression: Basic = sympify(input("Insira a funcao: "))
    expression_diff: Derivative = diff(expression, x)
    erro_permitido: float = float(input('Insira o erro desejado em porcentagem: '))
    x_ini: int = 0
    try:
        x_ini = get_interval(expression)
    except PolynomialError:
        x_ini = floor(newton_rapson(x_ini, erro_permitido)[1])
    print(newton_rapson(x_ini, erro_permitido)[0])
    print(newton_rapson(x_ini, erro_permitido)[1])
