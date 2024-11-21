n = int(input('quantas pessoas para cadastros: '))
listaNome = []

for i in range(n):
    nome = input('nome: ')
    idade = int(input('idade: '))
    nova = [nome,idade]
    listaNome.append(nova)

for j in listaNome: 
    print(f'Bem vindo {j[0]} tem {j[1]} anos.')

    if (j[1] >= 18):
        print(f'{j[0]} é maior de idade')
    else:
        print(f'{j[0]} é menor de idade')

##print(listaNome)