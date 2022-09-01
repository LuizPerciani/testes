peso = float( input("Digite o seu peso (kg): "))
altura = float( input("Digite sua altura (m): "))
imc = peso/(altura*altura)
if imc <= 25.99:
 print("Normal = ", imc)
if (imc >= 26) and (imc <= 29.99):
    print("Sobrepeso = ", imc)
if (imc >= 30) and (imc <= 39.99):
    print("Obesidade = ", imc)
if imc >= 40:
    print("Obesidade grave = ", imc)
