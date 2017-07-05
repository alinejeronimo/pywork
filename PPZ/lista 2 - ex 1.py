
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if (a > b+c) or (b > a+c) or (c > a+b):
    print("erro, valor invalido!")  
elif (a==b==c):
       print("Triangulo equilatero")       
elif  (a==b) or (a==c) or (b==c):
        print("Triangulo isoceles")
else:
    print("Triangulo escaleno")
