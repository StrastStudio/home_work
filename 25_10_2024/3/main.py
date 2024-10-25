from tank import Tank
from tkinter import *
from os import chdir
chdir("25_10_2024/3")

s = Tk()
s.title("Фикус")
CanvasTank = Canvas(s, width=800, height=600, bg="green")
CanvasTank.pack()
Player = Tank(CanvasTank, "Фикус", 100, 100, 100)
Enemy = Tank(CanvasTank, "Картошка", 100, 300, 300)

KeyNumbers = {"W": 87, "S": 83, "A": 65, "D": 68, "R": 82}

def HitboxSys():
    if Player.Intersects(Enemy): return True

def KeyPress(event):
    if event.keycode == KeyNumbers["W"]: Player.MoveSys(0, -1)
    if event.keycode == KeyNumbers["S"]: Player.MoveSys(0, 1)
    if event.keycode == KeyNumbers["A"]: Player.MoveSys(-1, 0)
    if event.keycode == KeyNumbers["D"]: Player.MoveSys(1, 0)
    if event.keycode == KeyNumbers["R"]: Player.fuel = Player.ammo = 100
    if HitboxSys(): print("ВЕСЕЛо")

s.bind("<KeyPress>", KeyPress)

s.mainloop()