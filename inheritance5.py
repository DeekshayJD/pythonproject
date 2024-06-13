class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak_word(self):
        print(self.name+"  generic sound")


class  Dog(Animal):
    #def speak_word(self):
        pass

dog=Dog("brownie",23)
dog.speak_word()