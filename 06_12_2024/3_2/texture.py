from tkinter import  PhotoImage

_Frames = {}

def Load(Name, FileName): _Frames[Name] = PhotoImage(file=FileName)

def Get(Name): return _Frames[Name]

def LoadTextures():
    Load("TankUp", "../IMG/00003010.png")
    Load("TankRight", "../IMG/00003011.png")
    Load("TankDown", "../IMG/00003012.png")
    Load("TankLeft", "../IMG/00003013.png")
    Load("Concreate", "../IMG/00003014.png")
    Load("Brick", "../IMG/00003015.png")
    Load("Water", "../IMG/00003016.png")