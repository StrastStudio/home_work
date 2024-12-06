import texture as t
from tkinter import NW
from random import randint, choice

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WIDTH = SCREEN_WIDTH * 2
HEIGHT = SCREEN_HEIGHT * 2

GROUND = "Ground"
WATER = "Water"
CONCREATE = "Concreate"
BRICK = "Brick"
BLOCK_SIZE = 64

_Canvas = None
_Map = []

def CreateMap(rows = 20, cols = 20):
    global _Map
    _Map = []
    for i in range(rows):
        row = []
        for j in range(cols):
            block = GROUND
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                block = CONCREATE
            elif randint(1, 100) <= 15: block = choice([BRICK, WATER, CONCREATE])
            row.append(_Cell(_Canvas, block, BLOCK_SIZE * j, BLOCK_SIZE * i))
        _Map.append(row)

def UpdateMap(CameraObj):
    global _Map
    for row in _Map:
        for col in row:
            col.SetX(col.GetOx() - CameraObj.OffsetX)
            col.SetY(col.GetOy() - CameraObj.OffsetY)
            col.Move()

def Initialize(Canvas):
    global _Canvas
    global _Map
    _Canvas = Canvas
    CreateMap()

class Camera:
    def __init__(self, target):
        self.Target = target
        self.OffsetX = 0
        self.OffsetY = 0

    def update(self):
        self.OffsetX = min(WIDTH - 350, max(0, self.Target.x + self.Target.hb.w // 2 - SCREEN_WIDTH // 2))
        self.OffsetY = min(SCREEN_HEIGHT, max(0, self.Target.y + self.Target.hb.h // 2 - SCREEN_HEIGHT // 2))

class _Cell:
    def __init__(self, canvas, block, x, y):
        self.__canvas = canvas
        self.__block = block
        self.__Ox, self.__Oy = x, y
        self.__x, self.__y = x, y
        self.__CreateElement(self.__block)

    def __CreateElement(self, block):
        if block != GROUND:
            self.__id = self.__canvas.create_image(self.__x, self.__y, image=t.Get(block), anchor=NW)

    def __del__(self):
        try: self.__canvas.delete(self.__id)
        except: pass

    def GetBlock(self): return self.__block

    def GetOx(self): return self.__Ox

    def GetOy(self): return self.__Oy

    def SetX(self, value): self.__x = value

    def SetY(self, value): self.__y = value

    def Move(self):
        if self.__block != GROUND:
            self.__canvas.moveto(self.__id, self.__x, self.__y)