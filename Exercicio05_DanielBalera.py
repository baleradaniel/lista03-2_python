"""
No comércio o conceito de margem bruta é uma porcentagem que é aplicada ao preço de custo para se obter o preço de venda. 
Uma loja tem como política comercial, aplicar uma margem bruta de 45%, quando o peço de custo é <= R$100,00. 
Se o produto custa mais que isso, a margem de lucro é 35%.
Escreva um programa que leia o preço do produto e mostre seu preço de venda. 
"""

preco = float(input('Insira o preço do produto: '))

if preco <= 100:
    aplicacao = preco + preco*0.45
    print('O preço de venda do produto é {:10f}'.format(aplicacao))
else:
    aplicacao = preco + preco*0.35
    print('O preço de venda do produto é {:1f}'.format(aplicacao))

print('Daniel Balera')
