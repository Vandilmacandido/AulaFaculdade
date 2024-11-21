i = int(input("informe um numero inteiro: "))

a = float(input("informe o valor de a: "))

b = float(input("informe o valor de b: "))

c = float(input("informe o valor de c: "))

if i % 2 == 0:
     media = (a + b + c)/3
     print('media aritimetica é ', media)
elif i > 10:
     media = (a + b + c)/3
     print('media aritimetica é: ', media)
     ponderada = (a*2 + b*3 + c*4)/ (2+3+4)
     print("a media ponderada é", ponderada)
else:
     print("erro no sistema")
     