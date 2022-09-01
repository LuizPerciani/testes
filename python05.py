valor_por_hora = float(input("Digite o quanto você ganha por hora: "))
quantidade_horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
quantidade_minutos_trabalhados = int(input("Digite o número de minutos trabalhados no mês (além das horas): "))

minutos_em_decimal = round(quantidade_minutos_trabalhados / 60, 2)

salario_bruto = round((quantidade_horas_trabalhadas + minutos_em_decimal) * valor_por_hora, 2)
ir = round(salario_bruto*11/100, 2)
inss = round(salario_bruto*8/100, 2)
sindicato = round(salario_bruto*5/100, 2)
salario_liquido = round(salario_bruto - ir - inss - sindicato, 2)

print(" + Salário Bruto : R$", salario_bruto)
print(" - IR (11%) : R$", ir)
print(" - INSS (8%) : R$", inss)
print(" - Sindicato (5%) : R$", sindicato)
print(" = Salário Liquido : R$", salario_liquido)


