class student:
   def __init__(self,name,age):
       self.name=name
       self.age=age
class info(student):


      def __init__(self,name,age,color,sports):

          super().__init__(name,age)
          self.color=color
          self.sports=sports
      def display(self):
          print("my name",self.name)
          print(self.age)

          print(self.name)
          print(self.color)

s=info("deekshay",26,"pink","cricket")
s.display()
