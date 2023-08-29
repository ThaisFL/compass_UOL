# DESAFIO 1 - operadores aritmeticos
"""
Calcule o percentual das despesas em relaçao ao salario:
salario = 3456.45
despesas = 2456.2

salario = 3450.45 
despesas = 2456.2 

percentual = despesas / salario * 100
"""
#DESAFIO 2 - operadores logicos
#%%
trabalho_terça = True
trabalho_quinta = False

tv_50 = trabalho_terça and trabalho_quinta 

tv_32 = trabalho_terça != trabalho_quinta

sorvete = trabalho_terça  or  trabalho_quinta

saude = not sorvete

print ('tv50={}  tv32={}  sorvete ={}  saudavel={}' 
       .format (tv_50, tv_32, sorvete, saude))

# %%
