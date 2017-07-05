a = int(input("insira o primeiro numero: "))
b = int(input("insira o segundo numero: "))
r = a % b
if (r==0):
   print("o mdc é: %d " % b)
elif (r != 0):
    r1 =  b % r
    if(r1 ==0):
      print("o mdc é: %d " % r)
elif (r1 !=0): 
    r3 = r1 % r2
    if (r3 == 0):
      print("o mdc é %d " % r2)