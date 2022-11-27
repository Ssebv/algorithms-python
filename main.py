import math
def compareTriplets(a, b):
    # Write your code here
    puntaje = [0,0]
    for i in range(len(a)):
        print(i)
        if a[i] > b[i]:
            puntaje[0] += 1
        elif a[i] < b[i]:
            puntaje[1] += 1
        else:
            pass
    return puntaje

def aVeryBigSum(ar):
    # Write your code here
    suma = 0
    for elemento in ar:
        print(elemento)
        suma += elemento
    return suma

def diagonalDifference(arr):
    # Write your code here
    suma1 = 0
    suma2 = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(i,j)
            #print(arr[i][j])
            if i == j:
                suma1 += arr[i][j]
            if i + j == len(arr) - 1:
                print(len(arr) - 1)
                suma2 += arr[i][j]

    #return abs(suma1 - suma2)
    return abs(suma1 - suma2)

def plusMinus(arr):
    # Write your code here
    positivos = 0
    negativos = 0
    ceros = 0
    for i in arr:
        #print(i)
        if i > 0:
            positivos += 1
        elif i < 0:
            negativos += 1
        elif i == 0:
            ceros += 1

    #print(positivos,negativos, ceros)
    cantidad_elementos = len(arr)

    proporcion_positivos = round(positivos / cantidad_elementos,6)
    proporcion_negativos = round(negativos / cantidad_elementos,6)
    proporcion_ceros = round(ceros / cantidad_elementos, 6)


    print(proporcion_positivos)
    print(proporcion_negativos)
    print(proporcion_ceros)





if __name__ == '__main__':

    #a = [5,6,7]

    #b = [3,6,10]

    #result = compareTriplets(a, b)

    #array =  [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    #print(aVeryBigSum(array))

    #arr = [[1,2,3],
           #[1,2,3],
           #[1,2,3]]
    #print(diagonalDifference(arr))

    arr = [-4,3,-9,0,4,1]

    print(plusMinus(arr))




