vitorias = int(input("Vitórias: "))
empates = int(input("Empates: "))
derrotas = int(input("Derrotas: "))

jogos = vitorias + derrotas + empates

pontos_disputados = jogos * 3
pontos_ganhos = (vitorias * 3) + empates
pontos_perdidos = pontos_disputados - pontos_ganhos

print("Jogos disputados pelo time:", jogos)
print("Total de pontos disputados:", pontos_disputados)
print("Total de pontos ganhos:", pontos_ganhos)
print("Total de pontos perdidos:", pontos_perdidos)

