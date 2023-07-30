# Descripcion: Fila FIFO -  First in First Out order

# Creacion de la clase Nodo que contiene el dato, el puntero al siguiente nodo y el puntero al nodo anterior

class Nodo():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
# Creacion de la clase FilaFIFO
class FilaFIFO:
    def __init__(self):
        self.head = None
        self.tail = None

    # Metodo para insertar un nodo al inicio de la lista (final de la cola)
    
    def Push(self, elemento):
        # Si la lista esta vacia se crea inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
            self.tail = nuevoNodo
            
        # Sino, se inserta al final de la cola
        else:
            nuevoNodo = Nodo(elemento)
            nuevoNodo.next = self.head
            self.head.prev = nuevoNodo
            self.head = nuevoNodo

    # Metodo para que salga el primer elemento de la cola

    def Pop(self):
        # Si la lista esta vacia sale el primer elemento que ingreso en la cola
        if self.head is None:
            return None
        
        # Sino, sale el primer elemento de la cola
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return temp.data

    # Metodo para imprimir la cola
    
    def printFila(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        
# __main__
       
if __name__ == '__main__':
    print("Fila FIFO - First in First Out order")
    cola = FilaFIFO()
    cola.Push(1)
    cola.Push(2)
    cola.Push(3)
    cola.Push(4)
    cola.Push(5)
    cola.Push(6)
    cola.Push(7)
    print("FILA")
    cola.printFila()
    print("-----------------")
    print("Retirada de la cola: ", cola.Pop())
    cola.printFila()
    print("Retirada de la cola: ", cola.Pop())
    cola.printFila()


# Comentario Documentacion
# Orden de Complejidad en notación O

# Las operaciones basicas(1 unidad de tiempo) son: O(1)
# El tiempo de un if es O(max(bloque_if, bloque_else))
# El tiempo de un for es la suma de sus tiempos usando la notación O-Grande

#-------------------------------------------#
# Tiempo de ejecucion de los metodos

# T(n)----->Tiempo de ejecucion

# Clase Nodo O(1)
# Clase FilaFIFO O(1)

# Push O(1)
# Pop O(1)
# printFila O(n)

#-------------------------------------------#

# Resolucion

# O(1) + O(7) + O(n) + O(1) + O(n) + O(1) + O(n) =

# O(10) + O(3n) = O(3n) = O(n)