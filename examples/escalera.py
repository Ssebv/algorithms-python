# Create a function that prints a stairway of n steps
def escalera(n):

    escalera = []
    for peldano in range(n):
        #print(peldano)
        escalera.append(" " * (n - peldano -1 ) + "#" * (peldano + 1))

    for peldano in escalera:
        print(peldano)

# Encotrar minimo y maxima suma de 4 elementos de una matriz
def minmaxSum(arr):
    # Write your code here
    suma = 0
    for i in arr:
        suma += i
    print(suma - max(arr), suma - min(arr))

# Mas de 5 elementos en una lista
def minmaxSum2(arr):
    sumaMayor = 0
    sumaMenor = 0
    numerosMayores = []
    numerosMenores = []
    for i in range(len(arr)):
        if len(numerosMayores) < 4:
            numerosMayores.append(max(arr))
            arr.remove(max(arr))
        if len(numerosMenores) < 4:
            numerosMenores.append(min(arr))
            arr.remove(min(arr))

    for i in numerosMayores:
        sumaMayor += i

    for i in numerosMenores:
        sumaMenor += i


    return sumaMayor, sumaMenor, numerosMayores, numerosMenores

if __name__ == '__main__':

    print(minmaxSum2([1,2,3,4,5,6]))
    #escalera = [ "   #",
                 #"  ##",
                 #" ###",
                 #"####"
                # ]
    #escalera(4)