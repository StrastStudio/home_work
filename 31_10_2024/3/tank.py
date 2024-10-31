from hitbox import  Hitbox
from tkinter import PhotoImage, NW

class Tank:
    __count = 0
    # __SIZE = 100
    def __init__(self, canvas, model, ammo, x, y, speed=1):
        Tank.__count += 1
        self.__ImgUp = PhotoImage(file = "../IMG/00003010.png")
        self.__ImgDown = PhotoImage(file = "../IMG/00003012.png")
        self.__ImgRight = PhotoImage(file = "../IMG/00003011.png")
        self.__ImgLeft = PhotoImage(file = "../IMG/00003013.png")
        self.__model = model
        self.__health = self.fuel = 100
        self.__xp = 0
        self.__ammo = ammo
        self.__x = max(x, 0)
        self.__y = max(y, 0)
        self.__speed = speed
        self.__canvas = canvas
        self.__hitbox = Hitbox(self.__x, self.__y, self.GetSize(), self.GetSize())
        self.Dx = 0
        self.Dy = 0
        self.__create()
        self.MoveSys(1, 0)


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
        if self.fuel > 0:
           self.__y += self.Dy * self.__speed
           self.__x += self.Dx * self.__speed
        self.fuel -= 1
        self.repaint()

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
        self.__canvas.moveto(self.__id, self.__x, self.__y)
        self.__hitbox.MoveTo(self.__x, self.__y)

    def Intersects(self, OtherTank):
        return self.__hitbox.Intersects(OtherTank.__hitbox)

    def __str__(self):
        return (f"Model: {self.__model}, Fuel: {self.fuel}, "
              f"Health: {self.__health}, Ammo: {self.__ammo}, "
              f"X: {self.__x}, Y: {self.__y}")

    ammo = property(GetAmmo, SetAmmo)
    x = property(GetX, SetX)
    y = property(GetY, SetY)
