#pegar 3 numeros e mostrar o maior
a=int(input("digite o primeiro numero: "))
b=int(input("digite o segundo numero: "))
c=int(input("digite o terceiro numero: "))
if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)