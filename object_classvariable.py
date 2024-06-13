class MyClass:
    class_var = 10  # Class variable

    def __init__(self, obj_var):
        self.obj_var = obj_var  # Instance variable


# Create two instances of MyClass
obj1 = MyClass(20)
obj2 = MyClass(30)

# Access class variables and instance variables
print("Class variable id:", id(obj2.class_var))
print("Instance variable id for obj1:", id(obj1.obj_var))
print("Instance variable id for obj2:", id(obj2.obj_var))
