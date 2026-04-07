class Bank:
 def create_account(self,name,acc_no,balance):
    self.name=name
    self.acc_no=acc_no
    self.balance=balance
 def deposit(self,amount):
   self.balance+=amount
   print("Amount Deposited:",amount)
 def withdraw(self,amount):
     if amount<=self.balance:
       self.balance-=amount
       print("Amount Withdrawn:",amount)
     else:
       print("Insufficient Balance")
 def display(self):
   print("Account Holder:",self.name)
   print("Account Number:",self.acc_no)
   print("Balance:",self.balance)
b = Bank()
b.create_account("Srinu",12345,1000)
b.deposit(500)
b.withdraw(2000)
b.display()