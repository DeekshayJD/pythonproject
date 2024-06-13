class Test:
    def m1(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print("plz provide 2 or 3 argument")

t=Test()
t.m1(10)
t.m1(20,30)
t.m1(10,20,30)
