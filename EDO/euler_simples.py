from sympy import Symbol, sympify
from sympy.core.sympify import Basic
from tabulate import tabulate
from math import e as numero_de_euler, cos, sin

x = Symbol('x')
y = Symbol('y')
e = Symbol('e')
    

def euler_simples_com_SE(func: Basic, y_0: float, h: float, ponto_parada: float, sol_analitica: Basic) -> list[list]:
    """
    Calcula o valor de y(x), sendo x o ponto de parada
    """
    var_indpendete = 0
    i = 0
    var_dependete = y_0
    erro = None
    tabela = list()
    while var_indpendete <= ponto_parada:
        temp_linha = list()
        temp_linha.append(i) # Numero da iteração
        i += 1
        temp_linha.append(var_indpendete) # Xi
        f_linha = func.subs([(x, var_indpendete), (y, var_dependete)])
        temp_linha.append(var_dependete) # Yi
        SE = sol_analitica.subs([(x, var_indpendete), (y, var_dependete), (e, numero_de_euler)]) # monta a expressão da SE
        erro = var_dependete
        var_indpendete += h
        var_dependete = var_dependete + f_linha * h
        temp_linha.append(f_linha) # f linha
        temp_linha.append(SE) # S.E.
        temp_linha.append(abs(erro - SE)) # erro
        tabela.append(temp_linha)
    return tabela


def euler_simples(func: Basic, y_0: float, h: float, ponto_parada: float) -> list[list]:
    """
    Calcula o valor de y(x), sendo x o ponto de parada
    """
    var_indpendete = 0
    i = 0
    var_dependete = y_0
    tabela = list()
    while var_indpendete <= ponto_parada:
        temp_linha = list()
        temp_linha.append(i)
        i += 1
        temp_linha.append(var_indpendete)
        f_linha = func.subs([(x, var_indpendete), (y, var_dependete)])
        temp_linha.append(var_dependete)
        var_indpendete += h
        var_dependete = var_dependete + f_linha * h
        temp_linha.append(f_linha)
        tabela.append(temp_linha)
    return tabela
          

def main():
    func: Basic = sympify(input('Insira a função: '))
    y_0 = float(input('Insira o valor de y(0): '))
    h: float = float(input('Insira o espaçamento de x: '))
    ponto_parada = float(input('Insira o ponto de parada: '))
    
    if (com_sol_analitica := int(input("Deseja incluir a solução analitica?\n1 - Sim\n2 - Não\n"))) == 1: 
        head = ['i', 'x_i', 'y_i', 'f\'(x_i, y_i)', 'S.E.', 'Erro']
        sol_analitica: Basic = sympify(input('Insira a solução analitica: '))
        res = euler_simples_com_SE(func, y_0, h, ponto_parada, sol_analitica)
        
    elif com_sol_analitica == 2:
        head = ['i', 'x_i', 'y_i', 'f\'(x_i, y_i)']
        res = euler_simples(func, y_0, h, ponto_parada)
    else:
        print('Opção inválida')
        return False
    y_final = res[-1][2]
    tab = tabulate(res , headers=head)
    print(tab)
    print(f"y({ponto_parada}) = {y_final}") 
    return True


if __name__ == "__main__":
    main()