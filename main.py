
#<>
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