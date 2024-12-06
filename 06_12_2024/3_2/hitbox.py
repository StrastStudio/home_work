class Hitbox:
    def __init__(self, x, y, w, h, padding=0):
        self.__x = x
        self.__y = y
        self.Pad = padding
        self.__SetWidth(w)
        self.__SetHeight(h)

    def __GetLeft(self):
        return self.__x

    def __GetRight(self):
        return self.__x + self.__w

    def __GetTop(self):
        return self.__y

    def __GetBottom(self):
        return self.__y + self.__h

    def __GetHeight(self):
        return self.__h

    def __GetWidth(self):
        return self.__w

    def __SetLeft(self, value):
        self.__x = value

    def __SetTop(self, value):
        self.__y = value

    def __SetWidth(self, value):
        if value <= 0: value = 1
        self.__w = value

    def __SetHeight(self, value):
        if value <= 0: value = 1
        self.__h = value

    def MoveTo(self, x, y):
        self.__SetLeft(x)
        self.__SetTop(y)

    def Move(self, dx, dy):
        self.__SetLeft(self.__x + dx)
        self.__SetTop(self.__y + dy)

    def Intersects(self, other):
        x = self.__x
        y = self.__y
        w = self.__w
        h = self.__h
        ox = other.x
        oy = other.y
        ow = other.w
        oh = other.h
        if x + w - self.Pad < ox + self.Pad: return False
        if x - self.Pad > ox + ow - self.Pad: return False
        if y + h - self.Pad < oy + self.Pad: return False
        if y + self.Pad > oy + oh - self.Pad: return False
        return True

    def __str__(self):
        return f"({self.__x=}, {self.__y=}, {self.__w=}, {self.__h=})"

    x = property(__GetLeft, __SetLeft)
    right = property(__GetRight)
    y = property(__GetTop, __SetTop)
    bottom = property(__GetBottom)
    w = property(__GetWidth, __SetWidth)
    h = property(__GetHeight, __SetHeight)
