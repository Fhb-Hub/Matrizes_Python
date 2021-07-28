#Função de soma entre duas matrizes
def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

#Função de subtração entre duas matrizes
def subtrair(a,b): 
    return somar(a,mult_escalar(b,-1))

def mult_escalar(matriz,escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

#Multiplicação entre matrizes
def matriz_mult(a, b):
    linhaA, colunaA = len(a), len(a[0])
    linhaB, colunaB = len(b), len(b[0])
    if colunaA != linhaB:
        print(f"Não é possível calcular a multiplicação. Matriz A tem {colunaA} colunas, matriz B tem {linhaB} linhas")
        return []

    r = []
    for i in range(linhaA):
        r.append([0] * colunaB)  # Adiciona uma linha nova e gera todas as colunas dessa linha
        for j in range(colunaB):
            for k in range(colunaA):  # pode usar também linhaB, já que nesse ponto elas são iguais
                r[i][j] += a[i][k] * b[k][j]
    return r


def matriz_nula(nlinhas, ncols):
    M = []
    for i in range(nlinhas):
        linha = [0]*ncols
        M.append(linha)
    return M

def transposta(M):
    nlinhas = len(M)  # Conta quantas linhas existem
    ncolunas = len(M[0])  # Conta quantos elementos têm em uma linha
    T = matriz_nula(ncolunas, nlinhas)
    for i in range(nlinhas):
        for j in range(ncolunas):
            T[j][i] = M[i][j]
    return T


def matriz_inversa(matriz):
    m_det = det_matriz(matriz)
    if m_det == 0:
        return []
    
    a = 1/m_det
    m_adjunta = gera_m_adjunta(matriz)
    result = mult_escalar(m_adjunta,a)
    return result


def gera_m_adjunta(matriz):
    matriz_cof = gera_m_cofator(matriz)
    result = transposta(matriz_cof) 
    return result


def gera_m_cofator(matriz):
    matriz_cof = [] # nova matriz com calculo do cofator
    tam = len(matriz)
    for l in range(tam):
        a = []  
        matriz_cof.append(a)
        for c in range(tam):
            cofator = co_fator(matriz,l,c)
            a.append(cofator)
    return matriz_cof   

def ler_matriz(ordem):
    matriz = []
    for i in range(ordem):
        linha_str = input()
        linha = []
        for i in linha_str.split():
            linha.append(float(i))
        matriz.append(linha)

    return matriz

def matriz_copia(m_origem):
    linha = len(m_origem)
    m_copia = []
    for l in range(linha):
        coluna = len(m_origem[l])
        m_copia.append([0] * coluna)
        for c in range(coluna):
            m_copia[l][c] = m_origem[l][c]

    return m_copia

def informar_matriz():
    m = int (input ("Digite a quantidade de itens das linhas:")) 
    n = int (input ("Digite a quantidade de itens das colunas"))    
    matriz=[]
    for i in range (m): #varrendo os itens da linha 
        matriz.append([0]*n) #cria a linha corrente mais as colunas
        for j in range (n): #varrendo as colunas
            matriz[i][j] = int (input (f"Digite o valor do elemento {i+1},{j+1}: ")) #pedindo as valores da matriz e atribuindo na posição correta
    return matriz


"""
    matriz: matriz original 
    linha: linha do pivo 
    col: coluna do pivo
"""
def cria_matriz_cofator(matriz, linha, col):
    tam = len(matriz) # lendo as quantidades de linha na matriz 
    tam_nova = tam -1 
    matriz_nova = []
    l_nova = 0
    for l in range(tam): 
        if l != linha: # não consedera a linha aonde está o pivo
            matriz_nova.append([0]*tam_nova)
            c_nova = 0
            for c in range(tam):
                if c != col: # não considera a coluna aonde está o pivo
                    matriz_nova[l_nova][c_nova] = matriz[l][c] 
                    c_nova += 1
            l_nova += 1

    return matriz_nova


def co_fator(matriz,linha,col):
    cofator = 0
    mult = (-1)**(linha+col) # potencia do co-fator
    cofator = mult * det_matriz(cria_matriz_cofator(matriz, linha, col)) # calculo recursivo do co-fator
    return cofator

def det_matriz(matriz):
    tam = len(matriz)

    # condição de parada da recursão
    if tam == 1:
        return matriz[0][0]
    
    #inicio do calculo
    col = 0 # fixando coluna em 0
    soma = 0 
    for linha in range(tam): 
       item = matriz[linha][col] # pegando os elementos da coluna 0
       if item != 0:  #se o item igual a zero não realiza o calculo
           soma += item * co_fator(matriz,linha,col) # calculo recursivo do co-fator

    return soma

