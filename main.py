def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros: "))


imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

    
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com o peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
