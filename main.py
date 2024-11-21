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

        
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
            
    def draw(self, canvas, fillColour="black"):
        canvas.create_line(
            self.startPoint.x, self.startPoint.y,
            self.endPoint.x, self.endPoint.y, 
            fill=fillColour, width=2
        )

class Cell():
    def __init__(self):
        self.hasLeftWall = hasLeftWall
        self.hasRightWall = hasRightWall
        self.hasTopWall = hasTopWall
        self.hasBottomWall = hasBottomWall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        

def main():

    win = Window(800, 600)

    pointOne = Point(50, 50)
    pointTwo = Point(350, 350)

    line = Line(pointOne, pointTwo)

    line.draw(win.screen, fillColour="red")

    win.waitForClose()

if __name__ == "__main__":
    main()