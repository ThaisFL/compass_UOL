# OPERADORES TERNARIOS

#%%
esta_chovendo = True 
if esta_chovendo == True:
   print('Hoje minhas roupas estao molhadas.')
else:
    print('Hoje minhas roupas estao secas')

# %%
esta_chovendo = True

print('Hoje minhas roupas estao ' + ('molhadas.' if esta_chovendo else 'secas.'))



#OPERADOR DE MEMBRO
#%%

lista = [1, 2, 3, 'Ana', 'Carla']

#%%
2 in lista
# %%
'Ana' not in lista

#%%
a = 2
b = '3'

a + b
# %%
help(list)
# %%
