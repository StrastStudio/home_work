import tkinter as tk
from random import randint


class Shape:
    """Базовый класс для всех геометрических фигур."""
    
    def __init__(self, canvas):
        self.canvas = canvas
        
    def draw(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе.")

    def move(self, dx=0, dy=0):
        raise NotImplementedError("Метод должен быть реализован в подклассе.")


class Circle(Shape):
    """Класс для представления круга."""
    
    def __init__(self, canvas, x, y, radius, color="blue"):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.id = None  # Идентификатор объекта на холсте

    def draw(self):
        self.id = self.canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill=self.color
        )

    def move(self, dx, dy):
        if self.id is not None:
            self.canvas.move(self.id, dx, dy)
            self.x += dx
            self.y += dy


class AnimationManager:
    """Менеджер анимации, управляющий движением объектов."""
    
    def __init__(self, root, shapes):
        self.root = root
        self.shapes = shapes
        self.dx = 5
        self.dy = 5
        self.animation_loop()

    def animation_loop(self):
        for shape in self.shapes:
            shape.move(self.dx, self.dy)
            
            # Проверка границ окна
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            if shape.x < 0 or shape.x > width:
                self.dx *= -1
            if shape.y < 0 or shape.y > height:
                self.dy *= -1
                
        self.root.after(50, self.animation_loop)  # Повтор через 50 мс


# Создание главного окна приложения
root = tk.Tk()
root.title("Анимация")

# Холст для рисования
canvas = tk.Canvas(root, bg='white', width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Генерация случайных кругов
shapes = []
for _ in range(10):
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(20, 60)
    c = f'#{randint(0x000000, 0xFFFFFF):06X}'
    circle = Circle(canvas, x, y, r, c)
    circle.draw()
    shapes.append(circle)

# Запуск менеджера анимации
manager = AnimationManager(root, shapes)

# Основной цикл программы
root.mainloop()