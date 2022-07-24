"""
Thread - Hilos de ejecución

Si quiero frenar para que el programa principal frenara a que el 
hilo secundario me retornara la informacion puedo usar JOIN.
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
# Espero a que fialice la ejecución del hilo secundario
t.join()

print("hola")