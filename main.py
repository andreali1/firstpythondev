# #ingresando para la funcion con uso de --raise--
# from  holi import error
# error()
#


# #excepcines reconociendo los errores
# try:
#     a = int(input("ingresa el numero"))
#     10  / a
#     #si ingresas texto es un ValueError
#     #si ingresas cero es un ZeroDivisionError
# except ValueError:
#     print("ingresaste texto ")
# except ZeroDivisionError:
#     print("no se puede dividir entre cero ")
# except Exception as x:
#     print(type(x).__name__)#identifica el tipo de error que esta cometiendo para declarara en la excepciion por error
#




# #en este ejemplo el error forzado parte de no ingresar el tipo de variable al numeor q se va ingresar
# try:
#     a=input("ingresar numero :  ")
#     10/a
# except Exception as x: #le estas dando al Expection el nombre de x osea un valor  -- x== Exception
#     print(type(x).__name__) # muestrael nombre del erro que se esta ejecutando


#exepciones multiples en python y como funciona el try
# while True: #while solo de prueba para que programa no se cierre
#     try:#cuando pueden exitir un erro obligarotio o por mal ingreos de dato s
#         va = int (input("ingres el numeor de telefono"))
#         print( "confirme si si numeor de telfono es correcto ",va)
#         opc= int(input("ingrese 1 para si y 2 para no "))
#         if opc ==1:
#             print("gracias ")
#         elif opc ==2:
#             print("reingrese su numeor de telefono")
#             continue
#         else:
#             print("ustede no inrgeso numero ")
#     except: #ya no sale Syntax erro line etc etc sino se muestra este mensaje
#         print("usted ingreso caravteres o simbolos mas no numero s")
#
#     else: #cuando termina el --try--- y de manera satisfactoria y se puede continuar
#         print("igreso de datos correecto ")
#         break #para termianr el while y no sea un bucle infinito
#     finally:#se muestra siempre que termina el ry
#         print("Mcuhas gracias por su tiempo y paciencia")





# print("ingresa tu numero de celular ")
# try:
#     b = int(input("ingresa el neumero "))
#     a = 2
#     x = a*b
#     print("es el doble de tu numoer ",x)
# except:
#     print("no ingresaste un numero")





##funciones on argumentos variables puden variar en tupla o en diccionarios definicion especificafa en keeps de google
# from holi import funca
#
# funca(1,2,3,4,andree='aliaga', rosa ='calderon', notas =[1,2,3,4])

# def argu(*tu):
#     for tus in tu:
#         print(tus)
#
# argu('andree', 'aliaga',122,[1,2,3,4,5])
#
# def dele(**lo):
#     for x in lo:
#         print(x, lo[x])
#
# dele(andree = 'aliaga', rosa = 'calderon ', notas = [1,2,3,4,5],carlos= ' coca' )




# numero =[9,8,7]
# for x,i in enumerate(numero): #x esta dando la posiscion en la q estan los valores yy la "i" esta haciendo q se saquen los valores de
# #la lista para poder operarlos con el operador que se encuntra luego del segundo prin dos lineas mas abajo
#     print(x,"xxxxxx")
#     print(i)
#     numero[x] *=3
#
# print(numero)

# #trabahjando con las funciones y como se puede manejar los valores q esten declaradas antes en ellas
# import  holi
# a,b,c,d = holi.gente() # la funcion tiene en el retur 4 valores cone sto estamos asigano a cada una de la varialbles un
# # valor y por eso ya podemos llamalas de manera dicrrecta
# print(holi.gente())
# print(a)
# print(type(a))
# print(b)
# print(c)
# print(type(c))
# print(d)



# #funciones mel scrip holi  todas las usadas estan en el import
# from holi import multiplicacion, division
# print("programa de  multi y divi")
#
# print(" ingrese el numero de la operacion que desea realizar ")
# print("1 .- multiplicacion")
# print("2.- division ")
# opc = int(input("el ingrese el valor -->"))
# b = int(input("ngrese el primer valor "))
# c = int(input("ingrese el segundo valor "))
# if opc == 1:
#     multiplicacion(b,c)
# elif opc ==2:
#     division(b,c)
#




# #utilizando funciones de manera mas directa en el from estan las funciones llamadas de holi
# #solo funciones suma y res
# from holi import suma,resta,tabla
# print(" sumas y restas ")
# print("1.- suma de los numeros")
# print("2 .- la resta de los numeor s")
# print("3.- obtener la tabla de un numero ")
# a = int(input("ingrese el numoer de la operacion q desea realizar "))
# if a ==1 :
#     f= int(input("ingrese el primer valor"))
#     g = int(input("ingrese el segundo calor "))
#     suma(f,g)
# elif a == 2:
#     f = int(input("ingrese el primer valor"))
#     g = int(input("ingrese el segundo calor "))
#     resta(f, g)
# elif a== 3:
#     g = int(input("ingrese el numero"))
#     tabla(g)
# else:
#     print("el numeor ingresado no es una opcion ")







