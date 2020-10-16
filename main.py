
#.-----------------------------------------------------
#.----------------------------------------------------- estudiar despues eventos
#semaforo automata ne python
# import time                                # Librería o Módulo implementado para llevar el tiempo del semáforo
# from fysom import Fysom                    # Libreria o Módulo que contiene las funciones para la máquina
#
# semaforo = Fysom({ 'initial': 'verde',     # Estado inicial de la máquina.
#         	   'events': [                   # Lista de transiciones (eventos) de la máquina
#                   {'name': 'precaucion', 'src': 'verde', 'dst': 'amarillo'},
#                   {'name': 'stop', 'src': 'amarillo', 'dst': 'rojo'},
#                   {'name': 'go', 'src': 'rojo', 'dst': 'verde'} ] })
#
# while True:
#   if semaforo.current == "verde":  # 'semaforo.current' almacena el estado actual de la máquina
#     print(semaforo.current)
#     time.sleep(15)                 # 'time.sleep(n)' espera 'n' segundos para continuar con la ejecución del programa
#     semaforo.precaucion()
#   if semaforo.current == "amarillo":
#     print(semaforo.current)
#     time.sleep(5)
#     semaforo.stop()
#   if semaforo.current == "rojo":
#     print(semaforo.current)
#     time.sleep(10)
#     semaforo.go()







# #dividr o multipkicar todos lo valores de una lista
#metodo nuero 1
# a = [10,20,30,40,50,60]
# indice =0
# for h in a:
#     a[indice]/=5
#     indice+=1
# print(a)
#metodo numeor 2 mismo resultado
# a = [1,2,3,4,5,6]
# i = 0
#
# for i ,h in enumerate(a):
#     a[i] *= 10
# print(a)
#print(list(range(10))) #creando una lista a raiz de un rango de numeros



#.-----------------------------------------------------
#.-----------------------------------------------------
# #programita funcionando todas las opciones todo lo del curos 20 %
# import os
# import  time
# a = input("escribe la palabra go para iniciar el programa : ")
#
# while a == "go":
#     print("revisa el menu de opcines ")
#     print(" 1.- sumar dos numeor \n 2.- restar dos numeor \n 3.- saludar \n 4.- dividir \n 5.-ingresar valores en una lista   \n 6.- salir del programa")
#     opc = int(input("ingrese el numeor de la opcion que desea realizar "))
#     if opc == 1:
#         f = int(input(" ingrese el vallor del primer numero "))
#         g = int(input(" ingrese el valor del segundo numeor "))
#         j = f+g
#         print("el resultado de la suma de los numeros es -->",j)
#     elif opc == 2:
#         f = int(input(" ingrese el vallor del primer numero "))
#         g = int(input(" ingrese el valor del segundo numeor "))
#         j = f - g
#         print("el resultado de la resta de los numeros es -->", j)
#     elif opc == 3:
#         nom = input("ingrese su nombre por favor ")
#         print("un gusto saludarlo ",nom," que tenga buen dia ")
#     elif opc == 4:
#         f = int(input(" ingrese el vallor del primer numero "))
#         g = int(input(" ingrese el valor del segundo numeor "))
#         if f > g:
#             c = f / g
#             print(" el resultado de la division es -->",c)
#         elif f ==g :
#             c = f /g
#             print("el resultado de la division es -->",c)
#         else:
#             print("el resultado de la operacion es menor a la unidad")
#     elif opc ==5:
#         print("opcion para ingresar valores en una lista ")
#         y = int(input("ingrese el numeor de valores con los q contara la lista "))
#         list = []
#         for x in range(0,y):
#             nombr = input("ingrese elprimer nombre la lista que tendra un indece de ")
#             list.append(nombr)
#             list.sort()
#         print("mostarndo la lista de nombres ingresados ")
#         print(list)
#         os.system("pause")
#         time.sleep(10)
#     elif opc == 6:
#         b = input("si dese salir del programa digite la palbra --salir--")
#         if b == "salir":
#             break
#         elif b != "salir":
#
#             print("Regresando al programa en 5")
#             time.sleep(1)
#             print("regresando al programa en 4")
#             time.sleep(1)
#             print("Regresando al programa en 3")
#             time.sleep(1)
#             print("regresando al programa en 2")
#             time.sleep(1)
#             print(" redirigiendo al programa ahora")
#             time.sleep(1)
#             os.system("clear")
#             continue
#     else:
#         print("usted no ingreso un numero de opcion valido \n regresando al menu principal del programa")
#     time.sleep(3)
#     os.system("clear")
# else:
#     print("usted no digito la plabara indica")
#     #break
# #





