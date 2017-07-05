area = int(input(' digite a área a ser printada em m²: \n'))

if (area % 54 == 0):
    latas = area / 54
    total = latas * 80
else:
    latas = int(area/54)+1
    total = latas*80
print('serão necessários %d galões de tinta. e o preço é R$ %d ' % (latas, total))
