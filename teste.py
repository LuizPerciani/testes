salario_bruto = float(input("Digite seu salário bruto mensal: "))

"\\Condição de VT"
while True:
    vale_transporte = input("Utiliza vale transporte?: ")

    if vale_transporte.lower() == "Sim":
        break
    elif vale_transporte.lower() == "Não":
        break
    else:
        print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")
        
if vale_transporte.lower() == "Sim":
    desconto_vt = salario_bruto * 0.06
    salario_liquido = salario_bruto - desconto_vt
    
else:
    salario_liquido = salario_bruto

"\\Cálculo de INSS"
if salario_bruto <= 1320.00:
    percentual = 0.075
elif salario_bruto <= 2571.29:
    percentual = 0.09
elif salario_bruto <= 3856.94:
    percentual = 0.12
elif salario_bruto <= 7507.49:
    percentual = 0.14
else:
    percentual = 0.14

inss = (salario_bruto * percentual)
    
"\\Cálculo de IRRF"   
    
if salario_bruto <= 2112.00:
    aliquota = 0
    deducao = 0
elif salario_bruto <= 2826.65:
    aliquota = 0.075
    deducao = 158.40
elif salario_bruto <= 3751.05:
    aliquota = 0.15
    deducao = 370.40
elif salario_bruto <= 4664.68:
    aliquota = 0.225
    deducao = 651.73
else:
    aliquota = 0.275
    deducao = 884.96

irrf = (salario_bruto * aliquota) - deducao
irrf_truncado = "{:.2f}".format(irrf)

"\\Cálculo de salário líquido"
    
salario_liquido = (salario_bruto - irrf - inss - desconto_vt)

print(" + Salário Bruto : R$ {:.2f}" .format (salario_bruto))
print(" - IRRF : R$ ", irrf_truncado)
print(" - INSS : R$ {:.2f}" .format (inss))
print(" - Vale transporte: R$ {:.2f}" .format (desconto_vt))
print(" = Salário Liquido : R$ {:.2f}" .format (salario_liquido))