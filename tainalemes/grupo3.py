while True :
    preco = int(input ('Digite o preço do produto adquirido.(Digite = para obter o resultado da soma) \n'))
    soma = soma + preco 
    if preco == "=" :
        print (soma)
        break
    