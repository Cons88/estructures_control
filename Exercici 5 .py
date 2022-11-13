#!/usr/bin/env python
# coding: utf-8

# - Exercici 5
# Crea un programa que donada una llista, et digui quants números coincideixen 
# amb la seva posició. Per exemple [3,4,2,0,2,3,6] el 2 i el 6 coincideixen.

# In[55]:


Numeros = [0,4,2,0,4,3,6]
if Numeros[0] == 0:
    print("El número 0 y su índice en la lista coinciden")
elif Numeros[0] != 0:
     print("El número 0 y su índice en la lista NO coinciden")
if Numeros[1] == 1:
     print("El número 1 y su índice en la lista coinciden")
elif Numeros[1] != 1:
     print("El número 1 y su índice en la lista NO coinciden")
if Numeros[2] == 2:
     print("El número 2 y su índice en la lista coinciden")
elif Numeros[2] != 2:
     print("El número 2 y su índice en la lista NO coinciden")
if Numeros[3] == 3:
     print("El número 3 y su índice en la lista coinciden")
elif Numeros[3] != 3:
     print("El número 3 y su índice en la lista NO coinciden")
if Numeros[4] == 4:
     print("El número 4 y su índice en la lista coinciden")
elif Numeros[4] != 4:
     print("El número 3 y su índice en la lista NO coinciden")
if Numeros[6] == 6:
     print("El número 6 y su índice en la lista coinciden")
if Numeros[6] != 6:
     print("El número 6 y su índice en la lista NO coinciden")


# In[50]:


Numeros = [0,4,2,0,4,3,6]
print(Numeros[0:4])


# In[52]:


Numeros = [0,4,2,0,4,3,6]
for i in range(len(Numeros)):
    numero=Numeros[i]
    print(i,numero)


# In[53]:


Numeros = [0,4,2,0,4,3,6]
for i in range(len(Numeros)):
    numero=Numeros[i]
    print(i,numero)
    if i==numero
    print("True")

