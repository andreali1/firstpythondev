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

