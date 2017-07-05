def poligono(a):
    if (a == 3):
        print('é um triangulo')
    elif (a == 4):
        print('é um quadrado')
    elif (a==5):
        print('é um pentágono')
    elif (a==6):
        print('é um hexágono' )
    elif (a==8):
        print ('é um octágono')
    elif (a ==9):
        print ('é um eneágono')
    elif (a==10):
        print('é um decágono')
    else:
        print('valor inválido')

    return a
a = int(input("Digite o numero de lados do polígono regular: "))
b = poligono(a)


