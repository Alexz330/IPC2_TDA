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
