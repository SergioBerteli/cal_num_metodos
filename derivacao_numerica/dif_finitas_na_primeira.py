from sympy import sympify, limit, Symbol
from sympy.core.sympify import Basic

x = Symbol('x')

def valor_func():
    def recebe_metodo(metodo):
        def aplica_methodo(*args, **kwargs):
            fun: Basic = sympify(input("Insira a função: "))
            y: float = float(limit(fun, x, args[0]))
            y2: float = float(limit(fun, x, args[1]))
            return metodo(y, y2, args[1] - args[0])
        return aplica_methodo
    return recebe_metodo

@valor_func()
def dif_prog(y_i: float, y_iplus1: float, h: float):
    return (y_iplus1 - y_i)/h

@valor_func()
def dif_reg(y_iminus1: float, y_i: float, h: float):
    return (y_i - y_iminus1)/h

@valor_func()
def dif_cent(y_iminus1: float, y_iplus1: float, h: float):
    return (y_iplus1 - y_iminus1)/h

def main():
    opt = int(input("Escolha o metodo:\n1 - Dif. Progressiva\n2 - Dif. Regressiva\n3 - Dif Central\n"))
    if opt == 1:
        x_i, x_iplus1 = map(float, input("Insira o valor de x_i e de x_i+1: ").split(','))
        print(dif_prog(x_i, x_iplus1))
    elif opt == 2:
        x_i, x_iminus1 = map(float, input("Insira o valor de x_i e de x_i-1: ").split(','))
        print(dif_reg(x_i, x_iminus1))
    elif opt == 3:
        x_iplus1, x_iminus1 = map(float, input("Insira o valor de x_i+1 e de x_i-1: ").split(','))
        print(dif_cent(x_iminus1, x_iplus1))
    else:
        print("Opção inválida!")
        return

if __name__ == '__main__':
    main()
        