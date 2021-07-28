from funcoes import *
from cramer_e_matriz_inversa import *
from la_place import *

def exercicios_matriz():
    Matriz_A = [[2, 1], [-3, 4]]
    Matriz_B = [[0, -1], [2, 5]]
    Matriz_C = [[3, 0],[6, 1]]
    
    #Resposta questão 1#
    print(f"Resultado questão 1:\n {matriz_mult(Matriz_A, Matriz_B)}\n")
    
    #Resposta  2 (A+b) + (4*c)#
    r2 = somar(somar(Matriz_A, Matriz_B), mult_escalar(Matriz_C,4))
    print(f"Resultado questão 2:\n {r2}\n")

    #Resposta 3 [A+(B-Ct])*B-1]#
    r3 = subtrair(Matriz_B,transposta(Matriz_C))
    r3 = somar(Matriz_A,r3)
    r3 = matriz_mult(r3,matriz_inversa(Matriz_B))
    print(f"Resultado questão 3:\n {r3}\n")
  
    #Resposta 4 (A*A-1) = In#
    r4 = matriz_mult(Matriz_A,matriz_inversa(Matriz_A))
    print(f"Resultado questão 4:\n {r4}\n")
    print(f' Resultado Matriz inversa: \n{matriz_inversa(Matriz_A)}')

    #Resposta  (b + At * C-1 -Bt) = In#
    r5 = matriz_mult(transposta(Matriz_A), matriz_inversa(Matriz_C)) # At*C-1
    r5 = somar(Matriz_B,r5)
    r5 = subtrair(r5,transposta(Matriz_B))
    print (f"Resultado questão 5:\n {r5}\n")


def exercios_determinante():

    # lista_exercicios_matriz()
    #lista_exercicios_determinate()
    
    
     matriz = informar_matriz()
     imprimir_determinante(matriz)
     
     Matriz_A = [[1, -1, 0], [2, 3, 4],[0, 1, -2]]
     Matriz_B = [[2, 7, 2], [8, -1, -3],[-1, 9, 5]]

     det_a = det_matriz(Matriz_A)
     trans_a = transposta(Matriz_A)
     soma_b_at = somar(Matriz_B,trans_a)
     print(soma_b_at)
     final = mult_escalar(soma_b_at,det_a)
     print(f"Resultado questão 2:\n {final}")


def exercicios_laplace():
    #Questão A: informar matriz desejada.
    matriz = informar_matriz()
    print(f"matriz informada:\n {matriz}")

    #Questão B: Contenha uma função que faça uma verificação se com as matrizes digitadas é possível calcular os determinantes dessas matrizes;
    print("a função que determina o cofator é a função: verifica_matriz")

    #Questão C: Calcule o Co-fator dos elementos
    print("a função que determina o cofator é a função: co_fator")

    #Questão D: Contenha uma função que calcule os determinantes de matrizes de qualquer ordem;
    print("a função que determina o cofator é a função: det_matriz")

    #Questão E: Verificação de calculo da matriz.
    imprimir_determinante(matriz)

def cramer():
    print("Executando o metodo de Cramer\n")
    metodo_de_cramer()

def metodo_matriz_inversa():
    print("Executando o metodo da matriz inversa\n")
    metodo_da_matriz_inversa()

#Para vizualizar determinado exercicio basta descomentar o metodo desejado
if __name__ == '__main__':
#    exercicios_matriz()
#    exercios_determinante()
#    exercicios_laplace()
#    cramer()
#    metodo_matriz_inversa()
    print("\n\nProcesso Concluido. Para vizualizar outro exercicio basya descomentar o metodo desejado")