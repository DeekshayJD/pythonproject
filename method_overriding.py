class p:
    def property(self):
        print("gold+cash+banglow")

    def marry(self):
        print("banglore")
class q(p):
    def marry(self):
        super().marry()
        print("hassan")

q1=q()
q1.marry()
q1.property()