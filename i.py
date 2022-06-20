from datetime import datetime
from time import strftime


class Account:
          def __init__(self,account_name,account_number,):
                 self.account_name = account_name
                 self.account_number = account_number
                 self.balance = 0
                 self.deposits = []
                 self.withdrawals = []   
                 self.transaction={}
                 self.loan_balance= 0 
                 self.statement= []            
                 
          def deposit(self,amount):
              self.balance += amount
              time=strftime("%c")
              narration="You deposited"
              self.transaction={amount,time,narration}
              if amount <=0:
                print( f"Deposit must be a positive number") 
              else:
               self.deposits.append(amount)
              print( f" Hello {self.account_name} Your current balance is {self.balance} and your deposits is {amount}")
              print(self.transaction)
              print(f" You have deposited {len(self.deposits)} times")

          def withdraw(self,amount):
              self.amount=amount
              transaction_fee= 100
              to_withdraw= self.amount+transaction_fee
              narration="You have withdrawn"
              time=strftime("%c")
              self.transaction={amount,time,narration}
              if amount <=0:
                return f"Withdraw must be greater than zero"
              elif to_withdraw >self.balance:
                return f"Your balance is {self.balance}, you can't withdraw {amount}"
              else:
                self.balance -=to_withdraw
                self.withdrawals.append(amount)
              print( f"Hello {self.account_name} you have withdrawn {amount} your new balance is {self.balance} and your withdrawals are {len(self.withdrawals)}")
              print(self.transaction)

          def deposits_statement(self):
            for amount in self.deposits:
              print(f"Your recent deposit is {amount} your total deposits are {sum(self.deposits)}")




          def full_statement(self):
              for money_transaction in self.statement:
                  amount=money_transaction["amount"]
                  Narration=money_transaction["Narration"]
                  time=money_transaction["time"]
                  date=time.strftime("%x/%X")
                  print(f"{date}: {Narration} {amount}")
                  
          def transfer(self,receiver,amount):
            self.receiver=receiver
            self.amount=amount
            current_balance=self.balance-amount
            if amount<=0:
                print( f"You cannot transfer a non-existant amount")
            elif amount>self.balance:
                print(f"Your cannot transfer {amount}.Your current balance is {self.balance}")
            elif amount<self.balance:
                print(f"You have transfered {amount} to {self.receiver} your current balance is {current_balance}")

          def  borrow_loans(self,loan_amount):
            self.loan_amount=loan_amount
            self.interest=0.03*self.loan_amount
            self.total_loan=self.loan_amount+self.interest
            if len(self.deposits)>10 and loan_amount<=sum(self.deposits)//3 and loan_amount>100 and self.balance<0:
                print(f"You have been awarded a loan of {loan_amount} your current balance is {self.amount}")
            else:
                print("You are not eligible for a loan")

          def pay_loans(self,amount_payloan):
              self.amount_payloan=amount_payloan
              self.interest=0.03*self.loan_amount
              total_topay=amount_payloan+self.interest
              loan_remaining=self.loan_amount-amount_payloan
              new_balance=self.loan_amount-total_topay
              if total_topay>0:
                  print(f"You have deposited {amount_payloan} your loan of {self.loan_amount}Ksh.Your new loan balance is {new_balance}Ksh")
              elif total_topay>loan_remaining:
                  print(f"Congratulations!! You have cleared your loan of {self.amount}.Your new balance is{new_balance}")
              else:
                  print(f"You have a loan balance of {self.total_loan}")
          def current_balance(self):
             print(f"Your current balance {self.balance}Ksh" )