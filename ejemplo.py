class linked_list_circular:
  def _init_(self, head=None):
    self.head = head   # si solo tiene un elemnto, la cabecera va ser tambien el final
    self.size = 0


  def insertar (self, cliente):
    if  self.size == 0:  # sino hay nada el la cabecera
      self.head = node(cliente=cliente)
      self.head.next = self.head # la cabecera apunta a cabecera 
    else: 
      new_node = node(cliente=cliente, next=self.head.next)
      self.head.next = new_node 
    self.size += 1

  def inprimir (self):
    if self.head is None:   
      return
    node = self.head
    print(node.cliente.nombre, end = " => ")
    while node.next != self.head: # si ya no hay solo un elemnto entonces si recorrro todo
      node = node.next
      print(node.cliente.nombre, end=" => ")

  def eliminar (self, no_habitacion):
    node = self.head
    previous = None

    while True:
      if node.cliente.no_habitacion == no_habitacion:  # si la habitacion se encuentra en la cabecera
        if previous is not None: # si el anterior no esta vacio
          previous.next = node.next
        else:
          while node.next != self.head: #mientras siguiente de nodo es diferente de cabecera
            node = node.next # nodo obtiene el valor siguiente 
          node.next = self.head.next #el siguiente de nodo ahora sera el siguiente de cabecera
          self.head = self.head.next #la cabecera ahora sera el siguiente de la cabecera 
        self.size -= 1
        return True 
      elif node.next == self.head: # si el siguiente del nodo es igual a la cabecera no elimina
        return False

      previous = node
      node = node.next # al nodo le asigno el siguiente nodo
      
 #lista Doblemente Enlazada    
class cliente:
  def __init__(self, nombre, no_habitacion):
    self.nombre = nombre
    self.no_habitacion = no_habitacion

class node_de:
  def __init__(self, cliente=None, next=None, previous=None):
    self.cliente=cliente
    self.previous= previous
    self.next = next

class linked_list_de:
  
  def __init__(self, head=None):
    self.head = head
    self.last = head
    self.size = 0
  
  def insertar (self,cliente):
    if self.size == 0:
      self.head = node_de(cliente = cliente)
      self.last = self.head
    else:
      new_node = node_de(cliente = cliente, next=self.head)
      self.head.previous = new_node
      self.head = new_node
    self.size+=1 

  def imprimir (self):
    if self.head is None:
      return
    node = self.head
    print(node.cliente.nombre, end = "=>")
    while node.next:
      node = node.next
      print(node.cliente.nombre, end= "=>")
  def eliminar(self, no_habitacion):
    node = self.head
    while node is not None:
      if node.cliente.no_habitacion == no_habitacion:
        if node.previous is not None:
          if node.next:
              node.previous.next = node.next
              node.next.previous = node.previous
          else:
            node.previous.next = None
            self.last = node.previous
        else:
          self.head = node.next 
          node.next.previous = self.head
          self.size -= 1
          return True
      else:
        node = node.next
        return False

c1 = cliente("alexis lopez", 100)
c2 = cliente("ana ramirez", 101)
c3 = cliente("Sergi Roberto", 102)

lista_de = linked_list_de()
lista_de.insertar(c1)
lista_de.insertar(c2)
lista_de.insertar(c3)

lista_de.imprimir()

lista_de.eliminar(102)



class cola:
  def _init_(self):
    self.cola = []
  def encolar(self, cliete):
    self.cola.append(cliente)
  def devolver(self):
    return len(self.cola)
  def imprimir(self):
    for n in self.cola:
      print(n)
  def desencolar(self):
    if self.cola:
      self.cola.pop(0)
     
    
 class pila:
  def _init_(self):
    self.pila = []
  def apilar(self, cliete):
    self.pila.append(cliente)
  def devolver(self):
    return len(self.pila)
  def imprimir(self):
    for n in self.pila:
      print(n)
  def desapilar(self):
    if self.pila:
      self.pila.pop()
