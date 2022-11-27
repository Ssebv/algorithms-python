# Mini suma de arbol simple
class Nodo:
    def __init__(self, data, lst):
        self.data = data
        self.hijos = lst

def suma(nd, ini):
    global v
    v += nd.data
    for i in nd.hijos:
        suma(i, ini)
    return v + ini

if __name__ == "__main__":
    n3 = Nodo(50, [Nodo(10, [Nodo(5, []), Nodo(5, [])]), Nodo(40, [Nodo(20, []), Nodo(20, [])])])
    v = 0
    n1 = Nodo(1, [Nodo(2, []), Nodo(3, [])])
    n2 = Nodo(1, [Nodo(2, [Nodo(3, []), Nodo(4, [])]), Nodo(5, [Nodo(6, []), Nodo(7, [])])])
    print(suma(n2, 2))
    v = 0
    print(suma(n1, 1))
    v = 0
    print(suma(n3, 1))


