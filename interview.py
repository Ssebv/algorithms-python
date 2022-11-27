'''
1. Definir una funcion max() que tome como
argumento dos numeros y devuelva el mayor de ellos 

'''
from operator import truediv
import re
from tkinter import N
from typing import KeysView
from unittest.util import strclass
from xml.etree.ElementTree import tostring


def f_maximo(n1,n2):
    while True:
        
        if n1 > n2:
            return n1
        elif n1 <=n2:
            return n2
        #else:
            #return ('Los numeros ingresados son iguales')

#print(fMaximo(3,3))         
'''
2. Definir una funcion max_de_tres(), 
que tome trenumeros como argumentos y devuelva el mayor de ellos.
'''

def max_de_tres(n1,n2,n3):
    a=f_maximo(n1,n2)
    #print(a)
    b=f_maximo(n2,n3)
    #print(b)
    c=f_maximo(n1,n3)
    #print(c)
    
    lista=[a,b,c]
    repeticiones={}
    
    for n in lista:
        if lista.count(n) != 1:
            
            if n in repeticiones:
                repeticiones[n] += 1
            else:
                repeticiones[n] = 0
    
        for mayores in repeticiones.keys():
            return mayores
            
print('El mayor numero encontrado es el', max_de_tres(5,1,3))

'''
3. Escribir una funcion que tome un caracter y devuelva True si es una vocal,
de lo contrario devolver False
'''

def f_es_vocal(caracter):
    vocal=['a','e','i','o','u']
    if caracter in vocal:
        return True
    else:
        return False
    
#caracter=str(input('Ingrese una letra del abecedario para comprobar si es vocal:'))

#print(f_es_vocal(caracter))

'''
4. Escribir una funcion sum() y una funcion multip() que sumen y 
multipliquen respectivamente todos los numeros de una lista.
Por ejemplo: sum([1,2,3,4]) deberia devolver 10 y multp deberia devolver 24
'''
def sum(lista):
    
    suma= 0
    for x in lista:
        suma += x
         
    return suma
        
        
def multp(lista):
    multiplicacion=1
    for x in lista:
       multiplicacion *= x
       
    return multiplicacion

#cant_numero= int(input('Ingrese ka cantidad de numeros a sumar y multiplicar: '))
#lista=[]
#for i in range(cant_numero):
#    lista.append(int(input('Numero %s : ' %(i+1))))
    
#print(('La suma de los numeros ingresados es : '), sum(lista))
#print(('La multiplicacion de los numeros ingresados es : '), multp(lista))

'''
5. Definir la funcion inversa() que calcule la inversion de una cadena. 
Por ejemplo la cadena 'Estoy probando' deberia devolver la cadena 'adnaborp yotse' 
'''

def inversa(cadena):
    #return cadena[::-1]
    cadena_invertida= ''
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
        #print(cadena_invertida)
    return cadena_invertida

#print(inversa(str(input('Ingrese una cadena de caracteres : '))))
    
    
'''
6. Definir una funcion es_palindromo() que reconoce palindromos
'''

def es_palindromo():
    
    while True:
        a=(str(input('Ingrese la palabra para comprobar que es un palindromo : ')))
        b= inversa(a)
        if a == b:
            return ('El caracter %s palindromo' %(a))
        elif a!= b:
            return ('La palabra %s no es un palindrom' %(a) +' La palabra invertida es %s' %(b))
        break
                  
#print(es_palindromo())

'''
7. Definir una funcion superposicion() que tome dos listas y devuelva True si
al menos 1 miembro o devuelva False de lo contrario.
'''

def superposicion(lista1, lista2):
    for elem in lista1:
        if elem in lista2:
            return True
    return False

#print(superposicion([1,2,5],[3,3,2]))

'''
8. Definir una funcion generar_n_caracteres() que tome un numero entero n y devuelva el 
caracter multiplicado por n 
'''

def generar_n_caracter(caracter,n):
    string= caracter
    for i in range(1, n):
        string += caracter
    print(string)
    
generar_n_caracter('abc', 2)

'''
Definir un histograma procedimiento() que tome una lista de numero enteros e imprima un histograma
en la pantalla 
'''

def procedimineto(lista):
    for i in lista:
        
        histograma= '*' * i
        print (f'{histograma} \n ')
        
procedimineto([5,2,3]) 