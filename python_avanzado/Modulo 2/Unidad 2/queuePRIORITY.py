"""
Queue FIFO - LIFO PRIORITY

FIFO - First in First out
LIFO - Last in First out

Ejemplo con PRIORITY
"""

# Libreria queue es nativa de python
import queue 

q = queue.PriorityQueue()

# Pongo los elementos en la cola detallando explicitamente el orden de prioridad mediante una tupla
# (prioridad, dato a guardar en al cola)
q.put((13, "Este es el ultimo"))
q.put((3, "Este va segundo"))
q.put((4, "Este va tercero"))
q.put((2, "Este va primero"))

# Obtengo en una lista los elementos de la cola y lso presento n una lista
print(list(q.queue))

# Levanto los datos de la cola y los presento según el orden de prioridad de salida
for i in range(q.qsize()):
    print(q.get())