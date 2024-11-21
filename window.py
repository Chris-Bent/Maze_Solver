from tkinter import Tk
from tkinter import BOTH
from tkinter import Canvas

class Window():
    def __init__(self, width, height)
        
        # Create Tk window
        self.__root = Tk()
        __root.title("Maze Solver")
         
        # Creating a screen that can expand
        # to the size of the window
        self.screen = Canvas(self.__root, width=width, height=height)
        self.screen.pack(fill=BOTH, expand=True)

        # Running window. Set to false
        self.running = False

    # Screen update method
    def redraw():
        self.__root.update_idletasks()
        self.__root.update()
        
    def waitForClose():
        

    def close():