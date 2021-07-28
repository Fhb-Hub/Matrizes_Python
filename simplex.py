import math
from fractions import Fraction

from funcoes import *
from la_place import *
from cramer_e_matriz_inversa import *

def def_entra_base(coeficientes_objetivo):
    lin = 0
    col = 0
    menor_elemento = coeficientes_objetivo[lin][col]
    tam_linha = len(coeficientes_objetivo)
    for l in range(tam_linha):
        tam_coluna = len(coeficientes_objetivo[l])
        for c in range(tam_coluna):
            atual = coeficientes_objetivo[l][c]
            if atual < menor_elemento:
                lin = l
                col = c
                menor_elemento = atual

    return lin, col


def def_sai_base(coeficiente_resticoes, termos_independentes, col_pivo):
    tam_linha = len(coeficiente_resticoes)
    valores = [0] * tam_linha
    for l in range(tam_linha):
        pivo = coeficiente_resticoes[l][col_pivo]
        ind = termos_independentes[l][0]
        if pivo > 0:
            valores[l] = ind / pivo
        else:
            valores[l] = math.inf

    ind = 0
    val = valores[ind]
    for i, v in enumerate(valores):
        if v < val:
            ind = i
            val = v

    return ind, val


def trocar_coluna(matriz_origem, coluna_deve_trocar, matriz_destino, coluna_vai_trocar):
    result = []
    for l in range(len(matriz_origem)):
        linha = []
        result.append(linha)
        for c in range(len(matriz_destino)):
            if c == coluna_deve_trocar:
                linha.append(matriz_destino[l][coluna_vai_trocar])
            else:
                linha.append(matriz_origem[l][c])

    return result


def informar_matriz_restricoes(x):
    n = int(input("Quantas restrições:"))
    matriz = []
    for i in range(x):  # varrendo os itens da linha
        matriz.append([0] * n)  # cria a linha corrente mais as colunas
        print(f"Informe os coeficientes para a restrição {i+1}")
        for j in range(n):  # varrendo as colunas
            matriz[i][j] = Fraction(input(f"x{j + 1}: "))  # pedindo as valores da matriz e atribuindo na posição correta
    return matriz, n


def informar_funcao_objetivo(m):
    print("Informe os coeficieentes da função objetivo: ")
    linha = []
    for i in range(m):  # varrendo os itens da linha
        valor = Fraction(input(f"x{i + 1}: "))  # pedindo as valores da matriz e atribuindo na posição correta
        linha.append(valor)
    matriz = []
    matriz.append(linha)
    return matriz


def informar_termos_independentes(n):
    print("Informe os termos independentes: ")
    linha = []
    for i in range(n):  # varrendo os itens da linha
        valor = Fraction(input())  # pedindo as valores da matriz e atribuindo na posição correta
        linha.append(valor)
    matriz = []
    matriz.append(linha)
    return matriz


def informar_funcao_max():
    print("A função objetivo é máximo ou de mínimo?")
    while (True):
        resposta = str(input("Digite max para máximo ou min para mínimo: ")).lower()
        if resposta == "max":
            return MAX
        elif resposta == "min":
            return MIN

    return matriz


def informar_completo():
    return bool(input("Programa deve imprimir todos os passos? Informa qualquer valor para Sim e vazio para Não."))


def print_variaveis_na_base(Xb, Rb):
    print(f"Variaveis da base:")
    for l in range(len(Rb)):
        for c in range(len(Rb[l])):
            print(f"{Xb[l][c]} = {Rb[l][c]}")


def print_solucao_otima(Z, tipo):
    tipo_s = "MAX" if tipo == MAX else "MIN"
    print(f"Solucao otima de {tipo_s} Z: {Z[0][0]}")


def print_variaveis_fora_base(X):
    print(f"Variaveis fora da base:")
    for l in range(len(X)):
        for c in range(len(X[l])):
            print(f"{X[l][c]} = 0")


def print_matriz(mensagem, matriz):
    print(mensagem, end=" ")
    print(matriz)


def print_modo_completo(iteracao, B, Bi, C1, Cb, Xb, completo):
    if completo:
        if iteracao == 0:
            print("Valor inicial das variáveis:")
        else:
            print(f"Valor das variáveis na iteração {iteracao}:")

        print_matriz("Variáveis na base: ", Xb)
        print_matriz("Matriz dos coeficientes das Variáveis: ", converter_para_decimal(B))
        print_matriz("B inversa: ", converter_para_decimal(Bi))
        print_matriz("Cb: ", converter_para_decimal(Cb))
        print_matriz("[Cb * Bi * A - C]:", converter_para_decimal(C1))
        print()


