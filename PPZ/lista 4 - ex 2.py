import random
numimpar = []
numpar = []
i = 0
for i in range(20):
    i +=  1
    num = random.choice(range(100))
    if (num % 2 == 0):
        numpar.append(num)
    else:
        numimpar.append(num)
numpar.sort()
numimpar.sort()
print("lista dos numeros primos: ", numpar, "\nlista dos numeros impares: " , numimpar)
    