#usando funciones del scrip holi en el import especifica que funciones estoy utilizando
# from holi import persona, nota
#
# dic1 =  dict()
# dic2 =  dict()
#
# a = persona(dic1, 'andree', 'aliaga', 30)
# print('nombre :', a['nom'], 'Apellido: ',a['ape'], 'edad : ', a['age'])
#
# y = int(input("ingrese el valor de la primera nota xxxxx "))
# t = int(input("ingrese l valor de la segunda notaxxxxx"))
# u = int(input("ingrese el valor de la tercera personaxxxx"))
# b = nota(y,t,u)
#





# #usando funciones eingresando los primeros usos de la misma
# import holi # importando funciones de otro scrip
# def estude(f,g): #declarando la primera funcion local
#     d = f * g
#     print("la multiplicacion de los numero s es ---> ",d)
#
# a=input("ingresa una palabra ")
#
# if a == 'go': #llamando a la funcion de otro scrip importar "import -- nombre del scrip -- . la funciopn y parametros
#     f = int(input("ingresa valor de j "))
#     w = int(input("ingresa el valor de k "))
#     holi.multi(f,w)
# elif a == "local": #llamando a la funcion dentro del mismo scrip
#     h = int(input("inrgesando primer valor"))
#     l = int(input("ingresando segundo valor"))
#     estude(h,l)
# elif a == 'chau': #cerrando el programa
#     print("no hay nada ")
# else:
#     print("no hay funcion con la que se peueda tarabajar")







#ingresando a funciones en python
#.-----------------------------------------------------
#.----------------------------------------------------- termiandno parametroa basicos y pasando a funciones
#el format puedes ingreasr valores en la cadena pero debe estar dentro de una variable primero
#el roden en q lo pongas sera el que agarre si no especificas un lugar en las comillas osea en el orden en q ingrese
# pero si especificas posiciones con 0,1,2 lo ingresara en el roden que tu le indiques al programa
# na = "..andreee"
# ne = "..bien"
# ni = "--me llegas al pincho "
# frase = "hola como estas {2} , como te encuentras en esta tarde {0} , danos un mensaje {1} ".format(na,ne,ni)
# print(frase)
# we ='andree'
# wa = 'aliaga'
# fa = ' como estas {} , pero te gusta {}'.format(we,wa)
# print('{:>100}'.format(fa)) # el :>100 le indicas al programa el numeor de tabulaciones con el que deb mostrar el texto y ademas
# #estamos interando un format dentro de otro format, no hay diferencia ya que "fa" ya nos entrega una cadena entera asi q seria inutil



#ingresanoddatos por teclado n en consola
# #ingresando varios valores en una lista y ordenandolos en forma creciente
# print("programa para ingreso de varios valores en una lista ")
# a = int(input("ingresa el numeor de elementos que va tener la lista"))
# li = []
# for h in range (a):
#     li.append(input("ingresa el valor "))
# li.sort()
# print(li)



#.-----------------------------------------------------
#.-----------------------------------------------------
#maneo de colas en python
#para usar librerias no vienen preinstaladas en los paquetes asi que se tiene q llamar a la libreria (from collections import deque)
#puedes eleiminar el primer elemento y el ultimo
# from collections import deque
# cola = deque()
# print(cola)
# cola = deque(['andree','carlos','juan '])
# print(cola)
# #cola.pop() # eliminas el ultimo elemento de la lista
# cola.popleft() #eliminas el primer elemento de la lista
# print(cola)



#.-----------------------------------------------------
#.-----------------------------------------------------
#mnejando pilas todo casi  lo mismo que las listas
# api = [2,5,9]
# print(api, "mostarando lista original")
# api.append(4)
# api.append(8)
# api.append(18)
# api.append(12)
# api.append(3)
# api.append(1)
# print(api,"mostrando lista con los nuevos valores ingresados ")
# api.sort() # ordenadno en metodo creciente la lista
# print(api,"mostrando lista con valores ya operdenaods")
# #a = api.pop() #eliminando el ultimo valor de la lista
# a = api.pop(4) # eliminando un valor de la lista segun su orden especifico
# c = len(api) # determinando el numeor de elementos que tiene la lista
# print(c,"num elementos") # mostrando numeor de elementos de la lista
# print(api)#"mostrando lista con el valor eimando "
# print(a, "valor eliminado") # valor que eliminaste de la lista
# print(api)
# api.append(a)
# print(api)
# api.sort()
# print(api)
# #multiplucaondo todos los elementods de la lista por un numoer
# for h in range(0,c):
#     b =(api[h]*c)
#     print("el numero ", api[h], "  multiplicado por ", c, " es igual ah ---> " ,b)
#     #print(b )
#




#.-----------------------------------------------------
#.-----------------------------------------------------
#diccionarios control y crear diccionarios desde una lista
# mi = ['miCoche1', 'miCoche2', 'miCoche3', 'miCoche4', 'miCoche5']
# lis =[]
# con = set(mi)
# print(con)
# con1 = list(con)
# con1.sort()
# print(con1,"hli")
# lis.extend(con1)
# print(lis)
# dic2 = dict(enumerate((lis)))
# print(dic2)

