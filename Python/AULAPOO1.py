n1= float (input('Digite a primeira nota'))
n2= float (input('Digite a segunda nota'))
nome= input('Digite o nome do aluno')
media = (n1+n2)/2

if media >=7:
    print('aluno',nome,'teve a media', media, 'e foi aprovado')

else:
    print('aluno',nome,'teve a media', media, 'e foi reprovado')