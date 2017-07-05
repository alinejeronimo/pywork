peixes = int(input('Quantos quilos de peixe você pescou? '))
exc = peixes - 50
if (exc > 0):
    multa = exc * 4
    print("Você deve pagar R$ %d em multa." % multa)
else:
    multa = 0  
    exc = 0
    print("Você não precisará pagar multa. Pois multa = R$ %d e excesso = %d Kg " % (multa, exc))


