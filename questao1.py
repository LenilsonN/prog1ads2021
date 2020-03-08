preco_gas = input("Insira o preço da gasolina: ")
compra = input("Insira o quanto deseja gastar: ")
total = float(compra)/float(preco_gas)
print("O total de litros adquiridos é: {:.2f}".format(total))