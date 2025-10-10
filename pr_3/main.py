from tkinter import *
from Score import Score
from Catcher import Catcher
import random
import time

tk = Tk()
tk.title("Гра: Ловець!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

tk.update()
time.sleep(3)

score = Score(canvas)
catcher = Catcher(canvas, 'blue', score)
tk.update()
time.sleep(1)

