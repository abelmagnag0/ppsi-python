import math

concreto = int(input("Concreto a ser feito (em m³): "))

areia_pedra = math.ceil(concreto * 0.6)
cimento = math.ceil(concreto * 4.8)

print("Qtd total de areia", areia_pedra)
print("Qtd total de pedra", areia_pedra)
print("Qtd total de cimento", cimento)