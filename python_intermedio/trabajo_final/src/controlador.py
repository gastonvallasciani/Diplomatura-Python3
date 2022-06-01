"""
controlador.py
"""
from tkinter import Tk 
from vista import Panel

__author__ = "Gastón Vallasciani"
__maintainter__ = "Gastón Vallasciani"
__email__ = "gastonvallasciani@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"


class Controller():
    def __init__(self, root_w):
        self.root = root_w
        self.objeto_vista = Panel(self.root)

if __name__ == "__main__":
    root_tk = Tk()
    mi_app = Controller(root_tk)
    root_tk.mainloop()
    