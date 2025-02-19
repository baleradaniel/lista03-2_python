"""
Nas eleições municipais, os munícipios com 200.000 eleitores ou mais, tem segundo turno caso o 1º colocado não tenha mais que 50% dos votos.
Escreva um programa que leia: O nome do munícipio, a quantidade de eleitores e a quantidade de votos do candidato mais votado. Informe se haverá segundo turno ou não.
"""

nome_municipio = input('Insira o nome do municipio: ')
qtde_eleitor = int(input('Insira a quantidade de eleitores: '))
qtde_voto = int(input('Insira a quantidade de votos do candidato mais votado: '))

if qtde_voto > qtde_eleitor/2:
    print('Não haverá um segundo turno.')
else:
    print('Haverá um segundo turno')