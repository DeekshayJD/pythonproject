class circle:
    def area(self,r):
        ac=3.14*r*r
        print("area of circle",ac)

class square:
    def area(self,s):
        ac=s*s
        print("area of square",ac)

class rectangle(square):
    def area(self,l,b):
        ac=l*b
        print("area of rectangle",ac)

co=circle()
so=square()
ro=rectangle()
ro.area(10,20)
so.area(10)
co.area(2)