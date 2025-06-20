#Using class and function to do withdraw ,deposit and scheck the balance
class BankAccount():
    
    def __init__ (self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
        self.interest_rate=3
    
    def get_details(self):
        print(f"Account Details are:\n\tAccount number:{self.account_number}\tAccount Holder:{self.account_holder}")
    
    def get_deposit(self,deposit):
        self.balance=self.balance+deposit
        #print(f"Current Balance is {self.balance}")
    
    def do_withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        #print(f"Current Balance is {self.balance}")
    
    def check_balance(self):
        print(f"Interest added = {self.interest}")
        print(f"Current Balance is {self.balance}")
    
    def get_interest(self):
        self.interest=(self.balance*self.interest_rate*3)/100
        self.balance=self.balance+self.interest
        

customer1=BankAccount(101546,'Kiruhtika',20000)
customer1.get_details()
customer1.get_deposit(10000)
customer1.do_withdraw(29000)
customer1.get_interest()
customer1.check_balance()
