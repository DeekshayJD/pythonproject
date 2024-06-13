'''
class P:
    def __init__(self):
        print("parent class")

class  Q(P):
    def __init__(self):
        super().__init__()
        print("child class")
q=Q()
'''

class P:
    def __init__(self, name="Parent"):
        print("Parent class:", name)

class Q(P):
    def __init__(self, name="Child"):
        super().__init__(name)
        print("Child class:", name)


# Creating instances
p1 = P()  # Uses default parameter value
p2 = P("Custom Parent")



#q1 = Q()  # Uses default parameter value
#q2 = Q("Custom Child")

