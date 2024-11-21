peso= float(input('Digite o seu Peso'))
altura = float(input('Digite a sua Altura'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso Normal')
elif imc > 25.1 and imc <= 30:
    print('Sobrepeso')
else:
    print('Obesidade')