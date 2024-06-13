class bank:
    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount


    def withdraw(self,amount):
        if self.balance>amount:

            self.balance-=amount
        else:
            print("insufficient fund")

Bank=bank("12346",500)
print(Bank.accountnumber)
Bank.deposite(500)
print(Bank.balance)
Bank.withdraw(300)
print(Bank.balance)