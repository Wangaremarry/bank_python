from datetime import datetime
from time import strftime

class Account:
    def __init__(self,name,account_number):
        self.balance=0
        self.name=name
        self.account_number=account_number
        self.deposits = []
        self.withdrawals =[]
        self.time=datetime.now().strftime('%c')
        self.trasaction={}
        self.loan_balance=0
        self.statement=[]
        self.loan_balance=0
        
    def deposit(self,amount):
        dict_addmoney={}
        dict_addmoney.update({"date":self.time})
        dict_addmoney.update({"amount":amount})
        dict_addmoney.update({"narration":"deposit"})
        print(dict_addmoney)

        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            self.deposits.append(amount)
    
            return f"You have deposited {amount},your new balance is {self.balance} and your deposits are {self.deposits}."  

    def withdraw(self,amount):
        
        dict_withdrawal={}
        dict_withdrawal.update({"date":self.time})
        dict_withdrawal.update({"amount":amount})
        dict_withdrawal.update({"narration":"withdraw"})
        print(dict_withdrawal)
    
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
        
    def all_statements(self):
        for a in self.statement:
            date = a["date"]
            narration = a["narration"]
            amount = a["amount"]
            return f"{date}-----{narration}------{amount}"

    def borrow(self):
        total = sum(self.deposits)
        times= len(self.deposits)
        check = 1/3*(self.loan_amount)
        self.loan_balance+= (0.03*self.loan_amount)+self.amount
        if self.amount<=10:
            print("Loan requested must be greater than 0")
        elif self.amount<100:
            print("Loan amount requested must be more than 100")
        elif self.amount <(sum//3):
            print("You are not qualified for this loan")
        elif self.amount > 0:
            print("You need to clear the outstanding loan") 
        else:
            return f"You have borrowed{self.amount} with an interest of {self.amount} and your balance is {self.loan_balance}"
        
            
    def current_balance(self):
             print(f"Your current balance {self.balance}Ksh" )
    
    def loan_payment(self,amount):
        loan=loan<amount
        if loan<amount:
            print(f"You have paid {amount} and your loan balance is {self.balance}")
        elif loan>amount:
            print("You have succefully repaid you full loan  and your current blance is {self.balnce}")
            