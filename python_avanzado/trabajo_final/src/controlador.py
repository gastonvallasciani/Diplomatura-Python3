"""
controlador.py
"""
from tkinter import Tk 
from vista import Panel
import observer_pattern_module.observer
#------------------------------------------------------------------------------
__author__ = "Gastón Vallasciani"
__maintainter__ = "Gastón Vallasciani"
__email__ = "gastonvallasciani@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"
#------------------------------------------------------------------------------
class Controller():
    def __init__(self, root_w):
        self.root = root_w
        self.objeto_vista = Panel(self.root)
        print(self.objeto_vista)
        self.observer = observer_pattern_module.observer.ConcreteObserverA(self.objeto_vista.abmc)
    def __str__(self,):
        return("Clase Controller()")
#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Version del modulo: ", __version__)
    print("Autor: ", __author__)
    root_tk = Tk()
    mi_app = Controller(root_tk)
    print(mi_app)
    root_tk.mainloop()
#------------------------------------------------------------------------------
    