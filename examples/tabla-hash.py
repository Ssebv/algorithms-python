# Implementation de una Tabla Hash

class TablaHash:
    def __init__(self, tamano):
        # Inicializacion de la tabla hash
        self.tamano = tamano
        # Inicializacion de la lista
        self.data = [[] for _ in range(self.tamano)]

    # Funcion para obtener el hash de un elemento
    def hash(self, key):
        hash = 0
        for i in key:
            hash = (hash + ord(i))
        return hash % self.tamano

    # Entrega el valor de la llave
    # Si bien la funcion buscar en el peor caso es O(n), en el mejor caso es O(1)
    def buscar(self, key):
        x = self.hash(key)
        for elemento in self.data[x]:
            if elemento[0] == key:
                return elemento[1]
            else:
                return None

    # Inserta un elemento con su llave a la tabla hash
    # La funcion insertar en el peor caso es O(n), en el mejor caso es O(1)
    def insertar(self, key, value):
        x = self.hash(key)
        encontrado = False
        # Si la cantidad de elementos en la posicion es igual a 0, se inserta el elemento
        if len(self.data[x]) == 0:
            self.data[x].append([key, value])
        # Si no se recorre la lista y se inserta el elemento
        else:
            for elemento in self.data[x]:
                if elemento[0] == key:
                    elemento[1] = value
                    encontrado = True
                if not encontrado:
                    self.data[x].append([key, value])

# Con sus palabras compare el costo en tiempo de ejecucion de la funcion buscar y la funcion insertar

# La funcion buscar en el peor caso es O(n), en el mejor caso es O(1)
# La funcion insertar en el peor caso es O(n), en el mejor caso es O(1)
# Las dos funciones tienen el mismo costo en el peor caso, pero la funcion buscar tiene un mejor costo en el mejor caso

# Comente en que situación o problemática podría ser útil implementar o usar una tabla hash.

# Una tabla hash es util cuando se necesita almacenar datos de manera eficiente y rapida, ya que se puede acceder a ellos con una llave unica y no se necesita recorrer toda la lista para encontrar el elemento

def main():
    myHashTable = TablaHash(10)
    myHashTable.insertar("AB", 1)
    myHashTable.insertar("CD", 2)
    myHashTable.insertar("EF", 3)
    myHashTable.insertar("GH", 4)
    myHashTable.insertar("IJ", 5)
    myHashTable.insertar("KL", 6)
    myHashTable.insertar("ABCD", 7)
    myHashTable.insertar("EFGH", 8)
    myHashTable.insertar("IJKL", 9)
    myHashTable.insertar("MNOP", 10)

    print(myHashTable.data)
    print(myHashTable.buscar("AB"))
    print(myHashTable.data[0])
    print(myHashTable.data[1])
    print(myHashTable.hash("AB"))
    print(myHashTable.hash("KL"))


if __name__ == "__main__":
    main()