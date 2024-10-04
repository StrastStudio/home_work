class Hitbox:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__set_width(width)
        self.__set_height(height)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    def __get_y(self):
       return self.__y

    def __set_y(self, y):
       self.__y = y

    def __get_width(self):
       return self.__get_width

    def __set_width(self, width):
        if width < 0:
            width = 0
        self.__width = width

    def __get_height(self):
       return self.__get_height

    def __set_height(self, height):
        if height < 0:
            height = 0
        self.__height = height

    def moveto(self, x, y):
        self.__set_x(x)
        self.__set_y(y)

    def move(self, dx, dy):
        self.__set_x(dx + self.__get_x())
        self.__set_y(dy + self.__get_y())

    def __get_top(self):
        return self.y

    def __get_bottom(self):
        return self.y + self.height

    def __get_left(self):
        return self.x
    
    def __get_right(self):
        return self.x + self.width

    def intersects(self, other):
        if self.left > other.right:
            return False
        elif self.top > other.bottom:
           return False
        elif self.right > other.left:
           return False
        elif self.bottom > other.top:
            return False
        else:
            return True


    def __str__(self):
        return f"{self.__x=},{self.__y=},{self.__width=},{self.__height=}"

    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)
    width = property(__get_width, __set_width)
    height = property(__get_height, __set_height)

    left = property(__get_left)
    right = property(__get_right)
    top = property(__get_top)
    bottom = property(__get_bottom)


SIZE = 100
class Tank:
    def __init__(self, canvas, x, y, model='Т-14 Армата', ammo=100, speed = 10):
        self.__hitbox = Hitbox(x, y, Tank.SIZE, Tank.SIZE)        
        Tank.__count += 1
        self.__hitbox = Hitbox(x, y, Tank.__SIZE, Tank.__SIZE)
        self.__speed = speed
        self.__canvas = canvas
        self.__model = model
        self.__fuel = 100
        self.__hp = 100
        self.__xp = 0
        self.__ammo = ammo
        self.__x = x
        self.__y = y
        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0

        self.create()

    def __update_hitbox(self):
        self.__hitbox.moveto(self.x, self.y)

    def forward(self):
        if self.fuel > 0:
            self.y  += -self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()

    def backward(self):
        if self.fuel > 0:
            self.y  += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()

    def left(self):
        if self.fuel > 0:
            self.y += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()

    def right(self):
        if self.fuel > 0:
            self.y += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()

    def intersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    # def check_collision():
    #     if player.intersects(enemy):
    #         print('Танки столкнулись')

    # def key_press():
    #     if event.keycode == KEY_W:
    #         player.forward()
    #     if event.keycode == KEY_A:
    #         player.left()
    #     if event.keycode == KEY_S:
    #         player.backward()
    #     if event.keycode == KEY_D:
    #         player.right()

    #     check_collision()