# #agregando valores a un diccionario en python
# dici = {"nombre":"andree", "apellido ":"aliaga"} # lista original
# print(dici)#motrandi lista original
# dici["seg"] = "calderon" #agregando una nueva llave y valor
# print(dici) # mostarando diccionario modificado con el nuevo valor



#
# mi2 = ["c","f","b" ,"w", "j", "e","a"] # lista original
# print(mi2) # mostarando lista original
# mi2.sort() #ordenando lista
# print(mi2)#mostarndo lista ordenada
# dic = dict(enumerate(mi2,1)) #convirtiendo la lista en un diccionairo ordenado, el argugmente declarado luego de la lista
# #enumerate(mi2, 1) el argumento indica desde que numeor empezara a enumerar si no se delcara el numeor empieza desde el 0
# print(dic) #mostrando el diccionairo ya ordenado que nacio de la lista
# print("-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-fuera de serie ")
# mi = ["c","f","b" ,1,3,5,6,"w", "j", "e","a"]
# frozenset((mi))
# print(mi)
# """Existen dos tipos de conjuntos: set, propiamente dicho, que es mutable y coloca los ítems en un orden aleatorio; y
# frozenset, que tal y como sugiere el pronombre "frozen", que se traduce como "congelado", es inmutable, es decir,
# que no se puede modificar. Esta es en síntesis su diferencia fundamental.
# """


# #mostrando las llaves con sus valores de iun diccionario
# dic = {'andree':'aliaga', 'jennifer': 'serpa','rosa':'calderon'}
# dics = ['hola', 'chau']
# #dic['andree'] = 'calderon' #modificando el valor de una llave en el diccionario
# #del(dic['andree']) #eliminando elemento del diccionario
# a =0
# for i in dic:
#     print(i #esta leyendo solo la llave n el orden como ingresaste darto
#           ,dic[i]) #el dic[i] esta ubicando con el numero de la llave el valor que va mostrar


#.-----------------------------------------------------
#.-----------------------------------------------------
#convirtiendo de lista a conjunto y luego regresando a lista
# lista = [1,2,3,4,5,5,5,5,5]
# print(lista)
# my_set = set(lista)
# print(my_set)
# new_lis = list(my_set)
# print(new_lis)
# print("x-x-x-x-x-x-x--x-x-x-x--x-x-x-x-x--x-x-x-")
# lista =["aba", "abe", "abi", "abo", "abu","aba","aba","carro", "carro"] #lista inicial
# print(lista)
# con = set(lista) #convirtiendo la lista en conjunto para eliminar elementos repetidos
# print(con)
# newc_con = list(con) #creando una nueva lista dsde un conjunto CONVIRTIENDO UN CONUNTO EN LISTA
# las = [] #nueva lista vacia
# las.extend(newc_con) #ingresando los valores de la nueva lista en la lista vacia
# las.sort() #ordenando la lista por orden alfabetico
# print(las)
# cadena = "cnskacndkncdsknvdsnkvsndvkndlamslcmdscdsvnns" # cadema con muchos caracteres repetidos
# print(set(cadena))# elimianndo caracateres repetidos


# my_set = set([1,2,3,4])
# my_list = list(my_set)
# print my_list






#ingresando caondicionales basados en la respuesta de un una coleccion
# cole = {"aba", "abe", "abi", "abo", "abu"} # no se puede tener elementos repetidos en colecciones
# print("aba" in cole)
# if ("aba" in cole) == True:
#     print("el if si funciona ")
#manejando conjuntos en python creando y agregando nuevos conjuntos
#con = set() #creando una lista vacia
#con.add(2) #agregando un valor a una lista
#print(con)  ##impirmiendo la lista
# con = {1,3,4,5}
# con.add(2)
# print(con)
# con.add(0)
# print(con)
# (con.add(91))
# print(con)



#.-----------------------------------------------------
#.-----------------------------------------------------
# #manejando tuplas primera tupla de ahi convertiendo a lista y agergando un elemento y despues regresando a tupla
# tu = ('andree','anthony', 'aliaga',25, [1,2,3],-80)
# print(tu)
# a = list(tu)
# print(a)
# a.append('yohanna')
# b = tuple(a)
# print(b)
# print(b[3])


#.-----------------------------------------------------
#.-----------------------------------------------------
# #ingresando valores por consola de una lista y luego ubicando el numeor de mayor valor en la lista
# #"la ubicacuiion se hace deacuerdo a la posicion "
# a = []
# for x in range(5):
#     b =int(input(("ingrese los valores de la lista : ")))
#     a.append(b)
# print(a)
#
# num = a[0]
# for x in range (1,5):
#     if a[x] > num:
#         num = a[x]
#
# print(a)
# print(num)
#



# lista=[]
# for x in range(5):
#     valor=int(input("Ingrese valor:"))
#     lista.append(valor)
#
# mayor=lista[0]
# for x in range(1,5):
#     print(x)
#     if lista[x]>mayor:
#         mayor=lista[x]
#
# print("Lista completa")
# print(lista)
# print("Mayor de la lista")
# print(mayor)
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