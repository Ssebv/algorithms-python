#Clase que permite reunir key, lista adyacencia y color class Nodo:
    def __init__(self,key ,ady_list ,color ):
        self.key = key
        self.ady_list = ady_list
        self.color = color
        
    def __str__(self):
        return str(self.key)+" "+str(self.ady_list)+" "+str(self.color)

#abrimos archivo
file = open("./salida.txt", "r")
(N, V) = file.readline().split(" ")
N = int(N)
V = int(V)
print("nodos:",N, "\tmax_adyacente:", V, "\n")
lines = file.readlines()

#Llenamos las lista de adyacencia, usamos un diccionario
grafo = {}
for l in lines:
    line = l.split(" ")
    key_nodo = int(line[0])
    ady_list = {}
    for i in range(1,len(line), 2):
        peso = float(line[i])
        vertice = int(line[i+1])
        ady_list[vertice] = peso
    grafo[key_nodo] = Nodo(key_nodo, ady_list, None)

#Calculamos enlaces de salida para cada nodo
print("\nenlaces de salida:")
for i in grafo:
    print(i, grafo[i], len(grafo[i].ady_list))

#Calculamos enlaces de entrada para cada nodo    
print("\nenlaces de entrada:")
suma = {x:0 for x in range(N)}
for i in grafo:
    for j in grafo[i].ady_list:
        suma[j] += 1
print(suma)

#definimos la funcion de recorrido en anchura
def bfs(grafo, inicio):
    #Cada nodo del grafo se establece de color blanco
    for i in grafo:
        grafo[i].color = "white"

    #inicializamos una cola vacia
    cola = []

    #agregamos a la cola la key del nodo de inicio
    cola.append(inicio)

    # Para cada nodo en la lista de adyacencia de u hacemos:
    while len(cola) > 0:
        # Si no se está apuntanto a si mismo y es blancho,
        # entonces lo marcamos como gray y lo agregamos a la cola
        u = cola.pop(0)
        for v in grafo[u].ady_list:
            if v != u and grafo[v].color == "white":
                grafo[v].color = "gray"
                cola.append(v)
        # marc
        grafo[u].color = "black"

    #Imprimimos el recorrido
    print("\nRecorrido BFS:")
    for i in grafo:
        print (grafo[i].key, grafo[i].color)

    print(cola)
    print()
#LLAMAMAOS A LA FUNCION

bfs(grafo, 0)
