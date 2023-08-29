#!/usr/local/bin/python3

## __EXERCICIO 1__ 

from datetime import datetime

ano_atual = datetime.now().year

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

ano_100 = ano_atual + (100 - idade)

print(ano_100)


## __EXERCICIO 2__

for numeros in range(3):
    numero = int(input('Digite um numero:'))
    
    if numero % 2 == 0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')


## __EXERCICIOS 3__

for par in range(0 , 21):
    if par % 2 == 0:
        print(par)


## __EXERCICIO 4__

for primo in range(2 , 100):
    if primo == 2 or primo == 3 or primo == 5 or primo == 7:
        print(primo)
        
    elif primo % 2 != 0 and primo % 3 != 0 and primo % 5 != 0 and primo % 7 != 0:
        print(primo)

## __EXERCICIO 5__

dia = 22
mes = 10
ano = 2022

print(f'{dia}/{mes}/{ano}')


