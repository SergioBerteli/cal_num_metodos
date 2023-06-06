from euler_simples import x, y, e, numero_de_euler, tabulate, Symbol, sympify, Basic, cos, sin



def euler_aprimodao(func: Basic, y_0: float, h: float, ponto_parada: float, sol_analitica: Basic = None) -> list[list]:
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
        temp_linha.append(var_indpendete)
        temp_linha.append(var_dependete)
        f_linha = func.subs([(x, var_indpendete), (y, var_dependete)])
        temp_linha.append(f_linha)
        k1 = h * f_linha
        temp_linha.append(k1)
        f_linha2 = func.subs([(x, var_indpendete + h), (y, var_dependete + k1)])
        temp_linha.append(f_linha2)
        k2 = h * f_linha2
        temp_linha.append(k2)
        if sol_analitica is not None:
            SE = sol_analitica.subs([(x, var_indpendete), (y, var_dependete), (e, numero_de_euler)]) # monta a expressão da SE
            temp_linha.append(SE)
            erro = abs(var_dependete - SE)
            temp_linha.append(erro)
        tabela.append(temp_linha)
        i += 1
        var_indpendete += h
        var_dependete += (k1 + k2)/2
    return tabela

def main():
    func: Basic = sympify(input('Insira a função: '))
    y_0 = float(input('Insira o valor de y(0): '))
    h: float = float(input('Insira o espaçamento de x: '))
    ponto_parada = float(input('Insira o ponto de parada: '))

    if (com_sol_analitica := int(input("Deseja incluir a solução analitica?\n1 - Sim\n2 - Não\n"))) == 1: 
        head = ['i', 'x_i', 'y_i', 'f\'(x_i, y_i)', 'k1', 'f\'(x_i+h, y_i+k1)', 'k2', 'S.E.', 'Erro']
        sol_analitica: Basic = sympify(input('Insira a solução analitica: '))
        res = euler_aprimodao(func, y_0, h, ponto_parada, sol_analitica)
    elif com_sol_analitica == 2:
        head = ['i', 'x_i', 'y_i', 'f\'(x_i, y_i)', 'k1', 'f\'(x_i+h, y_i+k1)', 'k2']
        res = euler_aprimodao(func, y_0, h, ponto_parada)
    else:
        print('Opção inválida')
        return False
    y_final = res[-1][2]
    tab = tabulate(res , headers=head)
    print(tab)
    print(f"y({ponto_parada}) = {float(y_final)}")
    return True

if __name__ == '__main__':
    main()