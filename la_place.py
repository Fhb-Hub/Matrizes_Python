from funcoes import *

#Teorema de Laplace
def verifica_matriz(matriz):
    tam_linha = len(matriz) 
    for linha in range (tam_linha):
        tam_col = len(matriz[linha])
        if tam_linha != tam_col: 
            return False # se coluna diferente de linhas retorna falso
    return True

def imprimir_determinante(matriz):
    matriz_quadrada = verifica_matriz(matriz)
    if matriz_quadrada == True:
        det = det_matriz (matriz)
        print(f"Velor da determinante é: {det}") 
    else: 
        print("Matriz não é quadrada!")

def gerar_identidade (tam):
    result=[]
    for lin in range (tam):
        linha = []
        result.append(linha)
        for col in range (tam):
            if lin == col:
                linha.append (1)
            else:
                linha.append(0)
    return result