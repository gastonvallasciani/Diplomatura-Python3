"""
Thread - Hilos de ejecución
"""

import threading
import time

def en_espera(arg, tiempo):
    print("Este argumento se pasa en el hilo: {}, {} segundos despues \n".format(arg, tiempo))
    # freno la app por un tiempo
    time.sleep(tiempo)
    print("El hilo: {} finaliza su ejecucion \n".format(arg))

# Definicion del hilo de ejecucion
t = threading.Thread(target=en_espera, name="thread", args=("thread", 7))
# Inicio el hilo
t.start()

print("hola")