'''
Para utilizarmos as funções criadas em outros 
arquivos de código fonte devemos impota-las
para isso utilizamos o comando import ou from import

Ex1: Importar as funções do arqivo funcoes 
'''
import funcoes

base= float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))

area = funcoes.caucularAreaTriangulo (base, altura)
print (area)