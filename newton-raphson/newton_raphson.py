from tabulate import tabulate
from sympy import Symbol, limit, sympify, rootof, diff
from math import floor

if __name__ == '__main__':
    x = Symbol('x')
    expressao = sympify(input("Insira a funcao: "))
    expressao_diff = diff(expressao, x)


def insere_valor_na_func(func, valor: float) -> float:
    return limit(func, x, valor)


def monta_dict(xi):
    line = dict()
    fx = insere_valor_na_func(expressao, xi)
    fx_linha = insere_valor_na_func(expressao_diff, xi)
    xi_plus_1 = xi - fx/fx_linha
    line['xi'] = xi
    line['f(x)'] = fx
    line['f\'(x)'] = fx_linha
    line['xi_plus_1'] = xi_plus_1
    line['error'] = (abs(xi_plus_1 - xi) / abs(xi_plus_1)) * 100
    return line


def newton_rapson(xi, tol_error):
    tentativas = list()
    error = None
    while error is None or error > tol_error:
        line = monta_dict(xi)
        tentativas.append(line)
        error = line['error']
        xi = line['xi_plus_1']
    table = list()
    for value in tentativas:
        linha = list()
        for key, element in value.items():
            linha.append(element)
        table.append(linha)
    head = ['xi', 'f(x)', 'f\'(x)', 'xi_plus_1', 'error']
    tabela_final = tabulate(table, headers=head, tablefmt="grid")

    res_final = tentativas[-1]['xi_plus_1']

    return tabela_final, float(res_final)


def pega_intervalo():
    raiz = rootof(expressao, 0)
    return floor(raiz)


if __name__ == '__main__':
    x_ini = pega_intervalo()
    erro_t = float(input('Insira o erro desejado em porcentagem: '))
    print(newton_rapson(x_ini, erro_t)[0])
    print(newton_rapson(x_ini, erro_t)[1])
