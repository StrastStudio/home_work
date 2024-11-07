from hitbox import  Hitbox
from tkinter import PhotoImage, NW
from random import  randint
import world as w

class Tank:
    __count = 0
    # __SIZE = 100
    def __init__(self, canvas, model, ammo, x, y, speed=1, bot=True):
        Tank.__count += 1
        self.__ImgUp = PhotoImage(file = "../IMG/00003010.png")
        self.__ImgDown = PhotoImage(file = "../IMG/00003012.png")
        self.__ImgRight = PhotoImage(file = "../IMG/00003011.png")
        self.__ImgLeft = PhotoImage(file = "../IMG/00003013.png")
        self.__model = model
        self.__health = self.fuel = 10000
        self.__xp = 0
        self.__ammo = ammo
        self.__x = max(x, 0)
        self.__y = max(y, 0)
        self.OldPos = {"X": self.__x, "Y": self.__y}
        self.__speed = speed
        self.__canvas = canvas
        self.__hitbox = Hitbox(self.__x, self.__y, self.GetSize(), self.GetSize(), padding=10)
        self.Dx = 0
        self.Dy = 0
        self.__create()
        self.MoveSys(1, 0)
        self.__Bot = bot
        self.Player = None

    @staticmethod
    def GetCount(): return Tank.__count

    def GetSize(self): return self.__ImgUp.width()

    def GetModel(self): return self.__model

    def GetHealth(self): return self.__health

    def GetXp(self): return self.__xp

    def GetAmmo(self): return self.__ammo

    def GetX(self): return self.__x

    def GetY(self): return self.__y

    def GetSpeed(self): return self.__speed

    def GetHitbox(self): return self.__hitbox

    def SetAmmo(self, Value): self.__ammo = Value
    
    def SetX(self, Value): self.__x = Value
    
    def SetY(self, Value): self.__y = Value
    
    def Update(self):
        if self.__Bot:
            if randint(1, 30) == 30:
                if randint(1, 10) < 9:
                    if self.Player.x > self.__x: self.MoveSys(1, 0)
                    if self.Player.x < self.__x: self.MoveSys(-1, 0)
                    if self.Player.y > self.__y: self.MoveSys(0, 1)
                    if self.Player.y < self.__y: self.MoveSys(0, -1)
                else: self.ChangeOrientation()
        if self.fuel > 0:
           self.__y += self.Dy * self.__speed
           self.__x += self.Dx * self.__speed
        self.fuel -= 1
        self.repaint()

    def ChangeOrientation(self):
        rnd = randint(0, 3)
        if rnd == 0: self.MoveSys(1, 0)
        if rnd == 1: self.MoveSys(-1, 0)
        if rnd == 2: self.MoveSys(0, 1)
        if rnd == 3: self.MoveSys(0, -1)

    def CheckWorldBorders(self):
        hb = self.__hitbox
        if hb.x < 0 or hb.y < 0 or hb.right > w.WIDTH and hb.bottom > w.HEIGHT: 
            self.UndoMove()
            if self.__Bot: self.ChangeOrientation()

    def MoveSys(self, dx, dy):
        if dx == 1:
            self.Dx = 1
            self.Dy = 0
            self.__canvas.itemconfig(self.__id, image=self.__ImgRight)
        if dx == -1:
            self.Dx = -1
            self.Dy = 0
            self.__canvas.itemconfig(self.__id, image=self.__ImgLeft)
        if dy == 1:
            self.Dx = 0
            self.Dy = 1
            self.__canvas.itemconfig(self.__id, image=self.__ImgDown)
        if dy == -1:
            self.Dx = 0
            self.Dy = -1
            self.__canvas.itemconfig(self.__id, image=self.__ImgUp)

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y, image=self.__ImgUp, anchor=NW)

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print("Стреляю!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def repaint(self):
        self.OldPos = {"X": self.__x, "Y": self.__y}
        self.__canvas.moveto(self.__id, self.__x, self.__y)
        self.__hitbox.MoveTo(self.__x, self.__y)
        self.CheckWorldBorders()

    def Intersects(self, OtherTank):
        if self.__hitbox.Intersects(OtherTank.__hitbox):
            self.UndoMove()
            if self.__Bot: self.ChangeOrientation()
            return True
        return False

    def UndoMove(self):
        if sum([self.Dx, self.Dy]) == 0: return
        self.__x = self.OldPos["X"]
        self.__y = self.OldPos["Y"]
        self.Dx = 0
        self.Dy = 0

    def __str__(self):
        return (f"Model: {self.__model}, Fuel: {self.fuel}, "
              f"Health: {self.__health}, Ammo: {self.__ammo}, "
              f"X: {self.__x}, Y: {self.__y}")

    ammo = property(GetAmmo, SetAmmo)
    x = property(GetX, SetX)
    y = property(GetY, SetY)