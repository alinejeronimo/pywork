dist = int(input("digite a distancia que voce vai percorrer em Km: \n"))
vm = int(input("digite a velocidade em KM/H: \n"))
t = dist/vm * 60
print("%0.2f" % t,"min", "eh o tempo estimado de duracao da viagem")
