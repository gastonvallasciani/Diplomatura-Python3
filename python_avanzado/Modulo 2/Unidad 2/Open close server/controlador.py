from logging import root
from tkinter import Tk
import vista

class Controller():
    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = vista.Ventanita(self.root_controller)

if __name__  == "__main__":
    root_tk = Tk()
    app  = Controller(root_tk)
    root_tk.mainloop()