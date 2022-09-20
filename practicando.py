#comando para abrir pycharm
# ./pycharm.sh

nom="carlos"
ape="mamani"
print(nom,ape)


mivar=False
print(mivar)
mivar=3>2
print(mivar)
from ast import If

#variables booleanas y if else
mivar=False
print(mivar)
mivar=3>5
print(mivar)

if mivar:
    print("es verdadero")
else:
    print("es falso")

#proceso de usuarioo uso de (input)
#funcion de input para procesar la entrada de usuario
res=input("ingrese un texto: ")
print("valor asignado:",res)
print("fin del input")




#funcion de input para procesar la entrada de numeros
#convirtiendo en booleano
num1=input('ingree primer numero ')
num2=input('ingree segundo numero ')
print('RESULTADO: ',int(num1)+int(num2))
#Ejercicio de calificando tu dia 
res=input('como estuvo tu dia: ')

print('mi dia estuvo de texto : ',res)

#ejercicio
titulo=input('proporciona el titulo: ')
autor=input('proporciona el autor: ')
print('El titulo es : ',titulo,'Escrito por ',autor)
#operaciones 
n1=10
n2=5
sum=n1+n2
res=n1-n2
mul=n1*n2
div=n1/n2
divent=n1//n2
exp=n1**n2
print(f'suma: {sum} resta: {res} multiplicacion: {mul} division: {div} diventero: {divent} expone: {exp}')
#ejercicio area y perimetro
a=int(input('ingrese alto: '))
b=int(input('ingrese ancho; '))
area=a*b
perimetro=(a*b)*2
print(f'El area es: {area} El parametro es: {perimetro}')
#usando los operadores abreviados
nu=37
nu+=1
print(nu)
nu-=1
print(nu)
nu*=2
print(nu)
nu/=2
print(nu)
nu//=3
print(nu)
nu**=2
#usando operadores abreviados
a=4
b=2

resultado = a == b
print(f'Resultado ==: {resultado}')
resultado=  a != b
print(f'Resultado !=: {resultado}')
resultado = a>b
print(f'Resultado >: {resultado}')

#ejercicio numero par o impar
a=int(input('ingrese numero: '))
if a % 2 == 0:
    print('Es par')
else:
    print('Es impar')
#edad de una persona
edadulto=18
edad=int(input('ingrese edad: '))
if edad>=edadulto:
    print('es un adulto')
else:
    print('es menor de edad')
#operadores logicos de python
a=True
b=3
res= not b
res = a and b
res = a or b
print(res)
#usando el operadores logicoa
valor=int(input('ingrese numero: '))
vmax=5
vmin=0
res = valor>=vmin and valor<=vmax
if res:
    print('dentro del rango')
else:
    print('Fuera de rango')

#not contrario
#usando el operadores logicoa 
valor=int(input('ingrese numero: '))
vmax=5
vmin=0
res = not(valor>=vmin and valor<=vmax)
if res:
    print('dentro del rango')
else:
    print('Fuera de rango')
    


