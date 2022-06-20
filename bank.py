from datetime import datetime
from time import strftime

class Account:
    def __init__(self,name,account_number):
        self.balance=0
        self.name=name
        self.account_number=account_number
        self.deposits = []
        self.withdrawals =[]
        self.time=datetime.now().strftime('%x')
        self.statement=[]
        self.loan_balance=0
        self.trasaction={}
        self.depo=[]
        self.another_account2=0
        
        
        

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
            self.deposits.append({"date":self.time, "amount":amount, "narration":"Deposit"})
    
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
            self.withdrawals.append({"date":self.time, "amount":amount, "narration":"Withdraw"})
            return f"You have withdraw {amount},your new balance is {self.balance} and your withdrawals are{ self.withdrawals}."
        
    def deposits_statement(self):
            for statement in self.deposits:
             print(f" Your had deposited {statement} Ksh.", sep="\n")

    def withdrawals_statement(self):
        for v in self.withdrawals:
         print(f"You had withdraw {v}Ksh.", sep="\n")
         
    def current_balance(self):
        return (f"Your current balance is {self.balance}Ksh")
    
    def all_statements(self):
        full_stats = self.deposits + self.withdrawals
        for i in full_stats:
            print(i)
        
       
  
    def borrow(self,amount):  
        sum=0  
        for i in self.depo:
                sum+=i["amount"]
        
        if len(self.deposits) < 10:
            print("You must have made atleast ten deposits ")
        elif amount <100:
             print("You must have more than 100 loan request")
        elif amount <=(sum//3):
            print("You cannot borrow, amount must be ore than 1/3 deposits. Loan denied.")
        elif self.balance==0:
            print(f"You cant borrow. Your account balance is 0")
            
        
        elif self.loan_balance > 0:
                print("You don't have an outstanding loan balance")
        else :
            self.loan_balance=(0.03*amount)+amount
            return f"You have borrowed a loan of {amount} with have an interest of {0.03*amount} and your total loan amount is{self.loan_balance}"
            
            
    def repayment(self,amount):
        
        if amount<self.loan_balance:
                    self.loan_balance-=amount
                    print(f"You have paid off {amount}, and your new loan balance is {self.loan_balance}")
      
        else:
          amount>self.loan_balance
          amount-=self.loan_balance
          self.balance=self.balance+amount
        print(f"You have successfull paid off your loan, and your new current balance is {self.balance}")
    
    def transfer(self,amount,another_account):   
        if amount<0:
            print ("You cannot transfer")
        elif amount>self.balance:
            print("You have insufficient balance")  
        else:
            amount<self.balance
            self.balance-=amount
            self.another_account2+=amount
            print(f"You have transfered {amount} to {another_account} and your new balance is {self.balance}. The new account have received {amount} and the balance is {self.another_account2}")

    
        
        
            
        
        
