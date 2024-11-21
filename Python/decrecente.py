n1= float (input('Digite um numero: '))
n2= float (input('Digite um numero: '))
n3= float (input('digite um numero: '))

if n1>n2 and n1>n3 and n2>n3:
    print(n1 , n2 , n3)
elif n2>n1 and n2> n3 and n1>n3:
    print(n2 , n1 , n3)
elif n3>n1 and n3>n2 and n1>n2:
    print(n3 , n1 , n2)

