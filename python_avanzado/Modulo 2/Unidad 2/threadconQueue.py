"""
Thread con Queue

"""

import queue
import threading
import time

def agregar_item(q):
    while True:
        print("inicio del hilo")
        # Cargo un elemento en la cola desde el hilo secundario
        q.put(4)
        time.sleep(2)
        print(list(q.queue))
        print("Ejecucion antes del break")
        break

# Creo una cola FIFO
q = queue.Queue()
# Creo un hilo secundario de ejecucion en el que se ejecutara la funcion agregar_item
# y se le pasa la cola q
t = threading.Thread(target=agregar_item, args=(q,))
# Inicio el hilo de ejecucion secundario
t.start()
# Pongo un elemento en la cola desde el hilo de ejecución principal
q.put(3)
# Espero a que finalcie el hilo de ejecución secundario
t.join()
# Printeo la cola resultante luego de ejecutar el hilo secundario
# Tiene el elemento que se cargo en el hilo principal y el elemento que se cargo
# en el hilo secundario
print(list(q.queue))
