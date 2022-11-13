#!/usr/bin/env python
# coding: utf-8

# - Exercici 3
# Crea un programa que et pregunti el teu nom, i et demani un número. Si el número és 0, hauria de mostrar un missatge d’error. En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número. Per exemple, “Joan Joan Joan”.
# 

# In[23]:



Nombre = input("Ingrese su nombre: ")
Numero = int(input("Ingrese su numero: "))

      
def my_function():
   print (Nombre,Numero)
   
my_function()


# In[29]:



Nombre = input("Ingrese su nombre: ")
Numero = int(input("Ingrese su numero: "))

      
def my_function(Numero,Nombre):
   if Numero < 1: 
       print("Error")
   else: 
       print ("Hola ",Nombre, Numero)
   
my_function(Numero, Nombre)


# - Exercici 4
# Crea un programa que donada una llista qualsevol, et digui si és simètrica o no. Si ho és, que et digui quants elements té.
# 

# In[16]:


#He utilizado una Matriz

def es_simetrica(matriz,orden):
    simetrica = True
    for i in range (orden):        
        for j in range (orden): 
            if(matriz[i][j]!=matriz[j][i]):
                simetrica=False
    return simetrica

def main():
    matriz = [ [0,0,1],
               [0,1,1],
               [1,4,1]
            ]
    respuesta=es_simetrica(matriz,len(matriz))
    if(respuesta==True):
        print("Matriz simetrica")
    else:
        print("Matriz no simetrica")
main()
               


# In[10]:



def es_simetrica(matriz,orden):
    simetrica = True
    for i in range (orden):        
        for j in range (orden): 
            if(matriz[i][j]!=matriz[j][i]):
                simetrica=False
    return simetrica

def main():
    matriz = [ [0,0,1],
               [0,1,1],
               [1,1,1]
            ]
    respuesta=es_simetrica(matriz,len(matriz))
    if(respuesta==True):
        print("Matriz simetrica")
        print("Elementos de la lista: ", len(matriz))
    else:
        print("Matriz no simetrica")
main()


# In[2]:


def es_simetrica(matriz,orden):
    simetrica = True
    for i in range (orden):        
        for j in range (orden): 
            if(matriz[i][j]!=matriz[j][i]):
                simetrica=False
    return simetrica

def main():
    matriz = [ ["Juan","Pedro","Jose"],
               ["Pedro","Juan","Jose"],
               ["Jose","Juan","Pedro"]
            ]
    respuesta=es_simetrica(matriz,len(matriz))
    if(respuesta==True):
        print("Matriz simetrica")
    else:
        print("Matriz no simetrica")
main()

