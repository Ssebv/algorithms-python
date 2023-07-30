 # Descripcion: Lista enlazada simple

# Creacion de la clase Nodo que contiene el dato y el puntero al siguiente nodo

class Nodo():
    def __init__(self, data):
        self.data = data
        self.next = None

# Creacion de la clase ListaEnlazada que contiene el puntero(head) al primer nodo

class ListaEnlazada:
    def __init__(self):
        self.head = None
        
    # Metodo para insertar un nodo al inicio de la lista
    def insertarInicio(self, elemento):
        # Si la lista esta vacia se crea inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        else:
            nuevoNodo = Nodo(elemento)
            nuevoNodo.next = self.head
            self.head = nuevoNodo
    
    # Metodo para insertar un nodo al final de la lista    
    def insertarFinal(self, elemento):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
            return
        # Si la lista no esta vacia se recorre hasta el ultimo elemento y se inserta
        temp = self.head
        while (temp.next)  is not None:
            temp = temp.next
        nuevoNodo = Nodo(elemento)
        temp.next = nuevoNodo
            
    # Metodo para insertar un nodo en una posicion determinada de la lista
    def insertarPos(self, elemento, pos):
        # Si la lista esta vacia se inserta como primer nodo inemdiatamente
        if self.head is None:
            nuevoNodo = Nodo(elemento)
            self.head = nuevoNodo
        # sino, se recorre la lista hasta la posicion deseada
        else:
            nuevoNodo = Nodo(elemento)
            elemento = self.head
            i = 0
            while (i < pos - 1):
                i += 1
                elemento = elemento.next
            if pos == 0:
                nuevoNodo.next = self.head
                self.head = nuevoNodo
            else:
                nuevoNodo.next = elemento.next
                elemento.next = nuevoNodo
    
    # Metodo para eliminar el elemento de una posicion determinada de la lista
    def eliminarPos(self, pos):
        
        # Manejo de errores
        if self.head is None:
            print("Lista vacia")
            return
        # Sino, se recorre la lista hasta la posicion deseada
        else:
            
            elemento = self.head
            
            # Si la posicion es 0 se elimina el primer elemento
            if pos == 0:
                self.head = elemento.next
                return elemento.data
            
            i = 0
            
            while (i < pos - 1):
                i += 1
                elemento = elemento.next
                # Si el elemento es mayor al largo de la lista imprimer error
                if elemento.next is None:
                    print("Posicion no valida")
                    print("El largo de la lista es: ", i)
                    return
                
            # Si la posicion es el ultimo elemento se elimina el ultimo elemento
            
            elemento.next = elemento.next.next
            return elemento.data
                
            
    # Metodo para recorrer la lista e imprimir los datos de cada nodo
    def recorrer(self):
        # Si la lista esta vacia se imprime un mensaje
        if self.head is None:
            print("La lista esta vacia")
            return
        # Sino, se recorre la lista e imprime los datos de cada nodo
        apuntar = self.head
        while (apuntar):
            print(apuntar.data)
            apuntar = apuntar.next
    
    # Metodo para acceder a la posicion entregada de la lista
    def accederPos(self, pos):
        # Si la lista esta vacia se imprime un mensaje
        if self.head is None:
            print("Lista vacia")
            return
        # Si no, se recorre la lista hasta la posicion deseada
        else:
            elemento = self.head
            i = 0
            while (i < pos):
                i += 1
                elemento = elemento.next
                # Si el elemento es mayor al largo de la lista imprimer error
                if elemento.next is None:
                    print("Posicion no valida")
                    print("El largo de la lista es: ", i)
                    return 
            return elemento.data

# Funcion main para probar la lista enlazada
if __name__ == "__main__":
  
    print("Lista Enlazada Simple")
    print("Se ingresan 7 nodos en total")
        
    miListaEnlazada = ListaEnlazada()
    miNodo1 = Nodo(1)
    miNodo2 = Nodo(2)
    miNodo3 = Nodo(3)
    miNodo4 = Nodo(4)
    miNodo5 = Nodo(5)
    miNodo6 = Nodo(6)
    miNodo7 = Nodo(7)
    miListaEnlazada.head = miNodo1
    miListaEnlazada.insertarInicio(miNodo2.data)
    miListaEnlazada.insertarInicio(miNodo3.data)
    miListaEnlazada.insertarInicio(miNodo4.data)
    miListaEnlazada.insertarInicio(miNodo5.data)
    miListaEnlazada.insertarFinal(miNodo6.data)
    print("-----------------")
    print("Lista enlazada simple")
    miListaEnlazada.recorrer()
    print("-----------------")
    miListaEnlazada.insertarPos(miNodo7.data, 2)
    miListaEnlazada.recorrer()
    print("Se inserto el nodo", miNodo7.data, "en la posicion 2")
    print("-----------------")
    Eleminar_Pos = miListaEnlazada.eliminarPos(1)
    miListaEnlazada.recorrer()
    print("Se elimino el nodo", Eleminar_Pos, "en la posicion 1")
    print("-----------------")
    print("El nodo en la posicion 3 es: ", miListaEnlazada.accederPos(3))
    print("El nodo en la posicion 1 es: ", miListaEnlazada.accederPos(1))
    print("El nodo en la posicion 0 es: ", miListaEnlazada.accederPos(0))

        

# Comentario Documentacion
# Orden de Complejidad en notación O
# Las operaciones basicas(1 unidad de tiempo) son: O(1)
# El tiempo de un if es O(max(bloque_if, bloque_else))
# El tiempo de un for es la suma de sus tiempos usando la notación O-Grande

#-------------------------------------------#
# Tiempo de ejecucion de los metodos

# T(n)----->Tiempo de ejecucion

# Clase nodo   O(1)
# Clase ListaEnlazada O(1)

# Insertar al inicio: O(1)
# Insertar al final: O(n)
# Insertar en una posicion: O(n + 1) + O(1) = O(n)
# Eliminar en una posicion: O(n(1) + 1) + O(1) = O(n)
# Recorrer la lista: O(n) + O(1) = O(n)
# Acceder a una posicion: O(n(1)) + O(1) = O(n)

#-------------------------------------------#


# Resolucion

# O(4) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) + O(n) = 

# = O(4) + O(8n) = O(n)


