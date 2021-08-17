km_inicial = float(input("Quilometragem inicial do veículo: "))
km_final = float(input("Quilometragem final do veículo: "))
combustivel = float(input("Combustível consumido: "))

km_rodado = km_final - km_inicial

# 1 Litro = x km
km_porlitro = km_rodado / combustivel
# 1 km = x L
litro_porkm = combustivel / km_rodado

print("A média de quilômetros por litro de combustível é", km_porlitro)
print("A média combustível por quilômetro rodado é", litro_porkm)
