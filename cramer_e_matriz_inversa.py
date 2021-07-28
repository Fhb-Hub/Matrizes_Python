from funcoes import *

def metodo_da_matriz_inversa():
    ordem = int(input("Informe a matriz de coeficiente. \n Informar o tamanho da matriz:"))
    print("Digite a matriz (separe os elememtos da linha por espaço):")
    matriz_coeficiente = ler_matriz(ordem)

    print("Digite os termos independentes separados por enter: ")
    t_independente =  ler_matriz(ordem)

    det_coeficiente = det_matriz(matriz_coeficiente)
    soma_t_independente = soma_itens(t_independente)

    if det_coeficiente == 0 and soma_t_independente!=0:
        print("Sistema impossível (SI)")
    elif det_coeficiente ==0 and soma_t_independente==0:
        print ("Sistema possível indeterminado (SPI)")
    else:
        print("Sistema possível determinado (SPD)")
        resultado = matriz_mult(matriz_inversa(matriz_coeficiente),t_independente)

        print(resultado)

def soma_itens(matriz):
    soma = 0
    for linha in matriz:
        for item in linha:
            soma += item
    return soma

def metodo_de_cramer():
    # Criação das matriz de coeficiente
    ordem = int(input("Informe a matriz de coeficiente. \n Informar o tamanho da matriz:"))
    print("Digite a matriz (separe os elememtos da linha por espaço):")
    matriz_coeficiente = ler_matriz(ordem)

    print("Digite os termos independentes separados por espaço: ")
    t_independente =  ler_matriz(1)[0]

    det_coeficiente = det_matriz(matriz_coeficiente)
    soma_t_independente = sum(t_independente)

    if det_coeficiente == 0 and soma_t_independente!=0:
        print("Sistema impossível (SI)")
    elif det_coeficiente ==0 and soma_t_independente==0:
        print ("Sistema possível indeterminado (SPI)")
    else:
        print("Sistema possível determinado (SPD)")
        matriz_result = [0]*ordem
        for coluna in range (ordem):
            m_copia = matriz_copia(matriz_coeficiente)
            for linha in range (ordem):
                m_copia[linha][coluna] = t_independente[linha]
            det_cp = det_matriz(m_copia)
            matriz_result [coluna] = det_cp / det_coeficiente
        print(matriz_result)