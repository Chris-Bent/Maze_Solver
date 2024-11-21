from tkinter import Tk
from tkinter import BOTH
from tkinter import Canvas

class Line():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, Canvas, fillColour):
        canvas.create_line(
            x1, y1, x2, y2, fill=fillColour, width=2
        ) 
        