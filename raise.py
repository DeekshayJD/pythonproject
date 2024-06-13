class Too_youngException(Exception):
    def __init__(self,arg):
        self.msg=arg

class Too_oldException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("enter your age :-"))
if age<24:
    raise Too_youngException("plz wait for some more days")
elif age>60:
    raise Too_oldException("your age is too more search peacfully")

else:
    print("you can marrie rite now")

