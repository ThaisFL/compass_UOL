# Exercicios PYTHON I *1/2*

## __EXERCICIO 1__ 
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
```python
for par in range(0 , 21):
    if par % 2 == 0:
        print(par)
```
---
## __EXERCICIO 4__
```python
for primo in range(2 , 100):
    if primo == 2 or primo == 3 or primo == 5 or primo == 7:
        print(primo)
        
    elif primo % 2 != 0 and primo % 3 != 0 and primo % 5 != 0 and primo % 7 != 0:
        print(primo)
```
---
## __EXERCICIO 5__
```PYTHON
dia = 22
mes = 10
ano = 2022

print(f'{dia}/{mes}/{ano}')
```
---

# Exercicios PYTHON I *2/2*
## __EXERCICIO 6__
```PYTHON
conjunto_a = set([1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89])
conjunto_b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

interseccao = conjunto_a.intersection(conjunto_b)

lista_interseccao = list(interseccao)

print(lista_interseccao)
```
---
## __EXERCICIO 7__
```PYTHON
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lista_impar = []

for num in a:
    if num % 2 != 0:
        lista_impar = lista_impar + [num]

print(lista_impar)
```
---
## __EXERCICIO 8__
```PYTHON
lista_palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in lista_palavras:
    if palavra == palavra[::-1]:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')
```
## __EXERCICIO 9__ 
```PYTHON
# Você deve Utilizar a função enumerate().
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']

sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']

idades = [19, 28, 25, 31]

dados = zip(primeirosNomes, sobreNomes, idades)

for indice, (primeirosNomes, sobreNomes, idades) in enumerate(dados):
    print(f'{indice} - {primeirosNomes} {sobreNomes} está com {idades} anos')
```
---
## __EXERCICIO 10__
```PYTHON
lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista_nova = list(set(lista))

print(lista_nova)
```
---
## __EXERCICIO 11__
```PYTHON

with open('arquivo_texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo, end = "")
```
---
## __EXERCICIO 12__
```PYTHON
import json

with open('person.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)
```
---
## __EXERCICIO 13__
```PYTHON
def potencia (num):
    soma = num ** 2
    return soma
    
def my_map (list, f):                   #declaraçao funçao my_map.
    nova_lista = []                     #abrindo a lista que eu quero retornar depois.
    for elemento in list:               # O 'for' vai aplicar a funçao my_map a cada elemento da lista.
        soma = f(elemento)              
        nova_lista.append(soma)         
        
    # a funçao .append serve para adicionar um novo elemento a uma lista,no caso, o novo elemento sera a 'soma' que ira adicionar os novoselementos somados á nova_lista.
    return nova_lista
```
---
## __EXERCICIO 14__
```PYTHON
def parametro (*args, **kwargs):
    for arg in args:
        print(arg)
    
    for chave, valor in kwargs.items():
        print(valor)
        

parametro(1, 3, 4, 'hello',
parametro_nomeado='alguma coisa', x= 20)
```
---
## __EXERCICIO 15__
```PYTHON
class Lampada:
    def __init__(self, estado):
        self.ligada = estado
        self.desligada = not estado
    
    def liga(self):
        self.ligada = True
        self.desligada = False
        
    def desliga(self):
        self.ligada = False
        self.desligada = True
        
    def esta_ligada(self):
        return self.ligada
    
# ligando a Lampada     
instancia_lampada = Lampada(True)
instancia_lampada.liga()
#testando se esta ligada
print('A lâmpada está ligada?', instancia_lampada.esta_ligada())

#desligando
instancia_lampada.desliga()
print('A lâmpada ainda está ligada?', instancia_lampada.esta_ligada())
```
---
## __EXERCICIO 16__
```PYTHON
def soma(string):
    numeros_lista = string.split(",")
    
    numeros_inteiros = [int(numero) for numero in numeros_lista]
    soma = sum(numeros_inteiros)
    
    return soma

    
string = "1,3,4,6,10,76"

print(soma(string))
```
---
## __EXERCICIO 17__
```PYTHON
def dividir_lista(lista):
    tamanho_partes = len(lista) // 3
    partes = [lista[i : i + tamanho_partes] for i in range(0, len(lista), tamanho_partes)]
    return partes 
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
partes_divididas = dividir_lista(lista)
    
# gambiarra para fazer do jeito que o exercicio quer

for i, parte in enumerate(partes_divididas):
    if i == len(partes_divididas) - 1:
        print(parte, end = "\n")
    else:
        print(parte, end = " ")
```
---
## __EXERCICIO 18__
```PYTHON
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

lista = list(set(speed.values()))

print(lista)
```
---
## __EXERCICIO 19__
```PYTHON
import random
import statistics
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

media = sum(random_list) / len(random_list)
mediana = statistics.median(random_list)
valor_maximo = max(random_list)
valor_minimo = min(random_list)
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
```
---
## __EXERCICIO 20__
```PYTHON
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lista = []
    
for elemento in reversed(a):
    lista.append(elemento)
    
print(lista)
```
---
## __EXERCICIO 21__
```PYTHON
class Passaro: 
    def voar(self):
        print('Voando...')
        
    def emiti_som(self, som):
        print('{self.__class__.__name__} emitindo som...')
        print(som)
        
class Pato(Passaro):
    def emiti_som(self):
        som = 'Quack Quack'
        super().emiti_som(som)
       
 
class Pardal(Passaro):
    def emiti_som(self):
        som = 'Piu Piu'
        super().emiti_som(som)
       
pato = Pato()
pato.voar()
pato.emiti_som()

pardal = Pardal()
pardal.voar()
pardal.emiti_som()
```
---
## __EXERCICIO 22__
```PYTHON
class Pessoa:
    def __init__(self, identificacao):
        self.id = identificacao
        self.__nome = None  # Inicializando o atributo privado como vazio

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome



pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'  
print(pessoa.nome) 

```
---
## __EXERCICIO 23__
```PYTHON
class Calculo:
    def soma(self, x , y):
        return x + y
        
    def subtraçao(self, x, y):
        return x + y
        
 
 
x = 4 
y = 5    
calculo = Calculo()

somar_numeros = calculo.soma(x,y)
subtrair_numero = calculo.subtraçao(x,y)

print(f'Somando: {x}+{y} = {somar_numeros}')
print(f'Subtraindo: {x}-{y} = {subtrair_numero}')
```
---
## __EXERCICIO 24__
```PYTHON
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada            
    
    def ordenacaoCrescente(self):
        lista_crescente = sorted(self.listaBaguncada)
        return lista_crescente
        
    def ordenacaoDecrescente(self):
        lista_decrescente = sorted(self.listaBaguncada, reverse = True)
        return lista_decrescente


#objeto para lista crescente
lista1 = [3,4,2,1,5]     
crescente = Ordenadora(lista1)
Lista_Crescente = crescente.ordenacaoCrescente()


#objeto para lista decrescente
lista2 = [9,7,6,8]
decrescente = Ordenadora(lista2)
Lista_Decrescente = decrescente.ordenacaoDecrescente()

print(Lista_Crescente)
print(Lista_Decrescente)
```
---
## __EXERCICIO 25__
```PYTHON
class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade
        
        
tupla_aviao = [ 
        ('BOIENG456', '1500 km/h','400'),
        ('Embraer Praetor 600' , '863km/h', '14'),
        ('Antonov An-2', '258 Km/h', '12')
]

lista_avioes = []

for elementos in tupla_aviao:             
    modelo, velocidade_maxima, capacidade = elementos       #separar os elementos da tupla 'tupla_aviao'
    aviao = Aviao(modelo, velocidade_maxima, capacidade)
    lista_avioes.append(aviao)            #Adiciona o objeto 'aviao' à lista 'lista_avioes'
    
for i in lista_avioes:
    print(f'modelo {i.modelo}: velocidade maxima {i.velocidade_maxima}: capacidade para {i.capacidade} passageiros: Cor {i.cor}')
```
---