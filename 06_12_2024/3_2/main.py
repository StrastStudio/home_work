import world as w
from tanks import *

KeyNumbers = {"W": 87, "S": 83, "A": 65, "D": 68, "R": 82, "UP": 38, "RIGHT": 39, "DOWN": 40, "LEFT": 37}

FPS = 60

def Update():
    Player.Update(CameraObj)
    UpdateList()
    w.UpdateMap(CameraObj)
    # Enemy.Update(CameraObj)
    CameraObj.update()
    # Player.Intersects(Enemy)
    # Enemy.Intersects(Player)
    s.after(1000 // FPS, Update)

def KeyPress(event):
    if event.keycode == KeyNumbers["W"]: Player.MoveSys(0, -1)
    if event.keycode == KeyNumbers["S"]: Player.MoveSys(0, 1)
    if event.keycode == KeyNumbers["A"]: Player.MoveSys(-1, 0)
    if event.keycode == KeyNumbers["D"]: Player.MoveSys(1, 0)
    if event.keycode == KeyNumbers["R"]: Player.fuel = Player.ammo = 100

s.bind("<KeyPress>", KeyPress)

Update()
s.mainloop()