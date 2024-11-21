from tkinter import Tk
from tkinter import BOTH
from tkinter import Canvas

class Window():
    def __init__(self, width, height)
        
        # Create Tk window
        self.__root = Tk()
        __root.title("Maze Solver")
        self.__root.protocol("WM_delete_window", self.close)

        # Creating a screen that can expand
        # to the size of the window
        self.screen = Canvas(self.__root, width=width, height=height)
        self.screen.pack(fill=BOTH, expand=True)

        # Running window 
        self.running = False

    # Screen update method
    def redraw():
        self.__root.update_idletasks()
        self.__root.update()
        
    def waitForClose():
        self.running = True
        while self.running == True:
            self.redraw()

    def close():
        running = False
