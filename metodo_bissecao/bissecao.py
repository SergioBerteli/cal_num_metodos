from tabulate import tabulate
from sympy import Symbol, limit, sympify, rootof
from sympy.polys.polyerrors import PolynomialError
from sympy.core.sympify import Basic
from math import ceil, floor


def insere_valor_na_func(valor: int) -> float:
    return limit(expressao, x, valor)


def monta_dict(a, b, c, error=None):
    line = dict()
    line['a'] = a
    line['b'] = b
    line['c'] = c
    line['fa'] = insere_valor_na_func(a)
    line['fb'] = insere_valor_na_func(b)
    line['fc'] = insere_valor_na_func(c)
    line['error'] = error
    return line


def bissecao(a, b, tol_error):
    tentativas = list()
    c = (a + b) / 2
    tentativas.append(monta_dict(a, b, c, insere_valor_na_func))
    error = None
    while error is None or error > tol_error:
        if insere_valor_na_func(c) > 0:
            dif_a = 0 - insere_valor_na_func(a)
            dif_b = 0 - insere_valor_na_func(b)
        else:
            dif_a = 0 + insere_valor_na_func(a)
            dif_b = 0 + insere_valor_na_func(b)
        if dif_a > dif_b:
            b = c
        else:
            a = c
        novo_c = (a + b) / 2
        error = (abs(novo_c - c) / abs(novo_c)) * 100
        c = novo_c
        tentativas.append(monta_dict(a, b, c, error))

    table = list()
    for value in tentativas:
        linha = list()
        for key, element in value.items():
            linha.append(element)
        table.append(linha)
    head = ['a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'Erro']
    tabela_final = tabulate(table, headers=head, tablefmt="grid")
    valores = [tentativas[-1]['a'], tentativas[-1]['b'], tentativas[-1]['c']]
    func_valor = list(map(insere_valor_na_func, valores))
    func_valor = list(map(abs, func_valor))
    ultima_linha = zip(valores, func_valor)
    res_final = min(ultima_linha, key=lambda element: element[1])

    return tabela_final, res_final[0]


def pega_intervalo(expr):
    raiz = rootof(expr, 0)
    return floor(raiz), ceil(raiz)


if __name__ == '__main__':
    x = Symbol('x')
    expressao: Basic = sympify(input("Insira a funcao: "))
    erro_t = float(input('Insira o erro desejado em porcentagem: '))
    try:
        a, b = pega_intervalo(expressao)
    except PolynomialError:
        a, b = -100, 100
        root_temp = bissecao(a, b, erro_t)[1]
        a, b = floor(root_temp), ceil(root_temp)
    print(bissecao(a, b, erro_t)[0])
    print(bissecao(a, b, erro_t)[1])

