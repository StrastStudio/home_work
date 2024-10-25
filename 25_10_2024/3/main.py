from tank import Tank
from tkinter import *

s = Tk()
s.title("Фикус")
CanvasTank = Canvas(s, width=800, height=600, bg="green")
CanvasTank.pack()
Player = Tank(CanvasTank, "Фикус", 100, 100, 100)
Enemy = Tank(CanvasTank, "Картошка", 100, 300, 300)

KeyNumbers = {"W": 87, "S": 83, "A": 65, "D": 68, "R": 82}

def HitboxSys():
    if Player.__Intersects(Enemy): return True

def KeyPress(event):
    if event.keycode == KeyNumbers["W"]: Player.__MoveSys(0, -1)
    if event.keycode == KeyNumbers["S"]: Player.__MoveSys(0, 1)
    if event.keycode == KeyNumbers["A"]: Player.__MoveSys(-1, 0)
    if event.keycode == KeyNumbers["D"]: Player.__MoveSys(1, 0)
    if event.keycode == KeyNumbers["R"]: Player.fuel = Player.__ammo = 100
    if HitboxSys(): print("ВЕСЕЛо")

s.bind("<KeyPress>", KeyPress)

s.mainloop()