"""
Queue FIFO - LIFO PRIORITY

FIFO - First in First out
LIFO - Last in First out

Ejemplo con FIFO
"""

# libreria queue es nativa de python
import queue 

q = queue.Queue()

# Pongo un elemento en la cola
q.put(5)

q.put(10)

# Obtengo en una lista los elementos de la cola y lso presento n una lista
print(list(q.queue))

# Verifico si la cola se encuentra vacia
print(q.empty())

# Obtengo un elemento y lo elimino de la cola
print(q.get())

# Verifico que el elemento se elimino de la cola
print(list(q.queue))

print(q.get())

# Verifico que la cola se encuentre vacia
print(q.empty())


# Extraccion de elementos FIFO

for x in range(3):
    q.put(x)

print(list(q.queue))

while not q.empty():
    print(q.get(), end="\t")
