class Account:
    def __init__(self,name,account_number):
        self.balance=0
        self.name=name
        self.account_number=account_number
        self.deposits = []
        self.withdrawals =[]
        
        
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
            return f"You have deposited {amount},your new balance is {self.balance} and your deposits are {self.deposits}."  

    def withdraw(self,amount):
        self.trasaction=100
        if amount>self.balance:
             return f"Your balance is {self.balance},so you cannot withdraw the {amount}." 
        elif amount<=0:
            return f"Amount must be greater than zero" 
        else:
            self.balance-=amount+self.trasaction
            self.withdrawals.append(amount)
            return f"You have withdraw {amount},your new balance is {self.balance} and your withdrawals are{ self.withdrawals}." 
    

    def deposits_statement(self):
        for statement in self.deposits:
         print(statement, sep="\n")

    def withdrawals_statement(self):
        for v in self.withdrawals:
         print(v, sep="\n")
        
    def current_balance(self):
        return self.balance
        
    
        