def print_resultados(Z, Xb, Rb, X, tipo):
    print_solucao_otima(Z, tipo)
    print_variaveis_na_base(Xb, Rb)
    print_variaveis_fora_base(X)
    print()


def exemplo_manual():
    m = int(input("Quantas variaveis de decisão tem o problema:"))
    C = informar_funcao_objetivo(m)  #
    A, n = informar_matriz_restricoes(m)
    b = informar_termos_independentes(n)
    tipo = informar_funcao_max()
    print_completo = informar_completo()
    return m, C, A, n, b, tipo, print_completo


def exemplo_aula():
    C = [[Fraction(1), Fraction(4), Fraction(2)]]
    m = len(C[0])
    A = [[Fraction(2), Fraction(2), Fraction(0)],
         [Fraction(1), Fraction(0), Fraction(3)],
         [Fraction(1), Fraction(1), Fraction(2)]]
    n = len(A)
    b = [[Fraction(20), Fraction(15), Fraction(40)]]
    return m, C, A, n, b, MAX, True


def exemplo_maximo_2_variaveis():
    C = [[Fraction(4), Fraction(1)]]
    m = len(C[0])
    A = [[Fraction(9), Fraction(1)],
         [Fraction(3), Fraction(1)]]
    n = len(A)
    b = [[Fraction(18), Fraction(12)]]
    return m, C, A, n, b, MAX, True


def exemplo_minimo():
    C = [[Fraction(2), Fraction(4), Fraction(-5)]]
    m = len(C[0])
    A = [[Fraction(1), Fraction(2), Fraction(10)],
         [Fraction(-1), Fraction(1), Fraction(-1)],
         [Fraction(2), Fraction(-1), Fraction(1)]]
    n = len(A)
    b = [[Fraction(600), Fraction(50), Fraction(100)]]
    return m, C, A, n, b, MIN, True


def verificar_valores_negativos(matriz):
    for l in matriz:
        for item in l:
            if item < 0:
                return True
    return False


def converter_para_decimal(matriz):
    result = []
    for l in range(len(matriz)):
        linha = []
        result.append(linha)
        for c in range(len(matriz[l])):
            linha.append(float(matriz[l][c]))

    return result


def inicializacao_simplex(C, b, m, n):
    b = transposta(b)
    X = transposta([[f'X{i}' for i in range(1, m + 1)]])
    Xb = transposta([[f'S{i}' for i in range(1, n + 1)]])
    B = gerar_identidade(n)
    Cb = [[0] * n]
    # Definir variaveis de base
    # Definir quem entra na base
    C1 = mult_escalar(C, -1)
    return B, C1, Cb, X, Xb, b


def simplex(m, C, A, n, b, tipo, completo=False):
    if tipo == MIN:
        C = mult_escalar(C, -1)

    B, C1, Cb, X, Xb, b = inicializacao_simplex(C, b, m, n)

    iteracao = 0
    print_modo_completo(iteracao, B, [[]], C1, Cb, Xb, completo)
    Z = [[0]]
    while verificar_valores_negativos(C1):
        l, entra = def_entra_base(C1)
        entra_na_base = transposta(X)[l][entra]
        # Definir quem sai da base
        sai, val = def_sai_base(A, b, entra)
        X[entra][0] = Xb[sai][0]
        Xb[sai][0] = entra_na_base
        B = trocar_coluna(
            # Bug
            B,
            sai,
            A,
            entra
        )
        Bi = matriz_inversa(B)
        Cb[0][sai] = C[0][entra]

        matriz_opera = matriz_mult(Cb, Bi)
        matriz_opera = matriz_mult(matriz_opera, A)
        matriz_opera = subtrair(matriz_opera, C)
        C1 = matriz_opera

        Rb = matriz_mult(Bi, b)
        Z = matriz_mult(Cb, Bi)
        Z = matriz_mult(Z, b)

        if tipo == MIN:
            Z = mult_escalar(Z, -1)

        iteracao += 1
        print_modo_completo(iteracao, B, Bi, C1, Cb, Xb, completo)

    if iteracao:
        print_resultados(Z, Xb, Rb, X, tipo)
    else:
        print("Não foi possível aplicar a otimização")

MAX = 1
MIN = 2

if __name__ == '__main__':
    m, C, A, n, b, tipo, completo = exemplo_manual()
    print()
    simplex(m, C, A, n, b, tipo, completo)