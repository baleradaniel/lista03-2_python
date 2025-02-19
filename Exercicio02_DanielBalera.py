"""
Escreva um programa para exibir na tela o nome e a categoria de um lutador, o programa deve ler uma string para o nome e um número real para o peso.
Conforme o peso, ocorrerá o enquadramento na categoria:
Peso:	Categoria:
<52	Inválido
>=52 e <65  | Peso Pena
>=65 e <72  | Peso Leve
>=72 e <79  | Peso Ligeiro
>=79 e <86  | Peso Meio-Médio
>=86 e <90  | Peso Médio
>=90 e <100 | Peso Meio-Pesado
>=100 	    | Peso Pesado
"""

nome = input('Insira o nome: ').capitalize()
peso = float(input('Insira o peso: '))

if peso < 52:
    print('Inválido.')

elif peso >= 52 and peso < 65:
    print(nome)
    print('Peso Pena.')

elif peso >= 65 and peso < 72:
    print(nome)
    print('Peso Leve.')

elif peso >= 72 and peso < 79:
    print(nome)
    print('Peso Ligeiro.')

elif peso >= 79 and peso < 86:
    print(nome)
    print('Peso Meio-Médio.')

elif peso >= 86 and peso < 90:
    print(nome)
    print('Peso Médio.')

elif peso >= 90 and peso < 100:
    print(nome)
    print('Peso Meio-Pesado.')

elif peso >= 100:
    print(nome)
    print('Peso Pesado.')

print('Daniel Balera')
