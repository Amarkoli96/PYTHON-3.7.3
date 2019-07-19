class Account():
    def __init__(self,owner,balance=0):
        self.owner =owner
        self.balancce =balance
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print("Added {} to the balance".format(dep_amt))
    def withdrawl(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -=wd_amt
            print("With_drawal accepted")
        else:
            print("Insuficient funds")

    def __str__(self):
        return "owner:{} \n Balance: {}".format(self.owner,self.balance)