#.-----------------------------------------------------
#.-----------------------------------------------------
# #utilizando el cicli while con if para porcesos sencillos de conteo
# a = 0
# b =0
# while a <=10:
#     a+= 1
#     print("oli")
#     if a ==5:
#         print("interacion ",a)
#         break
#     else:
#         print("continuamos ")
#


# for z in range (0,255):
#     for y in range (0,255):
#         print(z,y)


#.-----------------------------------------------------
#.-----------------------------------------------------

# #if con palabras o letras
#
# a = ['andree','anthony' ]
# b = ['grover','ricardo' ]
# c = [1,2,3,4,5,6,7,8]
# d = [2,4,1,7,3,9]
# e = ["xiomara", "jennifer", "angela","andrea"]
# a.extend(b) #ingresando los datos de una lista b en la lista a
# a.append("aliaga ") #ingresando un nuevo valor al final de la lista
# a.pop(1) #elimnando elemento por idice en la lista
# b.count('ricardo')# cuneta el numero de veces q esta el elemnto en la lista
# c.index(3)#devuelve el elemento en la posicion indicada iniciando desde el 0
#
# (c.insert(3, "andreee")) #insertando datos desde en el index ue se le indique segun numero
# c.remove(3)#elimina el numero o palabra que este denro del parentesis
# c.reverse() #inviertir el orden de los elementos en la lista
# d.sort()# ejemplode  ordenado de la lista con numeros
# e.sort()#ordenando la lista por palabras
# print(e)



# #condicionales baisca de if
# a = int(input("ingrese el primer valor "))
# b = int(input("ingrese el segundo valor "))
# c = a%b
# if a % b ==0:
#     print("el resto de la operaion es -->",c)
#     if a > b:
#         print("la multiplicaciond e los mismo es ", a*b)
# else:
#     print(" hola como estan ")
#
#
#






#<>
#.-----------------------------------------------------
#.-----------------------------------------------------

# #DECLARANDO VARIABLES DE ENTORNO PARA EJECUCION DE OS.SYSTEM en pycharm
# #funcion para limpiar pantalla -- RECORDAR DE DECLARAR LA VARIABLE DE ENTORNO -- ruta para agregar la variable
# #settings-- build,excution,deployment-- consolo .--- python console-- envirommetn variable -- agregar ("export TERM=xterm-color")
# #luego en ejecuacion ("edit configuration") activar ("emule terminal in output console")
#
# #funcion de limpiado de poantalla
# import os
# def clear():
#     if os.name == "nt":
#         os.system("cls")
#     else:
#         os.system("clear")
# clear()
# #funcion con reingreso al programa despues de termiarlo o con opcion a salir del mismo
# while True:
#     c = int(input("ingrese el rango de numeros "))
#     a = int(input("ingrese el numero de la suerte "))
#     b =  int (input("ingresa el valor a determiar del numeros de la sueerte "))
#     for h in range (1,c):
#         if b == a :
#             print("encontraste el numero")
#             break
#         else:
#             print("el numero no es correcto tu ingresaste el numero ",h ,b)
#             break
#     salir = input("escriba pasra salir del programa ")
#     if salir =="salir":
#         break
#     elif salir !="salir":
#         os.system('nano')
#     else:
#         clear()
#         continue
#




#<>
#.-----------------------------------------------------
#.-----------------------------------------------------

# #probando las condicionales logicas and or not
# print(2+3==5 and  3+2 ==1)
# print(2+3!=8 or  2-3 ==5)
# print("x-x-x--x-x-x-x-x-x-x-x-x--x-x")
# print(2-3 ==5 and 2+3!=8 )
# print(2-3 ==5 or 2+3!=8 )
# print("--x-x-x-x-x-x--xx")
# print(not False)
# print(not True)
#
# print(True)
# print(False)
#






#.-----------------------------------------------------
#.-----------------------------------------------------
# #ingresanod valores a  una lista ! por teclado
# a = int(input("ingrese el numeor de elementos de la lista"))
# #definimos una lista vacia
# lista=[]
# #disponemos un ciclo de 5 vueltas
# for x in range(a):
#     valor=int(input("Ingrese un valor entero:"))
#     print("el numoer esta ingresando en la posicion ",x)
#     lista.append(valor)
#
# #imprimimos la lista
# print(lista)