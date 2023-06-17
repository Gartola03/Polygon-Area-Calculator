class Rectangle:

    def __init__(self, wid, hei):
        self.width = wid
        self.height = hei

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, wid):
        self.width = wid
    
    def set_height(self, hei):
        self.height = hei
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        picture = ""
        if (self.width >50 or self.height > 50):
            return "Too big for picture."
        i = 0
        while i < self.height:
            picture += ("*" * self.width) + "\n"
            i += 1
             
        return picture

    def get_amount_inside(self, object):
        
        if self.width < object.width or self.height < object.height:
            return 0
        return self.get_area() // object.get_area()

    
class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __repr__(self):
        return f'Square(side={self.width})' 

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, wid):
        self.width = wid
        self.height = wid
    
    def set_height(self, hei):
        self.height = hei
        self.width = hei
    
