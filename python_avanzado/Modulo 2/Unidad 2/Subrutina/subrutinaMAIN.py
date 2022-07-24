"""
Subrutinas - Como lanzar desde un programa una subrutina

Por ejemplo se podria utilizar para lanzar desde la app el encendido de un servidor mediante una subrutina.
"""
from asyncio import subprocess
import sys
import os
from pathlib import Path
import subprocess

global elproceso
elproceso = ""

# Obtengo donde se encuentra el archivo main con respecto al test que quiero ejecutar
raiz = Path(__file__).resolve().parent
# Especifico ruta donde se encuentra el test que quiero encontrar
ruta = os.path.join(raiz, "subrutinaTEST.py")

the_path = ruta

elproceso = subprocess.Popen([sys.executable, the_path])
# Ejecuto el subproceso test
elproceso.communicate()