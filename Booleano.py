from itertools import product

def numero_funcoes_booleanas(variaveis):
    return 2 ** variaveis

def funcao_booleana_tres_variaveis(a, b, c):
    return int(not (a or (b and c)))

def funcao_booleana_quatro_variaveis(a, b, c, d):
    return int(not ((a or b) and (c or d)))

def tabela_tres_variaveis():
    tabela_tres_var = []
    for a, b, c in product([0, 1], repeat=3):
        resultado = funcao_booleana_tres_variaveis(a, b, c)
        tabela_tres_var.append((a, b, c, resultado))
    print("Tabela de funções booleanas de três variáveis:")
    print("A | B | C | Resultado")
    for linha in tabela_tres_var:
        print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]}")

def tabela_quatro_variaveis():
    tabela_quatro_var = []
    for a, b, c, d in product([0, 1], repeat=4):
        resultado = funcao_booleana_quatro_variaveis(a, b, c, d)
        tabela_quatro_var.append((a, b, c, d, resultado))
    print("\nTabela de funções booleanas de quatro variáveis:")
    print("A | B | C | D | Resultado")
    for linha in tabela_quatro_var:
        print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]} | {linha[4]}")

opcao = input("Selecione a opção que deseja resolver:\n1. Calcular número de funções booleanas.\n2. Tabela de funções booleanas de três variáveis.\n3. Tabela de funções booleanas de quatro variáveis.\nDigite o número da opção: ")

if opcao == '1':
    num_variaveis = int(input("Digite o número de variáveis: "))
    num_funcoes = numero_funcoes_booleanas(num_variaveis)
    print(f"Número de funções booleanas com {num_variaveis} variáveis: {num_funcoes}")
elif opcao == '2':
    tabela_tres_variaveis()
elif opcao == '3':
    tabela_quatro_variaveis()
else:
    print("Opção inválida.")
