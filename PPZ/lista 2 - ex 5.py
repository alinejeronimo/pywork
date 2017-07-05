a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número: '))
if (a>b) and (b>c):
    print('o maior número é %d e o menor é %d' % (a,c))
elif (c>b) and (b>a):
    print('o maior número é %d e o menor número é %d' % (c,a))
elif (b>a) and (a>c):
    print('o maior número é %d e o menor número é %d' % (b,c))
elif (c>a) and (a>b):
    print('o maior número é %d e o menor número é %d' % (c,b))
elif (a>c) and (c>b):
    print('o maior número é %d e o menor número é %d' % (a,b))
elif (b>c) and (c>a):
    print('o maior número é %d e o menor número é %d' %  (b,a))
else:
    print('erro!')
