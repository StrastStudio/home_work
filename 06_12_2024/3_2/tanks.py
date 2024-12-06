import world as w
from tank import Tank
from tkinter import *
from random import choice
import texture as t
from world import Initialize
s = Tk()
s.title("Фикус")
t.LoadTextures()
CanvasTank = Canvas(s, width=w.SCREEN_WIDTH, height=w.SCREEN_HEIGHT, bg="green")
CanvasTank.pack()
Initialize(CanvasTank)
Tanks = []
Player = Tank(CanvasTank, "Фикус", 100, 100, 100, bot=False, speed=5)
CameraObj = w.Camera(Player)
# Enemy = Tank(CanvasTank, "Картошка", 100, 300, 300, bot=True)
# Enemy.Player = Player

def CreateTanks(Range):
    for _ in range(Range+1):
        Tanks.append(Tank(CanvasTank, "Картошка", 100, choice(range(0, 1600+1)), choice(range(0, 1600+1)), bot=True))
        Tanks[-1].Player = Player

def CheckCollishion(TankObj):
    for TankObj2 in Tanks:
        if TankObj2 != TankObj:
            TankObj2.Intersects(TankObj)
            if not Player.Intersects(TankObj2):
                if TankObj2.Intersects(Player):
                    Player.Dx = 0
                    Player.Dy = 0
        else:
            continue

def UpdateList():
    for TankObj in Tanks:
        TankObj.Update(CameraObj)
        # TankObj.Intersects(Player)
        CheckCollishion(TankObj)


CreateTanks(10)