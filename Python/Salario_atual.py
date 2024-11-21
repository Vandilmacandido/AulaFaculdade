salario_atual= float(input('informe o salario do fucionario: '))

if salario_atual < 500:
    novo_salario = salario_atual * 1.15
elif salario_atual <= 1000:
    novo_salario = salario_atual * 1.10
else:
    novo_salario = salario_atual * 1.05

print( 'O novo salário reajustado é: R$ ', novo_salario )