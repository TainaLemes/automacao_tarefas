'''
As funções são utilizadas para modularizar o código, ou seja,
dividi-lo em partes menores, que podem ser reutilizadas. 

Estrutura:
def nome_funcao (param1, param2)
    faz algo 
    return valor
    
Exemplos:
'''
#Função 1
def caucularAreaTriangulo (base, altura):
    area= (base*altura) / 2
    return area

#Função 2
def somar (n1, n2):
    resultado = n1 + n2
    return resultado

#Função 3 
def login (usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False
    
'''
chamar a função 
print (login ("Ivan, 123"))
area = caucularAreaTriangulo (100,50)
print('A área do triângulo é', area)
'''
