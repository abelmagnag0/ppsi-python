mas = int(input("Quantidade de alunos do sexo masculino: "))
fem = int(input("Quantidade de alunos do sexo feminino: "))
aprovados = int(input("Quantidade de alunos aprovados nesta turma: "))

total = mas + fem
mas_percent = round((mas / total) * 100, 2)
fem_percent = round((fem / total) * 100, 2)
apr_percent = round((aprovados / total) * 100, 2)

print("-------------------------")
print("Total de alunos  ", total)
print("Percentual de alunos do sexo masculino  ", mas_percent, "%")
print("Percentual de alunos do sexo feminino  ", fem_percent, "%")
print("Percentual de alunos aprovados  ", apr_percent, "%")
