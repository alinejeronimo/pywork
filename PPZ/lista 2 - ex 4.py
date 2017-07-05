a=int(input("digite o primeiro numero: "))
b=int(input("digite o segundo numero: "))
c=int(input("digite o terceiro numero: "))
if (a>b) and (a>c):
    print("O maior numero é %d" %a)
elif (b>a) and (b>c):
    print("O maior numero é %d" %b)
else:
    print("O maior numero é %d" %c)
