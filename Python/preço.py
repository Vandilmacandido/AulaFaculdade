P1= float (input('Digite o preço 1: '))
P2= float (input('Digite o preço 2: '))
P3= float (input ('Digiteo preço 3: '))

if P1 < P2 and P1 < P3:
    print('O preço 1 é o menor preço para comprar')
elif P2< P1 and P2 < P3:
    print('O preço 2 è o menor preço para comprar')
else:
    print('O preço 3 é o menor preço para comprar')