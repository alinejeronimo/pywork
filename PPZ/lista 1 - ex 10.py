#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias perdidos.

a = int(input("quantos cigarros voce fuma por dia?\n"))
b = int(input("por quantos anos voce ja fumou?\n"))
diasp = a * 1/144
total = diasp * b
print("voce ja perdeu ", "%0.2f" % total, " dias de vida!\n")
