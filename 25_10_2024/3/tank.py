from hitbox import  Hitbox

class Tank:
    __count = 0
    __SIZE = 100
    def __init__(self, canvas, model, ammo, x, y, speed=10):
        Tank.__count += 1
        self.__model = model
        self.__health = self.fuel = 100
        self.__xp = 0
        self.__ammo = ammo
        self.__x = max(x, 0)
        self.__y = max(y, 0)
        self.__speed = speed
        self.__canvas = canvas
        self.__hitbox = Hitbox(self.__x, self.__y, Tank.__SIZE, Tank.__SIZE)
        self.__create()

    @staticmethod
    def GetCount(): return Tank.__count

    @staticmethod
    def GetSize(): return Tank.__SIZE

    def GetModel(self): return self.__model

    def GetHealth(self): return self.__health

    def GetXp(self): return self.__xp

    def GetAmmo(self): return self.__ammo

    def GetX(self): return self.__x

    def GetY(self): return self.__y

    def GetSpeed(self): return self.__speed

    def GetHitbox(self): return self.__hitbox

    def __MoveSys(self, dx, dy):
        if self.fuel > 0:
            if dx == 1: self.__x += self.__speed
            if dx == -1: self.__x -= self.__speed
            if dy == 1: self.__y += self.__speed
            if dy == -1: self.__y -= self.__speed
            if sum([abs(dx), abs(dy)]): self.fuel -= 1
            self.__repaint()

    def __create(self):
        self.id = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + Tank.__SIZE, self.__y + Tank.__SIZE, fill="red")

    def __fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print("Стреляю!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def __repaint(self):
        self.__canvas.moveto(self.id, self.__x, self.__y)
        self.__hitbox.MoveTo(self.__x, self.__y)

    def __Intersects(self, OtherTank):
        return self.__hitbox.Intersects(OtherTank.__hitbox)

    def __str__(self):
        return (f"Model: {self.__model}, Fuel: {self.fuel}, "
              f"Health: {self.__health}, Ammo: {self.__ammo}, "
              f"X: {self.__x}, Y: {self.__y}")


