from tank import Tank
from tkinter import *
from os import chdir
try: chdir("31_10_2024/3")
except: pass

s = Tk()
s.title("Фикус")
CanvasTank = Canvas(s, width=800, height=600, bg="green")
CanvasTank.pack()
Player = Tank(CanvasTank, "Фикус", 100, 100, 100)
Enemy = Tank(CanvasTank, "Картошка", 100, 300, 300)

KeyNumbers = {"W": 87, "S": 83, "A": 65, "D": 68, "R": 82, "UP": 38, "RIGHT": 39, "DOWN": 40, "LEFT": 37}

FPS = 60

def HitboxSys():
    if Player.Intersects(Enemy): return True

def Update():
    OldPos = {"X": Player.x, "Y": Player.y}
    Player.Update()
    if HitboxSys(): 
        print("ВЕСЕЛо")
        Player.x = OldPos["X"]
        Player.y = OldPos["Y"]
    s.after(1000 // FPS, Update)

def KeyPress(event):
    if event.keycode == KeyNumbers["W"]: Player.MoveSys(0, -1)
    if event.keycode == KeyNumbers["S"]: Player.MoveSys(0, 1)
    if event.keycode == KeyNumbers["A"]: Player.MoveSys(-1, 0)
    if event.keycode == KeyNumbers["D"]: Player.MoveSys(1, 0)
    # Передвижение врага по клавишам на клавиатуре.
    # if event.keycode == KeyNumbers["UP"]: Enemy.MoveSys(0, -1)
    # if event.keycode == KeyNumbers["DOWN"]: Enemy.MoveSys(0, 1)
    # if event.keycode == KeyNumbers["LEFT"]: Enemy.MoveSys(-1, 0)
    # if event.keycode == KeyNumbers["RIGHT"]: Enemy.MoveSys(1, 0)
    if event.keycode == KeyNumbers["R"]: Player.fuel = Player.ammo = 100

s.bind("<KeyPress>", KeyPress)

Update()
s.mainloop()