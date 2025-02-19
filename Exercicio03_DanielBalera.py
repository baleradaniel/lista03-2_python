"""
Uma empresa financeira consegue empréstimo a pessoas físicas, quando o valor da parcela é menor que 8% do salário da pessoa. 
Escreva um programa que leia 2 números reais: O valor do salário e o valor da parcela.
E informe se o empréstimo será concedido ou não.
"""
salario = float(input('Insira o salario: '))
valor_parcela = float(input('Insira o valor da parcela: '))

if salario*0.08 > valor_parcela:
    print('Emprestimo concedido.')
else:
    print('Emprestimo não concedido')

print('Daniel Balera')