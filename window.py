from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        super().__init__(self, width, height)
        
        # Create Tk window
        self.__root = Tk()
        __root.title("Maze Solver")
        
        # Creating a screen that can expand
        # to the size of the window
        self.screen = Canvas(self.__root)
        __root.pack(fill = BOTH, expand = True)

        # Running window. Set to false
        self.running = False
