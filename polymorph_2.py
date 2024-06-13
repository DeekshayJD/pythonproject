file_name="deek.txt"
with open(file_name,"r")as fo:
    #fo.write("good morning")
    print(fo.readline())















class circle(object):
    def draw(self):
        print("drawing circle class")

class rectangle(circle):
    def draw(self):
       # super().draw()
        print("drawing rectangle")

class square(rectangle):
    def draw(self):
        super().draw()
        print("drawing square")

so=square()
so.draw()