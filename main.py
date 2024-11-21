from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        
        # Create Tk window
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol(
            "WM_delete_window", self.close
            )

        # Creating a screen that can expand
        # to the size of the window
        self.screen = Canvas(self.__root, width=width, height=height)
        self.screen.pack(fill=BOTH, expand=True)

        # Running window 
        self.running = False

    # Screen update method
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def waitForClose(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def drawLine(self, Line, fillColour):
        line = Line(draw)
        getLine = draw.Line(Canvas, "White")
        

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, x, y):
        self.startPoint = startPoint
        self.endPoint = endPoint
        
    def draw(self, Canvas, fillColour):
        canvas.create_line(
            self.startPoint.x, self.startPoint.y,
            self.endPoint.x, self.endPoint.y, 
            fill=fillColour, width=2
        )

def main():

    win = Window(800, 600)
    win.waitForClose()

    pointOne = Point(50)
    pointTwo = Point(350)

    line = Line(pointOne, pointTwo)

    line.draw(window.screen, fillColour)

    window.waitForClose()

if __name__ == "__main__":
    main()