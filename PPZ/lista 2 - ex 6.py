salbrut = float(input('digite o seu salário bruto: '))
ir = (salbrut/100)*11
inss = (salbrut/100)*8
sind = (salbrut/100)*5
salliq = salbrut - (ir + inss + sind)
print(' o seu salário líquido é de R$ %d' % salliq)
