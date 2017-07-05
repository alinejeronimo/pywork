ano = int(input("Digite o ano: "))
if (ano % 4 == 0):
    print ('esse é um ano bissexto')
elif (ano % 400 == 0):
    print('esse é um ano bissexto')
else:
    print('esse nao é um ano bissexto')
