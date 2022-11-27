# Descripcion: Lista doblemente enlazada

# Creacion de la clase Nodo que contiene el dato y el puntero al siguiente nodo

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
# Creacion de la clase ListaDoblementeEnlazada que contiene el puntero(head) al primer nodo

class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        
    # Metodo para insertar un nodo al inicio de la lista
    
    def insertarInicio(self, elemento):
        # Si la lista esta vacia se crea inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        # Sino se crea un nuevo nodo y se inserta al inicio de la lista
        else:
            nuevoNodo = Nodo(elemento)
            nuevoNodo.next = self.head
            self.head.prev = nuevoNodo
            self.head = nuevoNodo
            
    # Metodo para insertar un nodo al final de la lista
    
    def insertarFinalNodo(self, elemento):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
            return
        #  Sino se crea un nuevo nodo y se inserta al final de la lista con la condicion de que el siguiente nodo no sea None
        temp = self.head
        while (temp.next)  is not None:
            temp = temp.next
        nuevoNodo = Nodo(elemento)
        temp.next = nuevoNodo
        nuevoNodo.prev = temp
        
     # Metodo para insertar un nodo en una posicion determinada de la lista    
    
    def insertarPos(self,elemento, pos):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        # Sino se crea un nuevo nodo y se inserta en la posicion de la lista con la condicion de que el siguiente nodo no sea None
        else:
            nuevoNodo = Nodo(elemento)
            elemento = self.head
            i = 0
            while (i < pos - 1):
                i += 1
                elemento = elemento.next
            if pos == 0:
                nuevoNodo.next = self.head
                self.head.prev = nuevoNodo
                self.head = nuevoNodo
            else:
                nuevoNodo.next = elemento.next
                elemento.next.prev = nuevoNodo
                elemento.next = nuevoNodo
                nuevoNodo.prev = elemento
    
    # Metodo para eliminar un nodo determinado de la lista
    
    def eleminarPos(self, pos):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            print("La lista esta vacia")
            return
        
        elemento = self.head
        if pos == 0:
            self.head = elemento.next
            elemento.next.prev = None
            return elemento.data
    
        i = 0
        while (i < pos):
            i += 1
            elemento = elemento.next
        
        else:
            elemento.prev.next = elemento.next
            elemento.next.prev = elemento.prev
            return elemento.data
    
    # Metodo para acceder a la posicion de un nodo determinado de la lista
    
    def accederPos(self, pos):
        if self.head is None:
            print("La lista esta vacia")
            return
        elemento = self.head
        i = 0
        while (i < pos):
            i += 1
            elemento = elemento.next
        return elemento.data
            
    # Metodo para recoorrer la lista desde el inicio hasta el final
    
    def recorrerInicioFin(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        apuntar = self.head
        while (apuntar):
            print(apuntar.data)
            apuntar = apuntar.next
            
    # Metodo para recoorrer la lista desde el final hasta el inicio

    def recorrerFinalInicio(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        apuntar = self.head
        while (apuntar.next):
            apuntar = apuntar.next
        while (apuntar):
            print(apuntar.data)
            apuntar = apuntar.prev
            
# Funcion main para probar la lista enlazada
if __name__ == "__main__":
         
        print("Lista Doblemente Enlazada")
        print("Se ingresan 6 nodos")
        
        miListaEnlazada = ListaDoblementeEnlazada()
        miNodo1 = Nodo(1)
        miNodo2 = Nodo(2)
        miNodo3 = Nodo(3)
        miNodo4 = Nodo(4)
        miNodo5 = Nodo(5)
        miNodo6 = Nodo(6)
        #miNodo7 = Nodo(1)
        miListaEnlazada.head = miNodo1
        miListaEnlazada.insertarInicio(miNodo2.data)
        miListaEnlazada.insertarInicio(miNodo3.data)
        miListaEnlazada.insertarInicio(miNodo4.data)
        miListaEnlazada.insertarFinalNodo(miNodo5.data)
        print("-----------------")
        miListaEnlazada.recorrerInicioFin()
        
        print("-----------------")
        miListaEnlazada.insertarPos(miNodo6.data, 3)
        miListaEnlazada.recorrerInicioFin()
        
        print("-----------------")
        Eleminar_Pos = miListaEnlazada.eleminarPos(2)
        miListaEnlazada.recorrerInicioFin()
        print(f"El elemento que se elemino en la posicion 2 es: {Eleminar_Pos}")
        
        
        print("-------------------")
        Pos = miListaEnlazada.accederPos(2)
        miListaEnlazada.recorrerInicioFin()
        print(f"El elemento que se accedio en la posicion 2 es: {Pos}")
        print("-----------------")
        miListaEnlazada.recorrerFinalInicio()
        print("-----------------")

        
# Comentario Documentacion
# Orden de Complejidad en notación O

# Las operaciones basicas(1 unidad de tiempo) son: O(1)
# El tiempo de un if es O(max(bloque_if, bloque_else))
# El tiempo de un for es la suma de sus tiempos usando la notación O-Grande

#-------------------------------------------#
# Tiempo de ejecucion de los metodos

# T(n)----->Tiempo de ejecucion

# Clase Nodo O(1)
# Clase ListaDoblementeEnlazada O(1)

# inserarInicio O(1)
# insertarFinalNodo O(1) + O(n)
# insertarPos O(1) + O(2 + n)
# eleminarPos O(3) + O(n) 
# accederPos O(1) + O(n)
# recorrerInicioFin O(1) + O(n)
# recorreFinalInicio O(1) + O(n) + O(n)

#-------------------------------------------#

# Resolucion

# O(8) +  O(3) + O(n) + O(n) + O(2+n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) =
# = O(9n) + O(13) = O(9n + 13) = O(n)
