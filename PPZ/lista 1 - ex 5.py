valor = int(input("insira o valor da mercadoria: \n"))
desc = int(input("digite a quantidade de desconto em %: \n"))
total = valor - valor/100*desc
print ("o valor do produto com desconto eh: \n", total)
