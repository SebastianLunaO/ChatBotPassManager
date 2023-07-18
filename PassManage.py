
def taking(posicion):
    PWV= open('receta.txt','r')
    i=1
    while i<=posicion:
        exit=PWV.readline()
        i=i+1
    PWV.close()
    return exit



