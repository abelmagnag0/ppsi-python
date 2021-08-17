import math

comodo_comprimento = float(input("Comprimento(m) do cômodo: "))
comodo_largura = float(input("Largura(m) do cômodo: "))
area_comodo = comodo_comprimento * comodo_largura

print("------------------------------")

piso_comprimento = float(input("Comprimento(cm) do piso: "))
piso_largura = float(input("Largura(cm) do piso: "))
area_piso = piso_comprimento * piso_largura / 10000

qtd_pisos = math.ceil(area_comodo / area_piso)
print("Serão necessários", qtd_pisos, "peças de piso para revestir todo o chão do cômodo.")
