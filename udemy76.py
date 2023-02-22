class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposite(self,dept_amt):
        self.balance = self.balance + dept_amt
        print('Added {} amount to your account'.format(dept_amt))

    def withdrawal(self,wit_amt):
        if self.balance >= wit_amt:
            self.balance = self.balance - wit_amt
            print("Withdrawal accepted")

        else:
            print("Sorry not enough funds")


    def __str__(self):
        return "Owner: {} \nBalance: {}".format(self.owner,self.balance)


mybank = Account('Deven',5000)
print(mybank)

print(mybank.deposite(1000))
print(mybank)


print(mybank.withdrawal(5000))
print(mybank)


print(mybank.withdrawal(2000))