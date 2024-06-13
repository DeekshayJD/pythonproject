class circle(object):
    def draw(self):
        print("area of circle")

class rectangle:
    def draw(self):
        print("area of rectangle")

class square(circle,rectangle):
    def draw(self):
        circle.draw(self)
        rectangle.draw(self)
        print("area of square")

so=square()
so.draw()
