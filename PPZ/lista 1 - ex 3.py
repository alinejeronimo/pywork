h = int(input("Digite as horas: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os  segundos: "))
total = (h*3600) + (m*60) + s
print("%.2f" % total, "s")
