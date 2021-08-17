import math

comprimento = float(input("Comprimento(m): "))
largura = float(input("Largura(m): "))
altura = float(input("Altura(cm): "))

concreto = comprimento * largura * (altura / 100)

areia_pedra = math.ceil(concreto * 0.6)
cimento = math.ceil(concreto * 4.8)

print("Qtd total de areia", areia_pedra)
print("Qtd total de pedra", areia_pedra)
print("Qtd total de cimento", cimento)