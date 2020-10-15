


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