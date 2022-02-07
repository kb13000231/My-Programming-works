class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, nwidth):
        self.width = nwidth

    def set_height(self, nheight):
        self.height = nheight

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            return ''.join(['*'*self.width+'\n' for _ in range(self.height)])

    def get_amount_inside(self, shape):
        return self.get_area()//shape.get_area()


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side={})".format(self.width)

    def set_side(self, nside):
        self.width = nside
        self.height = nside
