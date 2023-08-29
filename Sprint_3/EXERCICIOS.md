# Exercicios PYTHON I *1/2*

## __EXERCICIO 1__ 
> Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

```python 
from datetime import datetime

ano_atual = datetime.now().year

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

ano_100 = ano_atual + (100 - idade)

print(ano_100)
``` 
---
## __EXERCICIO 2__
> Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido). Importante: Aplique a função range() em seu código.

```python
for numeros in range(3):
    numero = int(input('Digite um numero:'))
    
    if numero % 2 == 0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')
```
---
## __EXERCICIOS 3__
> Escreva um código Python para imprimir os números pares de 0 até 20 (incluso). Importante: Aplique a função range() em seu código.
```python
for par in range(0 , 21):
    if par % 2 == 0:
        print(par)
```
---
## __EXERCICIO 4__
> Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.  Importante: Aplique a função range().

```python
for primo in range(2 , 100):
    if primo == 2 or primo == 3 or primo == 5 or primo == 7:
        print(primo)
        
    elif primo % 2 != 0 and primo % 3 != 0 and primo % 5 != 0 and primo % 7 != 0:
        print(primo)
```
---
## __EXERCICIO 5__
>Escreva um código Python que declara 3 variáveis:
> dia, inicializada com valor 22
> mes, inicializada com valor 10 e
> ano, inicializada com valor 2022
> Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.

```PYTHON
dia = 22
mes = 10
ano = 2022

print(f'{dia}/{mes}/{ano}')
```
---

# Exercicios PYTHON I *2/2*
## __EXERCICIO 6__
> Considere as duas listas abaixo:
>a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
>b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores >da interseção na saída padrão. Importante:  Esperamos que você utilize o construtor set() em seu código.