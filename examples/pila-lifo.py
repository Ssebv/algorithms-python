# Descripcion: Pila LIFO - Last In First Out

# Creacion de la clase Nodo que contiene el dato, el puntero al siguiente nodo y el puntero al nodo anterior

class Nodo():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
# Creacion de la clase PilaLIFO que contiene el puntero(head) al primer nodo

class PilaLIFO:
    def __init__(self):
        self.head = None
    
    # Metodo para insertar un nodo al final de la pila
    
    def Push(self, elemento):
        # Si la lista esta vacia se crea inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        
        # Sino, se inserta al inicio de la pila
        else:
            nuevoNodo = Nodo(elemento)
            nuevoNodo.next = self.head
            self.head.prev = nuevoNodo
            self.head = nuevoNodo
       
    # Metodo para eliminar el ultimo nodo que ingreso a la pila
    
    def Pop(self):
        # Si la lista esta vacia no se puede eliminar el ultimo nodo
        if self.head is None:
            return None
        
        # Sino, se elimina el ultimo nodo que ingreso a la pila
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data
    
    # Metodo para imprimir la pila
    
    def printPila(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next     
            
# __main__
if __name__ == '__main__':
    print("Pila LIFO - Last In First Out")
    pila = PilaLIFO()
    pila.Push(1)
    pila.Push(2)
    pila.Push(3)
    pila.Push(4)
    pila.Push(5)
    pila.Push(6)
    print("PILA")
    pila.printPila()
    print("-----------------")
    print("Retirada de la pila : ", pila.Pop())
    print("Retirada de la pila : ", pila.Pop())
    print("Retirada de la pila : ", pila.Pop())
    print("-----------------")
    print("PILA")
    pila.printPila()
    
# Comentario Documentacion
# Orden de Complejidad en notación O

# Las operaciones basicas(1 unidad de tiempo) son: O(1)
# El tiempo de un if es O(max(bloque_if, bloque_else))
# El tiempo de un for es la suma de sus tiempos usando la notación O-Grande

#-------------------------------------------#
# Tiempo de ejecucion de los metodos

# T(n)----->Tiempo de ejecucion

# Nodo O(1)
# PilaLIFO O(1)

# Push O(1)
# Pop O(1) 
# printPila O(n)

#-------------------------------------------#

# Resolucion

# O(1) + O(6) + O(n) + O(3) + O(n) = 

# O(10) + O(2n) = O(2n) = O(n)