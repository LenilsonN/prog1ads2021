import math

kmi = float(input("Kilometro Incial: "))
kmf = float(input("Kilometro Final: "))
litros_g = float(input("Litros Gastos: "))
kmt = kmf-kmi
lpk = litros_g/kmt
print("Litros por Kilometro: {}".format(math.ceil(lpk)))
