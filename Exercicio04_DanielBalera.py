"""
No SENAILÂNDIA mulheres e homens podem servir o exército do país. O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida.
 Existe uma única restrição para o ingresso, que é a idade da pessoa: 
•	Para mulheres, a idade aceita é entre 21 e 34 anos (>=21 e <=34)
•	Para homens, a idade aceita é entre 18 e 39 anos (>=18 e <=39)
Escreva um programa que leia 3 dados de entrada: Nome da pessoa, idade e gênero. Informe se a pessoa será aceita ou não para o serviço.
	OBS: Para o gênero deve ser lido somente um caractere, que pode ser: 'f' ou 'F', 'm' ou 'M'. Qualquer coisa diferente, deve ser informado como inválido.
"""

nome = input('Insira o seu nome: ')
idade = int(input('Insira a sua idade: '))
genero = input('Insira o seu gênero: ')

if genero == 'f' or 'F':
    if idade >= 21 and idade <= 34:
        print('Aceito para o serviço!')
    else:
        print('Não aceito para o serviço!')
else:
    print('Entrada de gênero inválida.')

if genero == 'm' or 'M':
    if idade >= 18 and idade <= 39:
        print('Aceito para o serviço!')
    else:
        print('Não aceito para o serviço!')
else:
    print('Entrada de gênero inválida.')

print('Daniel Balera')
    