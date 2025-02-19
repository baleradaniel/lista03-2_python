"""
Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de 2 dados fornecidos: O grau de aceitação de risco e o valor a ser investido.
Deve ser lido no teclado na forma BX ou AL risco. Se for fornecido algo diferente disso, o programa deve mostrar uma mensagem indicando que foi fornecido um dado inválido.
Para o valor, deve ser um número real.
Aceitação de risco:	    Valor < 1000,00:	Valor >= 1000,00:
        Baixo	            Poupança	        Renda Fixa
        Alto	            Bitcoins	        Ações
"""

grau_aceitacao = input('Insira o grau de aceitação de risco: ').upper()
valor = float(input('Insira o valor a ser investido: '))

if grau_aceitacao == 'BX' and valor < 1000:
    print('Aplicação financeira adequada: Poupança')

elif grau_aceitacao == 'BX' and valor >= 1000:
    print('Aplicação financeira adequada: Renda Fixa')

elif grau_aceitacao == 'AL' and valor < 1000:
    print('Aplicação financeira adequada: Bitcoins')

elif grau_aceitacao == 'AL' and valor >= 1000:
    print('Aplicação financeira adequada: Ações')

else:
    print('Dado inválido!')