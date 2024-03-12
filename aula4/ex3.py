while True :
    n1= int (input('Digite um número'))
    n2= int (input('Digite outro número'))
    op= (input('Digite um operador'))

    if op == "+" :
        som = n1 + n2
        print('A soma desses números é:',som)

    elif op == "-" :
        sub = n1 - n2
        print('A subtração desses números é:',sub)

    elif op == "*" or op =="x":
        mult = n1 * n2
        print('A multiplicção desses números é:',mult)

    elif op == "/" :
        div = n1 / n2
        print('A divisão desses números é:',div)

    else :
        print('Operador desconhecido!')

    resp = (input('Você deseja continuar (sim ou não)'))
    if resp == "não":
        break