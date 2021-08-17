print("Calculadora de faturamento diário")

minigames = int(input("Mini-games vendidos: "))
calculadoras = int(input("Calculadoras vendidas: "))
canetas = int(input("Canetas vendidas: "))

faturamento_minigames = 6.95 * minigames
faturamento_calculadoras = 3.50 * calculadoras
faturamento_canetas = 1.20 * canetas

faturamento_total = faturamento_minigames + faturamento_calculadoras + faturamento_canetas

print("-----------------------------")
print("Lucro por produto:")
print("Mini-games   R$", faturamento_minigames)
print("Calculadoras   R$", faturamento_calculadoras)
print("Canetas   R$", faturamento_canetas)

print("-----------------------------")
print("Lucro total R$", faturamento_total)
