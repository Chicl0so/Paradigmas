lista = [1,2,3,4,5]
lista1 = lista


def copy(lista):
    lis = []
    
    for i in range(0, len(lista)):
        lis.append(lista[i])
       
    
    return lis

def append(lista):
    lis = []
    for i in range(0, len(lista)):
        lis += str(lista[i])
        if type(lista[i]) == type(1):
            lis[i]= int(lis[i])
        print(lis)
    return lis

append(lista)