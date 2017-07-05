A = 80000
B = 200000
ano = 0
while (A<=B):
     A += A * 0.03
     B += B * 0.015
     ano =+ ano + 1
print("as populações serão iguais em %d anos" % ano)