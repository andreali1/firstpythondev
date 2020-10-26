#trabajando con try y funciones
#funciona siempre y cuando desde  el main e usea la funcion y y la mandes vacia  obviamente importando ion y el scrip
def error(estu= None):
    try:
        if estu is None:
            raise print("describe algo")
            #funcion ---raise- sirve para que te muestre el erro normal de consocla
            # cuando esta mal el codigo  peor en el value error puedes poner el texto que desee
    except ValueError:
        print("ingresa algo please")




#unciones con recursividad usando la funcion dentro de la misma funcion
def atras(seg):
    seg -=1
    if seg >=0:
        print(seg)
        atras(seg)
    else:
        print("finish")


#funcion con argumento variable
def funca(*ho,**lo):
    b =0
    for tus in ho:
        b+=tus
        print(tus)
    print(b)
    for x in lo:
        print(x , " ",lo[x] )



def multiplicacion(q,w):
    g = q *w
    print("l resultado de la multiplicacion es ---> ",g)
    #return g
def division(q,w):
    if q > w:
        b = q/ w
        d = int(b)
        print("el resulatdo de la operacion es ",d)
    elif q ==w:
        b = q/w
        print("el resuñtado de la operaion es -->",b)
    elif q <w:
        print("el resultado de la operaicion es menor a la unidad ")


def multi(j,k):
    p = j * k
    print("el valro de la multi - de otro scrip la funcion de muti de scrip holi " ,p)
    return p

def persona(dic, nombre , apellido, edad):
    dic['nom'] = nombre
    dic['ape'] = apellido
    dic['age'] = edad
    print(dic)
    return dic

def nota(pe,se,te):
    a  = (pe+ se+te)/3
    print(a)
    return a

def suma(q,w):
    p = q+w
    print("la siuma de los numeors es -->",p)

def resta(q,w):
    if q >= w:
        print("la resta de los numero es ",q-w)
    else:
        print("lla resta de los numeros es", q-w)


def tabla(a):
    for x in range(1,11):
        b = a * x
        print("el numero {} mutiplicado por {} es iguala a -->".format(x,a),b)
    return 0


def gente():
    return "hola", "chau",1, [12,3,4,5,6]

def potencia(a,b):
    c = pow(a,b)
    return print(c)