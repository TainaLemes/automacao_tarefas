#Estrutura de repetição 
"""Utilizando para repetir uma  instrução em um determinado
números de vezes"""
for x in range(1,5):
    nome = input('Digite o nome do aluno ')
    nota = float (input ('Digite a nota do aluno: '))
    if nota >= 6:
        print (nome, "foi aprovado, com nota ", nota)
    else :
        print (f"{nome} foi reprovado com nota {nota: .2f}")