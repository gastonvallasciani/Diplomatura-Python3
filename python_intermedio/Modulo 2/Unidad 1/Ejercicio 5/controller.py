from tkinter import Tk
import vista

class Controller:
    def __init__(self, root_w):
        self.root = root_w
        self.objeto_vista=vista.Panel(self.root)

if __name__=="__main__":
    root = Tk()
    mi_app=Controller(root)
    root.mainloop()