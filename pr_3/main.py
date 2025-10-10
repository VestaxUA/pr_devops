from tkinter import *
from Score import Score
from Catcher import Catcher
from Egg import Egg
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

eggs = []
while 1:
    if random.randint(1, 100) == 1:
        eggs.append(Egg(canvas, 'red', score))
    for egg in list(eggs):
        if egg.draw() == 'hit bottom':
            eggs.remove(egg)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.update()
time.sleep(1)




